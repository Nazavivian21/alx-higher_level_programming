#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL, and displays the body of the 
response decoded in utf-8."""
if __name__ == "__main__":
    import urllib.request
    import urllib.error
    import sys

    url = sys.argv[1]

    req = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(req) as response:
            # Decode response body
            body = response.read().decode('utf-8')
            # Print the response body
            print(body)
    except urllib.error.HTTPError as e:
        # Print the error code
        print(f"Error code: {e.code}")
