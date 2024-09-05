#!/usr/bin/python3
"""Fetches a URL and displays the body of the response."""
import requests

if __name__ == "__main__":
    # Fetch the URL
    response = requests.get('https://alx-intranet.hbtn.io/status')

    # Display the response body in the required format
    print("Body response:")
    print(f"\t- type: {type(response.text)}")
    print(f"\t- content: {response.text}")
