"""Roguelike: Lviv version"""
import game


kozelnytska = game.Street("Козельницька")
kozelnytska.set_description("")

stryiska = game.Street("Стрийська")
stryiska.set_description("")

franka = game.Street("Франка")
franka.set_description("")

shevckenka = game.Street("Шевченка")
shevckenka.set_description("")

krakivska = game.Street("Краківська")
krakivska.set_description("")

kozelnytska.link_room(stryiska, 'захід')
stryiska.link_room(kozelnytska, 'схід')
kozelnytska.link_room(franka, 'північ')
franka.link_room(kozelnytska, 'південь')
franka.link_room(stryiska, 'захід')
stryiska.link_room(franka, 'північ')
stryiska.link_room(shevckenka, 'захід')
shevckenka.link_room(stryiska, 'схід')
shevckenka.link_room(krakivska, 'північ')
krakivska.link_room(shevckenka, 'південь')

wine = game.Weapon("пляшка вина")
wine.set_description("пляшка з-під вина з невідомою субстанцією всередині")
stryiska.set_item(wine)

sweater = game.Support("укушне худі")
sweater.set_description("худі, яке зігріє не тільки тіло, а й душу")

shocker = game.Weapon("шокер")
shocker.set_description("чудова річ для самозахисту і затримання злочинців")

broom = game.Weapon("віник")
broom.set_description("ним було підметено не одну вулицю")
franka.set_item(broom)

batyar = game.Enemy("Батяр", "Гульвіса, п'яничка")
batyar.set_conversation("Агов, де тут найближчий бар?")
batyar.set_weakness("пляшка вина")
franka.set_character(batyar)

student = game.Friend("Микола", "Студент УКУ, твій давній знайомий")
student.set_conversation(
    "Йоо, давно не бачились! Нарешті можу віддати тобі подарунок - укушне худі)")
student.set_present(sweater)
kozelnytska.set_character(student)

laydak = game.Friend("Лайдак", "Вбогий бездомний чоловік")
laydak.set_conversation("Як же ж холодно на вулиці...")
laydak.set_present(shocker)
shevckenka.set_character(laydak)

zbyi = game.Enemy(
    "Збуй", "Грабіжник, який на твоїх очах вкрав телефон у перехожого")
zbyi.set_conversation("Чого дивишся? Хочеш неприємностей?!")
zbyi.set_weakness("шокер")
krakivska.set_character(zbyi)


current_street = kozelnytska
backpack = {"support": [], "weapon": []}

dead = False

while dead == False:

    print("\n")
    current_street.get_details()

    inhabitant = current_street.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_street.get_item()
    if item is not None:
        item.describe()

    command = input("> ")

    if command in ["північ", "південь", "схід", "захід"]:
        # Move in the given direction
        current_street = current_street.move(command)
    elif command == "говорити":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()
            # Get present from your friend
            if inhabitant == student:
                student.get_present()
                backpack["support"].append(student.get_name_of_present())
                current_street.character = None

            # Help the laydak or ignore him
            if inhabitant == laydak:
                print(
                    "Хочеш подарувати укушне худі лайдаку і врятувати його від холоду?")
                response = input("так\ні: ")
                while response != "так" and response != "ні":
                    response = input("так\ні: ")
                if response == "так":
                    if sweater.get_name() in backpack["support"]:
                        backpack["support"].remove(sweater.get_name())
                        laydak.get_present()
                        backpack["weapon"].append(laydak.get_name_of_present())
                        current_street.character = None
                    else:
                        print("Упс, у тебе немає худі. Раджу навідатись до Миколи")
                else:
                    print(
                        "Це звісно твій вибір, але пам'ятай, що все повертається сторицею")

        else:
            print("Друже, ти говориш сам до себе...")
    elif command == "битись":
        if inhabitant is not None and isinstance(inhabitant, game.Enemy):
            # Fight with the inhabitant, if there is one
            print("Оберіть знаряддя для битви:")
            print(backpack["weapon"])
            fight_with = input()

            # Do I have this item?
            if fight_with in backpack["weapon"]:

                if inhabitant.fight(fight_with) == True:
                    # What happens if you win?
                    print("Єєєй, виграш битви за тобою!")
                    current_street.character = None
                    if inhabitant.get_defeated() == 2:
                        print(
                            "Вітаю! Завдяки тобі львівські вулички стали ще безпечнішими!")
                        dead = True
                else:
                    # What happens if you lose?
                    print("Кінець.")
                    dead = True
            else:
                print("У тебе немає " + fight_with)
        else:
            print("Спокійно, тут немає з ким битись.")
    elif command == "взяти":
        if item is not None:
            print(item.get_name() + " тепер в твоєму рюкзаку")
            if isinstance(item, game.Weapon):
                backpack["weapon"].append(item.get_name())
            else:
                backpack["support"].append(item.get_name())
            current_street.set_item(None)
        else:
            print("Брати чуже погано!")
    else:
        print(command + " - незрозуміла команда, спробуй ще раз")
