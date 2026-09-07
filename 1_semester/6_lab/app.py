import os
import math

import httpx

print(f"Environment: {os.getenv('ENV_NAME')}")

url = os.getenv('URL')
r = httpx.get(url)
print(r.status_code)

import requests
r = requests.get(url)
print(r.status_code)
