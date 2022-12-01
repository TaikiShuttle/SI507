from email import header
from urllib import response
import requests
import pandas as pd
import json
api_key = "HvYZ4aDJuj-Vo84UZRgPKuVgBKT4MD0q0cw_d27eyu_eLLbIGvLaPWo71ZNsyVNft-4q-cSBcFiAq9zUWr_GK94nLiFXhDGwnLg3KkEt2qEDt8rwzdZ9JG5CWONBY3Yx"

def get_businesses(location, api_key):
    headers = {'Authorization': 'Bearer %s' % api_key}
    url = 'https://api.yelp.com/v3/businesses/search'

    data = []
    for offset in range(0, 1000, 50):
        params = {
            'limit': 50, 
            'location': location,
            'offset': offset
        }

        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data += response.json()['businesses']
        elif response.status_code == 400:
            print('400 Bad Request')
            break

    return data

# cache the result
with open("restaurant_info.json", 'w') as f:
    data = get_businesses(location = "NYC", api_key = api_key)
    f.write(json.dumps(data))
    f.close()