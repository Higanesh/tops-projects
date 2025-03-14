import requests


data = requests.get("http://127.0.0.1:8000/api/viewstudents/").json()
print(data[0]['id'])
print(data[0]['username'])
print(data[0]['email'])
print(data[0]['phone'])
print(data[0]['age'])