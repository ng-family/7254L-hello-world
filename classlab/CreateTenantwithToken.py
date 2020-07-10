import requests
import json

url = "http://192.168.10.1/api/aaaLogin.json"
payload = "{\n\"aaaUser\": {\n\"attributes\": {\n\"name\": \"admin\",\n\"pwd\": \"ciscoapic\"\n}}}"
headers = {'Authorization': 'Basic YWRtaW46Y21zY29hG1j'}
response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)

json_response = json.loads(response.text)
tokenfromlogin = (json_response['imdata'][0]['aaaLogin']['attributes']['token'])

url = "http://192.168.10.1/api/node/mo/uni/tn-TEST_TENANT.json"

payload = "{\
  \"fvTenant\": {\
    \"attributes\": {\
      \"dn\": \"uni/tn-testtenant\",\
      \"name\": \"testtenant\",\
      \"rn\": \"tn-testtenant\",\
      \"status\": \"created\"\
    },\
    \"children\": []\
  }\
}"
payload = "{\"fvTenant\":{\"attributes\":{\"dn\":\"uni/tn-TEST_TENANT\",\"status\":\"created\"},\"children\":[]}}"

cookie = {"APIC-cookie": tokenfromlogin}
response = requests.request("POST", url, data=payload, cookies=cookie)

print(response.text)
