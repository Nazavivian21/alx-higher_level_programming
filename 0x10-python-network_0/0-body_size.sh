#!/bin/bash
#Sends a request to a URL and displays the size of the body of the response.
response_size=$(curl -s -o /dev/null -w '%{size_download}' "$1")
echo "The size of the body of the response is $response_size bytes"