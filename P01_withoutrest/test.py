import requests

BASE_URL = "http://127.0.0.1:8000/"
# ENDPOINT = 'jsoncbv1/'
ENDPOINT = 'jsoncbv2/' # mixins

try:
    # response = requests.post(BASE_URL + ENDPOINT)
    # response = requests.put(BASE_URL + ENDPOINT)
    response = requests.delete(BASE_URL + ENDPOINT)
    response.raise_for_status()  
    
    print(f"Response type: {type(response)}")
    data = response.json()
    print("Response data:", data)

except requests.exceptions.RequestException as e:
    print(f"Error making request: {e}")
    print(f"Response status code: {response.status_code}")
    print(f"Response content: {response.content}")
except ValueError as e:
    print(f"Error parsing JSON response: {e}")
