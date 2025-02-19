import requests

# Make a GET request to the GitHub API
response = requests.get("https://api.github.com")

# Print the JSON response from the API
print(response.json())