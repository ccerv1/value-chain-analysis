import io
import json
import os
import pandas as pd
import requests
import time
import zipfile



class WorldBank:

    _BASE_URL       = "http://api.worldbank.org/v2/country/"
    _API_STRING     = "{}/indicator/{}?date={}&per_page={}&source=2&format=json"
    _NUM_RESULTS    = 10000 # set to the max by default

    @staticmethod
    def build_dataframe(json_data):
    
        df = pd.DataFrame.from_records(json_data)
        
        # clean up and format the data a little bit
        df['country'] = df['country'].apply(lambda x: x['value'])
        df['ind_code'] = df['indicator'].apply(lambda x: x['id'])
        df['indicator'] = df['indicator'].apply(lambda x: x['value'])
        
        cols = ['countryiso3code', 'country', 'ind_code', 'indicator', 'date', 'value']
        return df[cols]    

    @staticmethod
    def api(country_list, indicator_list, date_range, as_dataframe=True):

        country_q = ';'.join(country_list)
        indicator_q = ';'.join(indicator_list)
        date_q = ':'.join(str(x) for x in date_range)

        api_query = WorldBank._API_STRING.format(country_q, 
                                                 indicator_q, 
                                                 date_q, 
                                                 WorldBank._NUM_RESULTS)
        
        url = "".join([WorldBank._BASE_URL, api_query])
        
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Error {response.status_code}: {url}")
            return None

        result = response.json()

        try:
            if as_dataframe:
                return WorldBank.build_dataframe(result[1])
            else:
                return result
        except:
            print("No results:", url)


class Comtrade:

    _BASE_URL       = 'http://comtrade.un.org/api/get?'
    _API_STRING     = "max=500&type=C&freq={}&px=HS&ps={}&r=all&p=0&rg=all&cc={}"
    _COMMODITY_CODE = "090111"
    _DIRS           = ['annual', 'monthly', 'country_data']
    _COUNTRY_CODES  = "comtrade_country_codes.json"
    _SPECIAL_NAMES  = {
                        'Laos': "Lao People's Dem. Rep.",
                        'Tanzania': 'United Rep. of Tanzania',
                        'Vietnam': 'Viet Nam',
                        "Cote d'Ivoire": "Côte d'Ivoire",
                        "Bolivia": "Bolivia (Plurinational State of)",
                        "Congo (Kinshasa)": "Dem. Rep. of the Congo",
                        "Dominican Republic": "Dominican Rep."
                    }   

    _COLS = {
        'yr': 'Year',
        'periodDesc': 'Period',
        'rgDesc': 'Flow',
        'rtTitle': 'ImportCountry',
        'ptTitle': 'Country',
        'pt3ISO': 'ISO',
        'NetWeight': 'Weight',
        'TradeValue': 'Value'
    }

    def __init__(self, datadirectory, subdir='country_data'):

        self.data = None
        self._datadirectory = datadirectory
        self.load(subdir=subdir)
    

    def load(self, subdir='country_data'):
        if subdir not in Comtrade._DIRS:
            raise Exception(f"period_type must be in {Comtrade._DIRS}")

        data_path = self._datadirectory + subdir + '/'
        files = os.listdir(data_path)
        files = [f"{data_path}{file}" for file in files if file[-4:] == '.csv']
        dfs = [pd.read_csv(f, index_col=0) for f in files]
        df = pd.concat(dfs, axis=0, ignore_index=True)    
        df.rename(columns=Comtrade._COLS, inplace=True)
        df = df[self._COLS.values()]
        df = df.replace(dict((v,k) for k,v in Comtrade._SPECIAL_NAMES.items()))
        self.data = df


    @staticmethod
    def get_country_code(country, json_path):
        
        j = json.load(open(json_path))
        codes = {r['text']: r['id'] for r in j['results']}
        country_name = Comtrade._SPECIAL_NAMES.get(country, country)
        country_code = codes.get(country_name)
        return country_code


    def country_api(self, country, year):

        # determine the country code
        codes_path = self._datadirectory + Comtrade._COUNTRY_CODES
        country_code = Comtrade.get_country_code(country, codes_path)
        if not country_code:
            raise Exception(f"No country code for {country}")

        datapath = self._datadirectory + "country_data/"
        filename = "{}{}_{}.csv".format(datapath, year, country.replace(" ","_"))
        try:
            if len(pd.read_csv(filename)):
                return None
        except:
            pass

        # max=500&type=C&freq=A&px=HS&ps=2010&r=all&p=231&rg=1&cc=090111
        api_string = "&".join([
            "max=500",
            "type=C",
            "freq=A",
            "px=HS",
            f"ps={year}",
            "r=all",
            f"p={country_code}",
            "rg=1",
            f"cc={Comtrade._COMMODITY_CODE}"
        ])

        # request the API call
        url = Comtrade._BASE_URL + api_string
        response = requests.get(url)
        
        num_tries = 0
        while True:
            try:
                result = response.json()            
                json_data = result['dataset']
                break
            except:
                num_tries += 1
                print("Retrying:", country, year)
                time.sleep(5)
                if num_tries > 2:
                    print("Error at:", url)
                    return None

        # dump the data
        try:
            df = pd.DataFrame.from_records(json_data)    
            df.to_csv(filename)
            print("Success! Data dumped to:", filename)
            return df
        except:
            print("Error! Could not dump data to:", filename)
            return None

    

    def api_query(self, period_type, year, month=None):

        # build the query string
        if period_type=='monthly' and month:
            period = '{}{:02}'.format(year, month)
            freq = 'M'
        else:
            period = str(year)
            freq = 'A'
        query_string = Comtrade._API_STRING.format(
                        freq, period, Comtrade._COMMODITY_CODE)

        # request the API call
        url = Comtrade._BASE_URL + query_string
        response = requests.get(url)
        
        try:        
            result = response.json()
            json_data = result['dataset']
        except:
            status = response.status_code
            print(f"{status}: error at:", url)
            return None

        # dump the data
        datapath = self._datadirectory + period_type + '/'
        filename = "{}{}.csv".format(datapath, period)
        try:
            df = pd.DataFrame.from_records(json_data)    
            df.to_csv(filename)
            print("Success! Data dumped to:", filename)
            return df
        except:
            print("Error! Could not dump data to:", filename)
            return None




