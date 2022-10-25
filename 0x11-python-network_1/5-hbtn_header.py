#!/usr/bin/python3
""" Write a Python script that takes in a URL,
sends a request to the URL and displays the value of the variable
X-Request-Id in the response header """

import requests
import sys

if __name__ == '__main__':
    r = requests.get(sys.argv[1])
    if r.headers['X-Request-Id'] is not None:
        print(r.headers['X-Request-Id'])
