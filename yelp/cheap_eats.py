import os 
import requests

YELP_API_KEY = os.environ.get('YELP_API_KEY')

yelp_url = 'https://api.yelp.com/v3/businesses/search'

query = input('What type of restaurants? ')

headers = {'Authorization': 'Bearer ' + YELP_API_KEY}
params = { 
    'term' : query,
    'categories': 'restaurants',
    'location': 'Minneapolis,MN',
    'radius': '10000',
    'price': 1,
    'limit': 50
}

response = requests.get(yelp_url, headers=headers, params=params).json()

restaurants = response['businesses']

for r in restaurants:
    name = r['name']
    rating = r['rating']
    location = r['location']
    address = ','.join(location['display_address'])

    print(f'{name}, {rating}, {address}')

