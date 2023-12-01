#!/usr/bin/python3
"""
A script that accepts a URL, sends a request to it, and reveals the outcome
of the X-Request-Id variable found in the response's header.
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]  # Fetch the URL from command line arguments
    with urllib.request.urlopen(url) as response:
        request_id = response.getheader('X-Request-Id')
        print(request_id)
