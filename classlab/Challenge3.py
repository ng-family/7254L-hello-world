# This script will add a network object named Development with IP address of 100.1.1.1
# Then it will add vlan 600 name Construction and vlan 700 name Analysis
# Then add a static route 216.48.1.0/24 to 10.1.1.1
import requests
import json
from lxml import etree
from ncclient import manager

# ASAv, add network object.
url = "https://192.168.10.100/api/objects/networkobjects"
payload = "{\r\n  \"host\": {\r\n    \"kind\": \"IPv4Address\",\r\n    \"value\": \"100.1.1.1\"\r\n  },\r\n  \"kind\": \"object#NetworkObj\",\r\n  \"name\": \"Development\",\r\n  \"objectId\": \"Development\"\r\n}"
headers = {
    'Content-Type': "application/json",
    'Authorization': "Basic ZW5hYmxlXzE6Y2lzY28="
    }
#response = requests.request("POST", url, data=payload, verify=False, headers=headers)
#print(response.text)

# NXOSv, add 2 vlans
url='http://192.168.10.60/ins'
switchuser='admin'
switchpassword='Passw0rd1'
newvlans = [['600','Construction'], ['700', 'Analysis']]
myheaders={'content-type':'application/json'}
payload_input = 'conf t '
for each in newvlans:
    payload_input += ';vlan {} ;name {} '.format(each[0], each[1])
print(payload_input)
payload={
  "ins_api": {
    "version": "1.0",
    "type": "cli_conf",
    "chunk": "0",
    "sid": "1",
    "input": payload_input,
    "output_format": "json"
  }
}
#response = requests.post(url,data=json.dumps(payload), verify=False, headers=myheaders,auth=(switchuser,switchpassword)).json()
#print(response)
#IOS XE, add static route

url = "http://192.168.10.80/restconf/api/config/native/ip/route"

payload = "{\r\n\t\"ned:route\": {\r\n\t\t\"ip-route-interface-forwarding-list\": [{\r\n\t\t\t\"prefix\": \"216.48.1.0\",\r\n\t\t\t\"mask\": \"255.255.255.0\",\r\n\t\t\t\"fwd-list\": [{\r\n\t\t\t\t\"fwd\": \"10.1.1.1\"\r\n\t\t\t}]\r\n\t\t}]\r\n\t}\r\n}"
headers = {
    'Content-Type': "application/vnd.yang.data+json",
    'Accept': "application/vnd.yang.data+json",
    'Authorization': "Basic YWRtaW46Y2lzY28="
    }

response = requests.request("PATCH", url, data=payload, headers=headers)

print(response.text)
