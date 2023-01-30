import requests


api_url = "https://reqres.in"
endpoint_url = "/api/users/2"

uri = api_url+endpoint_url

response = requests.request("GET",uri)
print(response.status_code)
print(response.json())

if response.status_code == 200:
    print("Pass")

else:
    print("Fail")


