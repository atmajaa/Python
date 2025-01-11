import requests;
api_url = "https://dog.ceo/api/breed/hound/list"
response = requests.get(api_url)

status_code = response.status_code
print(status_code)

response_json = response.json()
print(response_json)