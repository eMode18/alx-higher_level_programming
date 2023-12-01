#!/usr/bin/python3
"""
A script that accepts a URL and an email, sends a POST request using the
email as a parameter to the URL, and conveys the content of the response
(decoded as utf-8).
"""

import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]  # Fetch the URL from command line arguments
    email = sys.argv[2]  # Fetch the email from command line arguments

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    req = urllib.request.Request(url, data=data, method='POST')

    with urllib.request.urlopen(req) as response:
        content = response.read().decode('utf-8')
        print("Your email is:", email)
        print(content)
