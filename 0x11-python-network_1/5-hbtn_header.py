#!/usr/bin/python3
"""
This script receives a URL as input, sends a request to that URL, and then
shows the X-Request-Id value found in the response header.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    request_id = response.headers.get('X-Request-Id')
    if request_id:
        print(request_id)
