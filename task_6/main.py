import game


kozelnytska = game.Street("Kozelnystska")
kozelnytska.set_description("")

stryiska = game.Street("Stryiska")
stryiska.set_description("")

franka = game.Street("Franka")
franka.set_description("")

shevckenka = game.Street("Shevckenka")
shevckenka.set_description("")

krakivska = game.Street("Krakivska")
krakivska.set_description("")

kozelnytska.link_room(stryiska, 'west')
stryiska.link_room(kozelnytska, 'east')
kozelnytska.link_room(franka, 'north')
franka.link_room(kozelnytska, 'south')
franka.link_room(stryiska, 'west')
stryiska.link_room(franka, 'north')
stryiska.link_room(shevckenka, 'west')
shevckenka.link_room(stryiska, 'east')
shevckenka.link_room(krakivska, 'north' )
krakivska.link_room(shevckenka, 'east')


dave = game.Enemy("Dave", "A smelly zombie")
dave.set_conversation("What's up, dude! I'm hungry.")
dave.set_weakness("cheese")
dining_hall.set_character(dave)

tabitha = game.Enemy("Tabitha", "An enormous spider with countless eyes and furry legs.")
tabitha.set_conversation("Sssss....I'm so bored...")
tabitha.set_weakness("book")
ballroom.set_character(tabitha)

cheese = game.Item("cheese")
cheese.set_description("A large and smelly block of cheese")
ballroom.set_item(cheese)

book = game.Item("book")
book.set_description("A really good book entitled 'Knitting for dummies'")
dining_hall.set_item(book)

current_room = kitchen
backpack = []

dead = False

while dead == False:

    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_room.get_item()
    if item is not None:
        item.describe()

    command = input("> ")

    if command in ["north", "south", "east", "west"]:
        # Move in the given direction
        current_room = current_room.move(command)
    elif command == "talk":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "fight":
        if inhabitant is not None:
            # Fight with the inhabitant, if there is one
            print("What will you fight with?")
            fight_with = input()

            # Do I have this item?
            if fight_with in backpack:

                if inhabitant.fight(fight_with) == True:
                    # What happens if you win?
                    print("Hooray, you won the fight!")
                    current_room.character = None
                    if inhabitant.get_defeated() == 2:
                        print("Congratulations, you have vanquished the enemy horde!")
                        dead = True
                else:
                    # What happens if you lose?
                    print("Oh dear, you lost the fight.")
                    print("That's the end of the game")
                    dead = True
            else:
                print("You don't have a " + fight_with)
        else:
            print("There is no one here to fight with")
    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your backpack")
            backpack.append(item.get_name())
            current_room.set_item(None)
        else:
            print("There's nothing here to take!")
    else:
        print("I don't know how to " + command)