#! usr/bin/env python3

def main():

    ##create a dictionary
    switch = {'hostname': 'sw1',  'ip': '10.0.1.1', 'version': '1.2', 'vendor': 'cisco'}

    ## display parts of the dictionary
    print( switch['hostname'] )
    print( switch['ip'] )

    ##request a faKE key
    ##print( switch['lynx'] )
    
    ##request a 'fake key' with .get() method
    print( "First test - .get()")
    print( switch.get('lynx') )

    print( "Second test - .get()")
    print( switch.get('lynx', "the key is in another castle") )

    print( "Third test - .get()")
    print( switch.get('version') )



main()
