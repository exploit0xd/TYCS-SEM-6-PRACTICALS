import requests

API_KEY = 'Your-api-key'
SEARCH_ENGINE_ID = 'Your-api-key'
search_query = 'dogs'

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