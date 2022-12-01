import pandas as pd

def split_zipcode(zipcode_str: str):
    '''
        split the zipcodes by comma and 'and'
    '''
    result = []
    zipcodes = zipcode_str.replace("and", ",").split(",")
    for zipcode in zipcodes:
        zipcode_striped = zipcode.strip()
        if len(zipcode_striped) != 0 :
            result += [zipcode_striped]
    return result

def return_dict(df):
    '''
        return a dict with zipcode as key and population as value
    '''
    pop_dict = {}
    for i in range(0, 1599):
        rank = df.iloc[i, 0]
        zipcode_str = df.iloc[i, 1]
        population = df.iloc[i, 2]
        zipcodes = split_zipcode(zipcode_str)

        for zipcode in zipcodes:
            pop_dict[zipcode] = population
    
    return pop_dict

df = pd.read_html("https://www.newyork-demographics.com/zip_codes_by_population")[0]
pop_dict = return_dict(df)


