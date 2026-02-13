import httpx
r = httpx.get('https://www.google.com/')
print(r.status_code)

import requests
r = requests.get('https://www.google.com/')
print(r.status_code)
