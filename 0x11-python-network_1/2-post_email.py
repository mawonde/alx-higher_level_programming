#!/usr/bin/python3
"""
a script that takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter, and
displays the body of the response
"""


import urllib.request
import urllib.parse
import sys

# Check if both a URL and an email are provided as command-line arguments
if len(sys.argv) != 3:
    print("Usage: python script.py <URL> <email>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

# Prepare the data to be sent in the POST request
data = urllib.parse.urlencode({'email': email}).encode('utf-8')
headers = {'Content-Type': 'application/x-www-form-urlencoded'}

try:
    req = urllib.request.Request(url, data=data, headers=headers)
    with urllib.request.urlopen(req) as response:
        content = response.read().decode('utf-8')
        print(content)
except urllib.error.URLError as e:
    print("Error:", e)
