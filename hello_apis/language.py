import os

import requests

print('Language Detection Program ')

# Example text in another language
text = 'Bonjour le monde!'

# API's URL
url = 'http://apilayer.net/api/detect'

# Get the key from the environment variables
# Make sure you set this before running the program.
key = os.environ.get('LANGUAGE_KEY')

# Query parameters, send as part of the request.
# API key and the text to identify the language for
query_params = {'access_key': key, 'query': text}

# Make the request, include the URL and query parameters
# Convert JSON response to Python dictionary
response = requests.get(url, params=query_params).json()

print(response)

results = response['results']  # results is a list
if results:     # Make sure there's at least one item
    top_result = results[0]
    language = top_result['language_name']
    print(f'{language} is the best guess for the language of "{text}".')
else:
    print('No results for this text.')



