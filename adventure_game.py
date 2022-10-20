def main_game():
    import time
    import random

    def print_pause(text, delay=3):
        time.sleep(delay)
        print(text)

    names_list = ["John", "Orlando", "Adam", "Michal", "Ariel", "Dwight",
                  "Stanley", "Joy", "Tom", "Samuel", "Michael", "Richard"]

    def ask_name():
        ask_for_name = input("Write yes (y) or no (n)?\n")
        while ask_for_name != "y" and ask_for_name != "n":
            ask_for_name = input("Write yes (y) or no (n)?")
        else:
            if ask_for_name == "y":
                name_first = input("Write the first Pig's name?\n")
                name_second = input("Write the second Pig's name?\n")
                print(name_first.capitalize(), " was older Pig,",
                      name_second.capitalize(), " was younger Pig.")
            elif ask_for_name == "n":
                print_pause("No worries, you will find theirs name"
                            "in a moment...")
                name_first = random.choice(names_list)
                name_second = random.choice(names_list)
                print(name_first.capitalize(), " was older Pig, ",
                      name_second.capitalize(), " was younger Pig.")

    def who_build_house():
        while True:
            print_pause("Who started building a house first?")
            print_pause("What do you think?")
            print_pause("Chose:")
            print("1. Older Pig")
            print("2. Younger Pig")
            who_build_first = input("Hmm, 1 or 2\n")
            if who_build_first == '1':
                first_pig_start()
                break
            elif who_build_first == '2':
                second_pig_build_house()
                break

    def fist_pig_build_house_next_function():
        while True:
            first_pig_build_house_whats_next = input("Hmm, 1 or 2: \n")
            if first_pig_build_house_whats_next == '1':
                print_pause("And wolf came...")
                print_pause("But pig find solution how to build a wolf-proof"
                            "house.")
                print_pause("And this solution worked. Wolf couldn't huffed"
                            "and puffed the house.")
                print_pause("Is it the end?")
                print_pause("Of course is not!")
                print_pause("Or maybe it is?")
                print_pause("Who will decide?")
                who_decide_if_end()
            elif first_pig_build_house_whats_next == '2':
                print_pause("Because pig wasn't happy alone in his house, "
                            "went to his brother to help build a house.")
                second_pig_build_house()
                break

    def proces_of_receiving_permission():
        while True:
            permission_easy_or_not = input("y (yes) or n (no)")
            if permission_easy_or_not == 'y':
                permission_is_easy_to_receive()
                break
            elif permission_easy_or_not == 'n':
                print_pause("It's true")
                print_pause("When pig went to the office they as him about "
                            "project.")
                print_pause("He did not have a project so ask somebody to "
                            "prepare project.")
                print_pause("Even though it wasn't so easy, because he had to "
                            "ask couple of other specialist.")
                print_pause("But finally after few months pig receive "
                            "permission and start build the house.")
                break

    def permission_is_easy_to_receive():
        print_pause("It's not true")
        print_pause("When Pig went to the office they as him about project.")
        print_pause("He did not have a project so ask somebody to prepare "
                    "project.")
        print_pause("When finally Pig's project was ready, wasn't covered "
                    "requirements.")
        print_pause("So pig decided that it doesn't make a sens and rent an "
                    "apartment in block of flat.")
        print_pause("And was happily ever after :)")

    def wolf_come_and_ate_pig():
        print_pause("Unfortunately, Pig couldn't changed destiny.")
        print_pause("Wolf came and ate Pig")
        print_pause("The end")

    def does_pig_opened_door():
        while True:
            opened_or_not = input("Pig opened the door(y) or didn't open the "
                                  "door(n)\n")
            if opened_or_not == "y":
                wolf_come_and_ate_pig()
                break
            elif opened_or_not == "n":
                print_pause("Pig didn't open the door.")
                print_pause("Wolf decided that he tried too many times ate "
                            "pigs.")
                print_pause("It was time to decide to go for vegetarian diet!")
                print_pause("The end")
                break

    def second_pig_build_house():
        print_pause("Younger brother was very ambitious.")
        print_pause("When mother had said that Brothers must leave home...")
        time.sleep(3)
        print("Older Brother took his piggy-bank and went to Home Depot to "
              "buy some materials.")
        print_pause("Building a house wasn't so difficult, and it went pretty "
                    "fast.")
        print_pause("As we know second pig was very reliable and come up with "
                    "idea to build house from bricks.")
        print_pause("He wanted to start build house really fast.")
        print_pause("However as all investors know this is not easy to build "
                    "a house without permission")
        print_pause("What do you think, it was easy to receive permission?")
        proces_of_receiving_permission()
        print_pause("One day when the house was almost finished, somebody  "
                    "knocked the door....")
        print_pause("Of course we know who was it..")
        print_pause("...it was wolf")
        print_pause("So he knocked on the door and said:")
        print_pause("Little pigs! Little pig! Let me in! Let me in!")
        print_pause("What do you think, what pig did?")
        does_pig_opened_door()

    def who_decide_if_end():
        print_pause("Who will decide? You ore me?")
        while True:
            ask_if_the_end = input("player (p) or computer (c)")
            if ask_if_the_end == "c":
                first_pig_build_house_whats_next_episode()
                break
            elif ask_if_the_end == "p":
                print_pause("Ok what is yor idea, what is next?")
                the_end = input(":")
                print(the_end)
                print_pause("This is great idea! I like it, but the true was:")
                wolf_come_and_ate_pig()
                break

    def first_pig_build_house_whats_next_episode():
        from random import choice
        answer = choice(['yes', 'no'])
        print(answer)
        if answer == "yes":
            print_pause("I think this is the end, if you are "
                        "curious what is next you have to google it!")
        else:
            print_pause("So I think it's time to check what was "
                        "going on with the second pig...")
            second_pig_build_house()

    def first_pig_start():
        print_pause("Older Brother was very lazy and didn't want to "
                    "work at all. He built his house out of straw.")
        print_pause("Then, he sang and danced and played together "
                    "with friends for the rest of the day.")
        print_pause("In children's story he would live happyly ever "
                    "after but today...")
        print_pause("Oh wait a minute you play this game, so what "
                    "will be next: ")
        print_pause("1. Wolf will come...")
        print_pause("2. pig will have happy life")
        fist_pig_build_house_next_function()
    print_pause("Once upon a time there was an old Mother Pig who "
                "had two little Pigs.")
    print_pause("Theirs name were..., wait a moment maybe you "
                "know name of Pigs?")
    ask_name()
    print_pause("Mother did not have enough food to feed their children.")
    print_pause("So when they were old enough, she sent them out into "
                "the world to seek their fortunes.")
    print_pause("They thought that adult's life should "
                "start from building a house.")
    who_build_house()


main_game()
