# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room


class Player(Room):
    def __init__(self, player_name, current_room, room_name, room_description):
        super().__init__(room_name, room_description)
        self.player_name = player_name
        self.current_room = current_room

    def updateRoom(self, current_room):
        new_room = current_room
        return new_room
