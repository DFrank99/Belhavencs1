# There is a 1st floor (containing rooms 0-3) then a second floor (containing rooms 4-7)
import print

print("""
Waking up in cold sweat, you find yourself in front of an abandoned
estate. It looks very expensive and has many looming columns; two stories tall.
You have no memory of who you are, what day it is, or how you could have gotten here.
Soaking wet, confused, and wielding a piece of paper with the name 'Charles' on it...

I guess that must be my name...?

You are standing on stairs with a rusted mail box on the left.\n
""")

def main():

    room_list = []
    room = [0, 1, 2 , 3 , 4, 5, 6, 7]

    # OUTSIDE room 0
    room[0] = "Up the stairs there is a large,rotting wood door."

    # Going North into dining room room 1 on first floor
    room[1] = 1

    # South
    room[2] = None

    # East
    room[3] = None

    # West
    room[4] = None

    room_list.append(room)


    # DINING ROOM room 1
    room = [0, 1, 2, 3, 4, 5, 6, 7]

    room[0] = (" You take a key out of the rusted mail box and go north"
    " unlocking the door and going in. A dining room is dimmly lit; only the light is coming"
    "from the moonlight in the window. A vintage type lamp gives a little warm"
    "glow through the shade, giving you a better view."
    "It has a table and three chairs marked with age and cobwebs."
    "It looks to be abandoned for decades."
    "\tHow does it even have a working electricity?"
    "Farther down is a door that can barely be seen. To the left you"
    " can peer into another room.")

    # North (Kitchen room 2)
    room[1] = 2

    # South (Outside room 0)
    room[2] = None

    # East (Living room room 3)
    room[3] = 3

    # West
    room[4] = None

    room_list.append(room)


    # KITCHEN room 2
    room = [0, 1, 2, 3, 4, 5, 6, 7]

    room[0] = ("You walk into a kitchen...a kitchen with the light on, completely."
    "The yellow light bleeds into the darkness behind you as you walk forward."
    "The door creaks shut. To your surprise, it looks similar to the dining room;"
    "Cobwebs make ornate patterns on the dishware. The cabinets are murky and frail,"
    "Sink rusted overflowing with left over dishes festered with rotten food, leaving a musty smell."
    "\tA kitchen frozen in time as if awaiting it's homeowner's arrival.")

    # North
    room[1] = None

    # South (back to dining room room 1)
    room[2] = 1

    # East
    room[3] = None

    # West
    room[4] = None

    room_list.append(room)


    # LIVING ROOM room 3
    room = [0, 1, 2, 3, 4, 5, 6, 7]

    room[0] = ("You walk through into the living room. Old couch, retro television."
    "Nothing you wouldn't expect out of an old estate. The living room is far larger"
    " than that of the other rooms.Off in the corner stands a replica of knight's armor."
    " Inspecting it closer, you see it's warped like..."
    "\t...it was put under heat\nWhat is this estate? Why am I here, What does this all mean?"
    "\nBehind the couch, a dingy carpet with holes leads north up the stairs to the second floor.")

    # North (upstairs to room 4)
    room[1] = 4

    # South
    room[2] = None

    # East
    room[3] = None

    # West (back to dining room room 1)
    room[4] = 1

    room_list.append(room)


    # UPSTAIRS room 4
    room = [0, 1, 2, 3, 4, 5, 6, 7]

    room[0] = ("Up the stairs is a small area leading to the living quarters."
    "When you make it completely up the stairs there are two doors and one window."
    "One door is north, the other is west and the window to the east."
    "\tthere is one lone tree standing outside the window."
    "There is a tire swing swaying from the tree.\n Why is this familier? Why?"
    "Trying to bog your mind, you turn towards the doors.")

    # North (bedroom 2 room 5)
    room[1] = 5

    # South (back to living room room 3)
    room[2] = 3

    # East
    room[3] = None

    # West (bedroom 1 room 6)
    room[4] = 6

    room_list.append(room)


    # BEDROOM 2 room 5
    room = [0, 1, 2, 3, 4, 5, 6, 7]

    room[0] = ("On the door there is a drawing of a horse and flowers, surely drawn by a child."
    "\tYour heart flutters.\nOpening the door, you enter into a child's bedroom, highly preserved."
    "This room is nothing like the others. Plushes of horses "
    "and cowboy imagry covering every wall. On a wooden bed lies two stuffed cows."
    "\tI love it.\nThis looks like something I would have as a child."
    "This room would be a dream. A pair of cowboy boots sit under a chipping, "
    "painted mural of a horse mural.")

    # North
    room[1] = None

    # South (back to the main upstairs room 4)
    room[2] = 4

    # East
    room[3] = None

    # West
    room[4] = None

    room_list.append(room)


    # BEDROOM 1 room 6
    room = [0, 1, 2, 3, 4, 5, 6, 7]

    room[0] = ("Opening the door, you find a master bed drapped in vintage lace bedding."
    "There was a wardrobe, vanity, and a nightstand set atop a mangey, pink carpet."
    "To your right there is an open double door leading to the balcony veiled by beige curtains."
    "\tThere's a figure...human. Who is that?"
    "They could give you answers, about the estate, you, the situation?"
    "Why this place? Should you even persue?")

    # North (onto balcony room 7)
    room[1] = 7

    # South
    room[2] = None

    # East (back to upstairs room 4)
    room[3] = 4

    # West
    room[4] = None

    room_list.append(room)


    # BALCONY room 7
    room = [0, 1, 2, 3, 4, 5, 6, 7]

    room[0] = ("You walk through the curtains and there is a man leaning over the balcony."
    "\n'Hey, you. Why am I here? Who are you? What is this place'."
    "The man turns around and speaks; he is an older man wearing a button up with a cowboy hat on."
    "\t'Charles,my son, how are you. It's been years.'"
    "'After the fire, I tried preserving the home after they took you from me.'"
    "'This was the only way I could bring us back together. Mother would have been proud.'")

    # North
    room[1] = None

    # South
    room[2] = None

    # East
    room[3] = None

    # West
    room[4] = None

    room_list.append(room)


    current_room = 0
    next_room = 0

    #[room_list]
    #[current_room][0]

    #pprint.pprint(room_list) prints the text and list of rooms
    done = False

    while done == False:
        print("-----------------")
        print("Your adventure awaits")
        print("-----------------")

        print(room_list[current_room][0])
        print("\nWhere would you like to go?")
        print("\nYou have the choice of 'N' for North")
        print(" 'S' for south   'E'for East,")
        go = str(input(" 'W' for West, and Q to quit.---->"))
        go = go.strip()
        go = go.upper()

        # North
        if go.startswith('N'):
            next_room = room_list[current_room][1]
        # South
        elif go.startswith('S'):
            next_room = room_list[current_room][2]
        # East
        elif go.startswith('E'):
            next_room = room_list[current_room][3]
        # West
        elif go.startswith('W'):
            next_room = room_list[current_room][4]
            # Quit
        elif go.startswith('Q'):
            done = True
        else:
            print("I do not understand that answer.")
        if go in {"N","E","W","S"} and next_room is None:
            print("You can not go that way.")
        elif not done:
            current_room = next_room

if __name__=='__main__':
    main()
