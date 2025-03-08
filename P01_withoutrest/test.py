import requests

BASE_URL = "http://127.0.0.1:8000/"
ENDPOINT = 'json'

try:
    response = requests.get(BASE_URL + ENDPOINT)
    response.raise_for_status()  # Raise an exception for bad status codes
    
    print(f"Response type: {type(response)}")
    data = response.json()
    print("Response data:", data)

except requests.exceptions.RequestException as e:
    print(f"Error making request: {e}")
except ValueError as e:
    print(f"Error parsing JSON response: {e}")