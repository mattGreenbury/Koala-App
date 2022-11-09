import requests

endpoint = "http://localhost:8000/api/" #http://127.0.0.1:8000/

get_response = requests.get(endpoint, json={"koala_id": 1}) #http request
#print(gblanket_response.text) # print raw text response\
#print(get_response.status_code)


# http request -> html
# rest api http request -> json
# javascript object notation ~ python dictionary

print(get_response.json())
#print(get_response.status_code)