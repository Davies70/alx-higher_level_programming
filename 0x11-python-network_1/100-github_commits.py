#!/usr/bin/python3
""" Please list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
You must use the GitHub API, here is the documentation
https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)"""

import sys
import requests
if __name__ == '__main__':
    r = sys.argv[1]
    o = sys.argv[2]

    url = 'https://api.github.com/repos/' + o + '/' + r + '/commits'
    response = requests.get(url)
    api = response.json()
    try:
        for i in range(10):
            print('{}: {}'.format(
                  api[i].get('sha'),
                  api[i].get('commit').get('author').get('name')))
    except IndexError:
        pass
