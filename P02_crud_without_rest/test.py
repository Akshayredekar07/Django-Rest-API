import requests

BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'api/'
ENDPOINT1 = 'api1/'
ENDPOINT2 = 'api2/'

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def get_resource():
    response = requests.get(f"{BASE_URL}{ENDPOINT}/")
    print(response.status_code)
    print(response.json())


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def get_resource1(emp_id):
    response = requests.get(f"{BASE_URL}{ENDPOINT1}{emp_id}/")
    print(response.status_code)
    print(response.json())



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# get_resource()


emp_id = input("Enter Employee ID: ")
get_resource1(emp_id)


 