from player import Player
from room import Room

# this is a python dictionary :
# A dictionary is a collection which =>
# unordered,
# changeable
# indexed.
# written with curly brackets,
# they have keys and values like JSON.

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# print('LINE 24', room)
# print(inspect.getmembers(Room('XY', 'ZZ')))
# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# print('LINE 37', room['treasure'].s_to)
#
# Main
#

# Make a new player object that is currently in the 'outside' room.
# player_name, current_room, room_name, room_description
new_player = Player('Joel', room['outside'], room['outside'], room['outside'])


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:

    # print('*** NEW PLAYER :', new_player)

    print('* new_player.room_description &*^ ', new_player.room_description)

    user_input = input(" *** Which way do you want to go ? *** ").lower()

    if user_input == 'n':
        print(new_player.current_room,)
    elif user_input == 's':
        print('A bear eats you')
    elif user_input == 'w':
        print('You slip on a bananna & are in a coma')
    elif user_input == 'e':
        print('You head east and fall plunge to your death in a hole.')
    elif user_input == "q":
        print('Until next time... ')
        break
    else:
        print("not valid input")


# while user_input != exit_game:

#     if user_input == 'north':
#         print(f'{new_player.name} heads north ')
#         break
#     elif user_input == 'south':
#         print(f'{new_player.name} heads south')
#     elif user_input == 'east':
#         print(f'{new_player.name} heads east')
#     elif user_input == 'west':
#         print(f'{new_player.name} heads west')
#     elif:
#         print('The game continues')
#         break
# else:
#     print('The game continues')
#     input('which way ? ')
