
import requests
from getpass import getpass
'''
from datetime import date

auth_endpoint = "http://localhost:8000/pl/auth/"
password = getpass()
auth_response = requests.post(auth_endpoint, json={'username':'admin', 'password': password}) 

token = auth_response.json()['token']
endpoint = "http://localhost:8000/pl/api/registrations/" 

data = {
    "plate": "EBR40XXESCORT24",
                "start_date": '2022-07-25' #' #,
                #"end_date": None
}
headers = {'Authorization': f"Token {token}"}
get_response = requests.post(endpoint, json=data, headers=headers)
'''

auth_endpoint = "http://localhost:8000/pl/auth/"
password = getpass()
auth_response = requests.post(auth_endpoint, json={'username':'admin', 'password': password}) 

#endpoint = "http://localhost:8000/pl/api/registrations/"

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    endpoint = "http://localhost:8000/pl/api/vehicles/18/" 
#auth = requests.auth.HTTPBasicAuth('admin', 'badmin')
    data = {
        #"plate": "EBR40XX",
        "make": "ford",
        "model": "escort",
        "registrations": [
            {
                "plate": "EBR40XXESCORT-typ2"#,
                #"start_date": None,
                #"end_date": None
            }
        ],
        "type": "Truck-tractor",
        "first_registration": "2000-04-05",
        "vin_number": "f200109899gfdd",
        "axles": 2,
        "production_year": 2000,
        "weight": 0.0,
        "gvm": 0.0,
        "gcwr": 0.0,
        "suspension": "Air suspension"
    }
    #print(data)
    #data = {
    #   "plate": "EBR001API200s"
    #}

    headers = {'Authorization': f"Token {token}"}
    
    get_response = requests.patch(endpoint, json=data, headers=headers)
     
    #print(get_response.json())
    #print("STATUS CODE", get_response.status_code)
    print("STATUS CODE", get_response.status_code, get_response.text)
