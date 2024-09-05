#!/usr/bin/python3
"""Prints all commits in the format: <sha>: <author name>."""
import requests
import sys

if __name__ == "__main__":
    # Get repository name and owner name from command line arguments
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    # GitHub API URL for fetching commits
    url = f'https://api.github.com/repos/{owner_name}/{repo_name}/commits'

    # Send a GET request to the GitHub API
    response = requests.get(url)

    # Parse the JSON response
    commits = response.json()

    # Loop through the first 10 commits
    for commit in commits[:10]:
        # Get the SHA and author name for each commit
        sha = commit.get('sha')
        author_name = commit.get('commit').get('author').get('name')

        # Print the commit information
        print(f"{sha}: {author_name}")
