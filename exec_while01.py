#!/usr/bin/python
import requests


r = requests.get('https://uol.com.br')
site = r.status_code
# print(site)




while(site != 200):
    r = requests.get('https://uol.com.br')
    site = r.status_code
    print(site)
