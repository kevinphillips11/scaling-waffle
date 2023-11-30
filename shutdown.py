import requests

url = "https://handy-labrador-humane.ngrok-free.app/close_the_app?token=johnlocke"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
