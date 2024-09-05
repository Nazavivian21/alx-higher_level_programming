#!/usr/bin/python3
"""Sends a POST request to a URL with the letter as a parameter."""
import requests
import sys

if __name__ == "__main__":
    # Get the letter from command line arguments
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    # Define the payload with the letter
    data = {'q': q}

    # Send a POST request with the letter as a parameter
    response = requests.post('http://0.0.0.0:5000/search_user', data=data)

    try:
        # Attempt to parse the response as JSON
        result = response.json()

        # Check if the result is an empty dictionary
        if result:
            # Print the id and name if available
            print(f"[{result.get('id')}] {result.get('name')}")
        else:
            # Print 'No result' if the JSON is empty
            print("No result")
    except ValueError:
        # Print 'Not a valid JSON' if the JSON is invalid
        print("Not a valid JSON")
