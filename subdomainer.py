
# SIMPLE SUBDOMAIN SCANNER USING PYTHON

#!/usr/bin/env python3

import requests
import sys

try:
	wordlist=sys.argv[1]
	with open(wordlist,'r') as handle:
		content=[line.strip() for line in handle.read().split('\n') if line]
except Exception:
	
	print("PLEASE ENTER THE WORDLIST NAME FOR SCANNING:")
	sys.exit()

Domain=input("ENTER THE DOMAIN NAME TO SCAN :")

Discovered_domain=[]

for contents in content:
	url=f"http://{contents}.{Domain}"
	try:
		requests.get(url)
	except requests.ConnectionError:
		pass

	else:
		print('[+] DISCOVERED DOMAIN :',url)
		Discovered_domain.append(url)

