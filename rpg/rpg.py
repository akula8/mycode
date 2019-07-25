#!/usr/bin/python3
'''My rpg game

def showInstructions():
    print('''
    RPG Game
    Commands:
        go [direction]
        get [item]
    ''')

def showStatus(): # display status
    print('===============')
    print('You are in the ', currentRoom)
    
    #show inventory
    print('Inventory : ', str(inventory))
    
    #show item if in the room
    
    if 'item' in room[currentRoom]:
        print('You see a ', rooms[currentRoom]['item'])

#init an empty list

inventory = []

rooms = {
        'Hall' : {
            'south' : "Kitchen',
            'item' : 'key'
            },
        'Kitchen' : {
            'north' : 'Hall'
            }
        }

# player start location
currentRoom = 'Hall'

# show instuctions to the player
showInstructions()

#create and infinite loop
while True:
    showStatus()
    move = ''
    while move == '':
        move = input('>') # so long as the move does not have a value
        #have a value. ask the user for inoput
   
   move = move.lower().split() #make everything lower case because dirctions adn items require it, then split into a list

    if move[0] == 'go':
        if move[1] in rooms[CurrentRoom]: 
            currentRoom = rooms[currentRoom][move[1]]
            # if YES that direction exists assign new current room to the value of the key the user entered

        else:
            print("You cant go that way!!!"

    if move[0] == 'get':
        if 'item' in rooms[currentRoom and move[1] in rooms[currentRoom]['items']:
            inventory += [move[1]] # add item to inventory list
            print(move[1] + 'got!') # print picked up item
            del rooms[currentRoom]['item'] # deletes item from dictionary

