"""Room, Character, Enemy, Friend, Item for game wanderers"""


class Room:
    def __init__(self, name: str) -> None:
        self.name = name
        self.connected_rooms = []
        self.item = None
        self.character = None

    def set_description(self, description: str):
        self.description = description

    def get_details(self):
        print(self.name)
        print('--------------------')
        print(self.description)
        for info in self.connected_rooms:
            room = info[0]
            direction = info[1]
            print(f'The {room.name} is {direction}')

    def link_room(self, room: object, direction: str):
        self.connected_rooms.append((room, direction))

    def set_character(self, character: object):
        self.character = character

    def get_character(self) -> object:
        return self.character

    def set_item(self, item: object):
        self.item = item

    def get_item(self) -> object:
        return self.item

    def move(self, direction: str) -> object:
        for info in self.connected_rooms:
            room = info[0]
            room_direction = info[1]
            if room_direction == direction:
                return room
        print('There is no room is that direction.')
        return self


class Character:
    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

    def describe(self):
        print(f'{self.name} is here!')
        print(self.description)


class Enemy(Character):
    defeated = 0

    def set_conversation(self, conversation: str):
        self.conversation = conversation

    def set_weakness(self, weapon: str):
        self.weakness = weapon

    def talk(self):
        print(f'[{self.name} says]: {self.conversation}')

    def fight(self, weapon: str) -> bool:
        if weapon == self.weakness:
            Enemy.defeated += 1
            return True
        print(f'{self.name} crushes you, puny adventurer!')
        return False

    def get_defeated(self):
        return Enemy.defeated


class Item:
    def __init__(self, name) -> None:
        self.name = name

    def set_description(self, description: str) -> None:
        self.description = description

    def get_name(self) -> str:
        return self.name

    def describe(self):
        print(f'The [{self.name}] is here - {self.description}')
