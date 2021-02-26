  
import os
import requests

os.system('pip install get-mac')
os.system('pip3 install get-mac')

from getmac import get_mac_address as gma

mac=gma()

#print(mac)

x = requests.get('https://api.macvendors.com/'+mac)

#print(x.text)
if x.text =='Microsoft Corporation' or x.text=='Xensource, Inc.' or x.text=='VMware, Inc.' :
	print('Its a vm')
else:
	print('Not a vm')
x=input("end ans")
