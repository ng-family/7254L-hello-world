import re
interface = 'Hardware is CSR vNIC, address is 0050.5602.415a (bia 0050.5602.415a)'
mac = re.search('0050.56.{7}', interface)
print 'There is a device with OUI:'
print(mac.group(0))