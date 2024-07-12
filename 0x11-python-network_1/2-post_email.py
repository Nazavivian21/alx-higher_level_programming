#!/usr/bin/python3
import urllib.parse
import urllib.request
import sys

url = sys.argv[1]
email = sys.argv[2]

data = urllib.parse.urlencode({'email': email})
data = data.encode('utf-8')

req = urllib.request.Request(url, data)

with urllib.request.urlopen(req) as response:
  # Decode response body
  body = response.read().decode('utf-8')
  # Print the response body
  print(body)