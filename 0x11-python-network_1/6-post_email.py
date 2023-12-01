#!/usr/bin/python3
"""
This script accepts a URL and an email address, performs a POST request to
the provided URL with the email as a parameter,
and then reveals the response body.
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    payload = {'email': email}
    response = requests.post(url, data=payload)
    print(response.text)
