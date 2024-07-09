#!/bin/bash
# Make the request and display the response body
curl -sL -X PUT -d "user_id=42" -H "Origin: School" 0.0.0.0:5000/catch_me
