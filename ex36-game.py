choice = '> '
character = []
inventory = []

# LAIR OF THE DARK RABBIT TIKI GOD
# Freeing the buns:
# Doodle, Alfie, and Timmy
# Character Generation and Housekeeping

def start():
    print """
    Welcome to the Lair of the Dark Rabbit Tiki God.
    You will be exploring the lair and helping those who need your assistance.

    Your instructions are as follows:
    \tYou will encounter strange items, people, and creatures.
    \tYour choices will be highlighted by being entirely capitalized.
    \tYou must input the choice as it is typed.
    \tIf there are no choices, type 'yes' or 'no'.
    \tYou must remember that your choices do affect a real character
    \tand may result in their mortality.

    Do you understand?
    """

    enter_choice = raw_input(choice).upper()

    if 'YES' in enter_choice:
        character_generation()
    elif 'NO' in enter_choice:
        exit(0)


def character_generation():
    print "Good, now what is your name?"

    character_name = raw_input(choice)

    print "Thank you %s." % character_name
    print "That is your name, right?"
    character_confirm = raw_input(choice).upper()
    character.append(character_name)

    if 'YES' in character_confirm:
        front_door()
    else:
        character_generation()


#Game Rooms
def front_door():
    print "You awaken in a clearing."
    print "What appears to be a Polynesian home stretches out before you."
    print "You come upon a grey wooden door"
    print "with a tiki carved in the front of it."
    print "A small POND is to your right."
    print "Do you OPEN the door or LEAVE?"

    door_choice = raw_input(choice).upper()

    if 'POND' in door_choice:
        inventory.append('FROG')
        print "You found a frog. It has been added to your inventory."
        print "Now what do you do?"
        door_choice = raw_input(choice).upper()
    else:
        pass

    if 'OPEN' in door_choice:
        entryway()
    elif 'LEAVE' in door_choice:
        print "Thanks for playing!"
        exit(0)
    else:
        front_door()

def entryway():
    print "You enter a dark room with an ARCH to your right."
    print "In the arch, you hear the whirring of profane rituals"
    print "intended to reveal the future."
    print "Along the wall just ahead,"
    print "there is an ALTAR to the gods of the land."
    print "To your left, there is a TABLE surrounded by shelves"
    print "upon shelves of small armies, intended to bring success in war."
    print "Just ahead, you see a HALLWAY that leads into darkness."
    print "Where would you like to go?"

    door_choice = raw_input(choice).upper()

    if 'ARCH' in door_choice:
        print "The whirring that was heard upon entering gets louder."
        print "You see a wooden box glowing in the distance,"
        if 'DRUM' not in inventory:
            print "As an offering to the box, there is a small DRUM"
            print "in a circle on the floor."
        print "You inspect the room and find nothing else of consequence."
        print "Do you go BACK or do something else?"

        door_choice2 = raw_input(choice).upper()

        if 'DRUM' in door_choice2 and 'DRUM' not in inventory: # IDEA: make into function2
            inventory.append('DRUM')
            print "You found a drum. It has been added to your inventory."
            print "Now what do you do?"
            door_choice2 = raw_input(choice).upper()
        else:
            pass

        if 'BACK' in door_choice2:
            entryway()
        elif 'DRUM' in door_choice2 and 'DRUM' in inventory:
            print "You already have that."
            door_choice2 = raw_input(choice).upper()
        else:
            print "Thanks for playing"
            exit(0)

# Game Initiation

start()
