#!/usr/bin/python3
""" Write a Python script that fetches https://alx-intranet.hbtn.io/status

You must use the package urllib
You are not allowed to import any packages other than urllib
The body of the response must be displayed \
        like the following example (tabulation before -)
You must use a with statement """

from urllib.request import Request, urlopen

url = 'https://alx-intranet.hbtn.io/status'
with urlopen(url) as r:
    body = r.read()
print('Body response:')
print('    - type: {}'.format(type(body)))
print('    - content: {}'.format(body))
print('    - utf8 content: {}'.format(body.decode()))
