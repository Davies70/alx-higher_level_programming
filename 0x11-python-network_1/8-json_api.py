#!/usr/bin/python3
""" Write a Python script that takes in a letter
and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter. """

import requests
import sys

if __name__ == '__main__':
    dic = {}
    if len(sys.argv) == 1:
        dic['q'] = ""
    else:
        dic['q'] = sys.argv[1]
    r = requests.post('http://0.0.0.0:5000/search_user', data=dic)
    try:
        data = r.json()
    except JSONDecodeError:
        print('Not a valid JSON')
        exit()
    data = r.json()
    if len(data) == 0:
        print('No result')
    else:
        print('[{}] {}'.format(data.get('id'), data.get('name')))
