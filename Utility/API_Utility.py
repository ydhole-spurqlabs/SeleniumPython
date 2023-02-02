import json
import requests


class API_Utility:
    data = json.load(open("Resources/config.json"))
    api_url = data['APIURL']

    def GET_Call(self,endpoint):
        uri = self.api_url+endpoint
        response = requests.request("GET", uri)
        return response


