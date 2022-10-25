#!/usr/bin/python3
""" Write a Python script that takes your
_ GitHub credentials (username and password)
_ and uses the GitHub API to display your id """

import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == '__main__':
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=HTTPBasicAuth(sys.argv[1], sys.argv[2]))
    print(response.json().get('id'))
