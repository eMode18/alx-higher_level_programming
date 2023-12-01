#!/usr/bin/python3
"""
Uses GitHub API to display your user ID by authenticating
with a personal access token.
"""

import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    personal_token = sys.argv[2]

    url = f"https://api.github.com/user"
    response = requests.get(url, auth=(username, personal_token))
    if response.status_code == 200:
        user_data = response.json()
        print("Your GitHub user ID is:", user_data['id'])
    else:
        print("Failed to retrieve user ID. Status code:", response.status_code)
