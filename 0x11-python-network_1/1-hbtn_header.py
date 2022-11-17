#!/usr/bin/python3

"""
Write a Python script that takes in a URL,sends a request to the URL and
displays the value of the X-Request-Id variable
"""
from urllib.request import urlopen
import sys

if __name__ == '__main__':
    with urlopen(sys.argv[1]) as req:
        dic = dict(req.headers)
        print(dic.get('X-Request-Id'))
