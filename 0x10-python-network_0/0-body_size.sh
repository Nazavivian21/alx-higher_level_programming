#!/bin/bash
#Sends a request to a URL and displays the size of the body of the response.
if [ -z "$1" ]; then
  echo $0
  exit 1
fi

URL=$1

response_size=$(curl -s -o /dev/null -w '%{size_download}' "$URL")

echo $response_size
