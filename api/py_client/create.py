import requests

endpoint = "http://localhost:8000/api/koalas/" 

data = {
    'sex': 'm', 
    'dob': '2022-08-15'
}
get_response = requests.post(endpoint) 
print(get_response.json())

#POST is currently off ???