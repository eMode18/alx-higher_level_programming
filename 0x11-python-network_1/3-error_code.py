#!/usr/bin/python3
"""
This script accepts a URL, sends a request to that URL, and depicts the body
of the response (in utf-8). It is in charge of urllib.error.Exceptions
from HTTPError.
"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]  # Fetch the URL from command line arguments
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read().decode('utf-8')
            print(content)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
