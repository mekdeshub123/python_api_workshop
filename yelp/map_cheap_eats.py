import os 

import requests
import folium 

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

minneapolis_location = [44.97, -93.26]
map = folium.Map(location=minneapolis_location, zoom_start=12)


for r in restaurants:
    name = r['name']
    rating = r['rating']
    location = r['location']
    address = ', '.join(location['display_address'])
    lat = r['coordinates']['latitude']
    lng = r['coordinates']['longitude']

    popup = f'<p><b>{name}</b></p><p>{rating} stars</p><p>{address}</p>'

    folium.Marker([lat, lng], popup=popup).add_to(map)
    print(f'{name}, {rating}, {address}')


map.save('cheap_eats_map.html')
