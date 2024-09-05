#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL"""
import requests
import sys

if __name__ == "__main__":
    # Get the URL from the command line arguments
    url = sys.argv[1]

    # Send a GET request to the URL
    response = requests.get(url)

    # Retrieve the value of X-Request-Id from the response headers
    x_request_id = response.headers.get('X-Request-Id')

    # Print the value of X-Request-Id
    print(x_request_id)
