# call_API.py
import pandas as pd

def call_API(weather_type, num_data_pts):
    # df = pd.read_csv(‘https://api.thingspeak.com/channels/12397/fields/4.csv?results=20’)
    
    # create the url out of a couple different strings
    url1 = 'https://api.thingspeak.com/channels/12397/fields/'
    w_select_dict = {'temperature':4,'humidity':5}
    
    url2 = str(w_select_dict[weather_type])
    url3 = '.csv?results='
    url4 = str(num_data_pts)
    
    url = url1 + url2 + url3 + url4
    # call the url to create the dataframe
    df = pd.read_csv(url)
    
    # return a dataframe with the data
    return df
