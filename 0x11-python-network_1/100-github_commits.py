#!/usr/bin/python3
""" Please list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
You must use the GitHub API, here is the documentation
https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)"""

import sys
import requests
if __name__ == '__main__':
    o = sys.argv[1]
    r = sys.argv[2]

    headers = {'accept': 'application/vnd.github+json', 'owner': o, 'repo': r}
    url = 'https://api.github.com/repos/' + o + '/' + r + '/commits'
    response = requests.get(url, headers=headers)
    api = response.json()
    i = len(api) - 1
    j = 10
    while (i and j > 0):
        print('{}: {}'.format(api[i].get('sha'),
                              api[i].get('commit').get('author').get('name')))
        i -= 1
        j -= 1
