from email import header
from urllib import response
import requests
import pandas as pd
import json

api_key = "HvYZ4aDJuj-Vo84UZRgPKuVgBKT4MD0q0cw_d27eyu_eLLbIGvLaPWo71ZNsyVNft-4q-cSBcFiAq9zUWr_GK94nLiFXhDGwnLg3KkEt2qEDt8rwzdZ9JG5CWONBY3Yx"

my_headers = {
    'Authorization': 'Bearer %s' % api_key,
}

target_url = 'https://api.yelp.com/v3/businesses/search'
response_t = requests.get(url = target_url, headers = my_headers, params = {"location": "NYC"}).json()['businesses']
print(response_t)

# cache the result
with open("restaurant_info.json", 'w') as f:
    f.write(json.dumps(response_t))
    f.close()
