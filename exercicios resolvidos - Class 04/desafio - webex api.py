import requests
import json

WEBEX_API_URL = 'https://webexapis.com/v1/messages'
WEBEX_ACCESS_TOKEN = 'ZDg2YzEyNjctOTgxOS00ZDg5LTg4YjYtOGMzZTZmNTFjOTU4MzVjZDQ1ZjMtNjEx_P0A1_6d9a73cd-a6ab-4e5e-86bf-e02773888d51'


httpHeaders = {'Authorization': f'Bearer {WEBEX_ACCESS_TOKEN}'}


body = {'toPersonEmail': 'victor.vhsc@gmail.com', 'text':'Quem está te respondendo é o robo, ele determina as regras'}

response = requests.post(url=WEBEX_API_URL, headers=httpHeaders, json=body)

print(response.status_code)
print(json.dumps(response.json(), indent=2))
