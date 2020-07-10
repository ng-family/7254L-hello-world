import requests

url = "https://192.168.10.1/api/aaaLogin.json"

payload = "{\n\"aaaUser\": {\n\"attributes\": {\n\"name\": \"admin\",\n\"pwd\": \"ciscoapic\"\n}}}"
response = requests.request("POST", url, verify=False,data=payload)

print(response.text)