import yaml

def main():
    hitchhikers = [{"name": "Zaphod", "species": "bete"}, \
            {"name": "Arthur", "species": "human"}]

    print(hitchhikers)
	
yamlstring = yaml.dump(hitchhikers)

print(yamlstring)
    #zfile = open("galaxyguide.yaml", "w")

    #yaml.dump(hitchhikers, zfile)

    #zfile.close()

main()
