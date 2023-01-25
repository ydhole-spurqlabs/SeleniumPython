import requests
import json
api_url = "https://reqres.in"
endpoint_url = "/api/users"

uri = api_url+endpoint_url

payload = {
    "name": "morpheus",
    "job": "leader"
}

response = requests.request("GET",uri,data=payload)
print(response.status_code)
response_body = response.json()
print(response_body)