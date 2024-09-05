#!/usr/bin/python3
"""A python file that takes in a URL and sends request to a URL"""

import urllib.request
import sys

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    headers = response.headers

x_request_id = headers.get('X-Request-Id')
print(x_request_id)
