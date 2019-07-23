#!/usr/bin/env/python3

"""Alta3 || Tracking ISS"""


import urllib.request

import json

MAJORTOM = 'http://api.open-notify.org/astros.json'

def main():

    groundctrl = urllib.request.urlopen(MAJORTOM)

    helmet = groundctrl.read()

    helmetson = json.loads(helmet.decode('utf-8'))

    print("\n\nConverted Python data")
    print(helmetson)

    print('\n\nPeople in Space: ', helmetson['number'])
    people = helmetson ['people']
    print(people)

main()

