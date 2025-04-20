import requests

API_KEY = 'paste_your_key_here'
SEARCH_ENGINE_ID = 'paste_your_id_here'
search_query = 'book'

url = 'https://www.googleapis.com/customsearch/v1'
params = {
    'q': search_query,
    'key': API_KEY,
    'cx': SEARCH_ENGINE_ID
}

response = requests.get(url, params=params)
results = response.json()

# Print the first result link if available
if 'items' in results:
    print(results['items'][0]['link'])


## change the API Key And Site Id Of Your OWN