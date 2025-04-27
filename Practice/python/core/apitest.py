import requests

# The API endpoint
url = "https://restcountries.com/v3.1/all"

# A GET request to the API
response = requests.get(url)

# Print the response
print(response.json())
