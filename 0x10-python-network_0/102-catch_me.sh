#!/bin/bash
# Make the request and display the response body
curl -sL -X PUT -H  "Origin: Holberton School" -d "user_id=98" 0.0.0.0:5000/catch_me
