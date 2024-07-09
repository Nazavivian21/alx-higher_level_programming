#!/bin/bash
# Make the request and display the response body
curl -sL -X PUT -H "Origin: Holbertonschool" -d "user_id=42" 0.0.0.0:5000/catch_me
