import requests

url = "http://192.168.10.1/api/node/mo/uni/tn-testtenant/"

payload = "{\"fvTenant\": {\"attributes\": {\"dn\": \"uni/tn-testtenant\",\"name\": \"testtenant\",\"rn\": \"tn-testtenant\",\"status\": \"created\"},\"children\": []}}"

cookie = {"APIC-cookie": "3C6bClcLtoXJ2wSOdulbhCKpH9HOtstxDU3ltdbZ6AmBUvZ1u7ha0woZ8vfbqUVQlJNzlcePic8UVWJP1eWMdPsIR6zWVkwbo170pY0s5LnLlrnzeZYF76PDrb9l2Dcpm2APLWh3yiPJYx7VM48wsMcmCkej3pLkRdgIlSygjxg="}
response = requests.request("POST", url, data=payload, cookies=cookie)

print(response.text)