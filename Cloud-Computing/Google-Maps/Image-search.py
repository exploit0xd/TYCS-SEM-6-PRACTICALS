import requests

# Read API key and Search Engine ID from files
API_KEY = Your-api-key
SEARCH_ENGINE_ID = Your-api-key

# Define the search query
search_query = 'linux book'

# Set up the request URL and parameters
url = 'https://www.googleapis.com/customsearch/v1'
params = {
    'q': search_query,
    'key': API_KEY,
    'cx': SEARCH_ENGINE_ID,
    'searchType': 'image'
}

# Make the API request
response = requests.get(url, params=params)
results = response.json().get('items', [])

# Print the image links
for item in results:
    print(item['link'])

## change the API Key And Site Id Of Your OWN