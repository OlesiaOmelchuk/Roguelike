"""Street, Character, Enemy, Friend, Item"""


class Street:
    """Class Street"""

    def __init__(self, name: str) -> None:
        self.name = name
        self.connected_rooms = []
        self.item = None
        self.character = None

    def set_description(self, description: str) -> None:
        """
        Sets description to the room.
        """
        self.description = description

    def get_details(self) -> None:
        """
        Prints info about current room.
        """
        print(self.name)
        print('--------------------')
        print(self.description)
        for info in self.connected_rooms:
            room = info[0]
            direction = info[1]
            print(f'Вулиця {room.name} - {direction}')

    def link_room(self, room: object, direction: str) -> None:
        """
        Links one room to another.
        """
        self.connected_rooms.append((room, direction))

    def set_character(self, character: object) -> None:
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
        print('Тупік. Обери інший напрямок.')
        return self


class Character:
    """Class Character"""

    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

    def describe(self) -> None:
        """
        Prints info about the character.
        """
        print(f'Тут {self.name}!')
        print(self.description)

    def set_conversation(self, conversation: str) -> None:
        """
        Sets conversation for the character.
        """
        self.conversation = conversation

    def talk(self) -> None:
        """
        Prints the conversations of the character.
        """
        print(f'[{self.name} каже]: {self.conversation}')


class Enemy(Character):
    """Class Enemy - child of class Character"""
    defeated = 0

    def set_weakness(self, weapon: str) -> None:
        """
        Sets weakness for the character.
        """
        self.weakness = weapon

    def fight(self, weapon: str) -> bool:
        """
        Returns the result of the fight.
        True: you won
        False: enemy won
        """
        if weapon == self.weakness:
            Enemy.defeated += 1
            return True
        print(f'{self.name} розтер вас в порошок :(')
        return False

    def get_defeated(self) -> int:
        """
        Returns number of defeated enemys.
        """
        return Enemy.defeated


class Friend(Character):
    """Class Friend - child of class Character"""

    def set_present(self, present: object):
        self.present = present

    def get_name_of_present(self) -> str:
        """
        Returns name of the present.
        """
        return self.present.name

    def get_description_of_present(self) -> str:
        """
        Retrns description of the present.
        """
        return self.present.description

    def get_present(self) -> None:
        """
        Get the present from friend.
        """
        print(f"{self.name} подарував тобі {self.get_name_of_present()} - {self.get_description_of_present()}")
        print(f"{self.get_name_of_present()} тепер в твоєму рюкзаку")


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

    def describe(self) -> None:
        """
        Prints description of the item.
        """
        print(f'Тут є [{self.name}] - {self.description}')


class Weapon(Item):
    """
    Class Weapon - child of class Item.
    """
    pass


class Support(Item):
    """
    Class Support - child of class Item.
    """
    pass
