#!/usr/bin/env/python3

import yaml

def main():
    hitchhikers = [{"name": "Zaphod", "species": "bete"}, \
            {"name": "Arthur", "species": "human"}]

    print(hitchhikers)

    zfile = open("galaxyguide.yaml", "w")

    yaml.dump(hitchhikers, zfile)

    zfile.close()

main()


