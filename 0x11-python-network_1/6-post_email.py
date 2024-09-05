#!/usr/bin/python3
"""Takes in a URL and an email address, displays the body of the response."""
import requests
import sys

if __name__ == "__main__":
    # Get the URL and email from command line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Define the payload with the email
    data = {'email': email}

    # Send a POST request with the email as a parameter
    response = requests.post(url, data=data)

    # Print the body of the response
    print(response.text)
