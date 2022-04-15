"""Room, Character, Enemy, Item for game wanderers"""


class Room:
    """Class Room"""
    def __init__(self, name: str) -> None:
        self.name = name
        self.connected_rooms = []
        self.item = None
        self.character = None

    def set_description(self, description: str):
        """
        Sets description to the room.
        """
        self.description = description

    def get_details(self):
        """
        Prints info about current room.
        """
        print(self.name)
        print('--------------------')
        print(self.description)
        for info in self.connected_rooms:
            room = info[0]
            direction = info[1]
            print(f'The {room.name} is {direction}')

    def link_room(self, room: object, direction: str):
        """
        Links one room to another.
        """
        self.connected_rooms.append((room, direction))

    def set_character(self, character: object):
        """
        Sets the character in the current room.
        """
        self.character = character

    def get_character(self) -> object:
        """
        Returns the character from the current room.
        """
        return self.character

    def set_item(self, item: object):
        """
        Sets the item in the current room.
        """
        self.item = item

    def get_item(self) -> object:
        """
        Returns the item from the current room.
        """
        return self.item

    def move(self, direction: str) -> object:
        """
        Moves to another room.
        If there is no room in that direction, stays in the current room.
        """
        for info in self.connected_rooms:
            room = info[0]
            room_direction = info[1]
            if room_direction == direction:
                return room
        print('There is no room is that direction.')
        return self


class Character:
    """Class Character"""
    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

    def describe(self):
        """
        Prints info about the character.
        """
        print(f'{self.name} is here!')
        print(self.description)


class Enemy(Character):
    """Class Enemy - child of class Character"""
    defeated = 0

    def set_conversation(self, conversation: str):
        """
        Sets conversation for the character.
        """
        self.conversation = conversation

    def set_weakness(self, weapon: str):
        """
        Sets weakness for the character.
        """
        self.weakness = weapon

    def talk(self):
        """
        Prints the conversations of the character.
        """
        print(f'[{self.name} says]: {self.conversation}')

    def fight(self, weapon: str) -> bool:
        """
        Returns the result of the fight.
        True: you won
        False: enemy won
        """
        if weapon == self.weakness:
            Enemy.defeated += 1
            return True
        print(f'{self.name} crushes you, puny adventurer!')
        return False

    def get_defeated(self):
        """
        Returns number of defeated enemys.
        """
        return Enemy.defeated


class Item:
    """Class Item"""
    def __init__(self, name) -> None:
        self.name = name

    def set_description(self, description: str) -> None:
        """
        Sets description for the item.
        """
        self.description = description

    def get_name(self) -> str:
        """
        Retruns the name of the item.
        """
        return self.name

    def describe(self):
        """
        Prints description of the item.
        """
        print(f'The [{self.name}] is here - {self.description}')
