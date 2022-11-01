from urllib import response
import requests

#url = "http://127.0.0.1:8001/api/users_list/"

#response = requests.get(url)
#print(response.text)

#get auth token
#def get_token():
url = "http://127.0.0.1:8001/api/users_list/"
response = requests.get(url)
print(response.text)