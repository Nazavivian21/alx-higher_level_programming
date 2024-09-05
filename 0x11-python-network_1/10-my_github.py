#!/usr/bin/python3
"""Takes GitHub credentials and uses the GitHub API to display your user ID."""
import requests
import sys

if __name__ == "__main__":
    # Get the username and personal access token from command line arguments
    username = sys.argv[1]
    token = sys.argv[2]

    # GitHub API URL for user information
    url = 'https://api.github.com/user'

    # Send a GET request with Basic Authentication using the username and token
    response = requests.get(url, auth=(username, token))

    try:
        # Attempt to parse the response as JSON
        user_info = response.json()

        # Display the user's GitHub ID
        print(user_info.get('id'))
    except ValueError:
        # If JSON parsing fails, print an error message
        print("Not a valid JSON")