class USDA:

    _ATTR_COL      = 'Attribute_Description'
    _COUNTRY_COL   = 'Country_Name'
    _CODE_COL      = 'Country_Code'
    _USDA_BASE_URL = 'https://apps.fas.usda.gov/psdonline/downloads/'
    _DOWNLOAD_PATH = _USDA_BASE_URL + 'psd_coffee_csv.zip'
    _CSV_FILENAME  = 'psd_coffee.csv'
    _YEARS         = ['Market_Year', 'Calendar_Year']

    def __init__(self, datadirectory, year_type='Market_Year'):

        if year_type not in self._YEARS:
            raise Exception(f"year_type must be in {self._YEARS}")


        datapath = datadirectory + self._CSV_FILENAME
        try:
            data = pd.read_csv(datapath, index_col=0)
        except:
            self.refresh_data(datadirectory)
            data = pd.read_csv(datapath, index_col=0)

        self.attribute_list = sorted(list(data[self._ATTR_COL].unique()))
        self.country_list = sorted(list(data[self._COUNTRY_COL].unique()))
        self.year_type = year_type
        self.data = data        

        cc = data[[USDA._COUNTRY_COL, USDA._CODE_COL]]
        cc = cc[~cc.duplicated()]
        self.country_codes = dict(zip(cc[USDA._COUNTRY_COL], cc[USDA._CODE_COL]))
        
    

    def query_for_country(self, country, attributes=[]):
        df = self.data[self.data[self._COUNTRY_COL] == country]
        if attributes:
            df = df[df[self._ATTR_COL].isin(attributes)]
        return df.pivot_table(
            index=self._ATTR_COL, 
            columns=self.year_type, 
            values='Value'
        )
    
    def query_for_attribute(self, attribute, countries=[]):
        df = self.data[self.data[self._ATTR_COL] == attribute]
        if countries:
            df = df[df[self._COUNTRY_COL].isin(countries)]
        return df.pivot_table(
            index=self._COUNTRY_COL, 
            columns=self.year_type, 
            values='Value'
        )
    
    def refresh_data(self, datadirectory):
        response = requests.get(self._DOWNLOAD_PATH)
        zf = zipfile.ZipFile(io.BytesIO(response.content))
        dataset = pd.read_csv(zf.open(self._CSV_FILENAME))
        self.data = dataset
        dataset.to_csv(datadirectory + self._CSV_FILENAME)
