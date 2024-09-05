#!/usr/bin/python3
"""Takes in a URL, prints an error message with a status code. """
import requests
import sys

if __name__ == "__main__":
    # Get the URL from command line arguments
    url = sys.argv[1]

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the status code is greater than or equal to 400
    if response.status_code >= 400:
        # Print the error code
        print(f"Error code: {response.status_code}")
    else:
        # Print the body of the response
        print(response.text)
