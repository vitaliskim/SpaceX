import requests

# URL for SpaceX API
url = "https://api.spacexdata.com/v4/launches"

# Send GET request to SpaceX API
response = requests.get(url)

# Convert the response to JSON
data = response.json()

# Print the number of launches
print(f"Number of launches: {len(data)}")
