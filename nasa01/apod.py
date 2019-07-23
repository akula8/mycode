#!/usr/bin/env python3

import urllib.request
import json
import webbrowser

apodurl = 'https://api.nasa.gov/planetary/apod?'
mykey = 'api_key=d9JCQLvJ0KhjjPjijiuxhhvleFBQNrKzkAKJj2xm'

apodurlobj = urllib.request.urlopen(apodurl + mykey)

apodread = apodurlobj.read()

decodeapod = json.loads(apodread.decode('utf-8'))

print("\n\nConverted python data")

print(decodeapod)

input('\nPress enter to open NASA picture of the day in FF')
webbrowser.open(decodeapod['url'])
