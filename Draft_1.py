from time import sleep
import nltk


def setting():
    global item_box
    item_box = []
    global clue, ceil_light1,candon,crystal_wall,rope_yes
    clue=[0,0,0,0,0]
    ceil_light1=[0,0]
    candon=[0]
    crystal_wall=[0]
    rope_yes=[0]
    global main_room_sight, cabinet_sight, basement_sight, garret_sight, dining_table  # first layer
    main_room_sight = [[], ["tv set", "cabinet", "bug"], ["curtain", "sash"], ["case", "cabinet", "switch", "bug"],
                       ["front door", "bug", "rug"], ["garret door", "ceiling light"]]
    #cabinet_sight = [[], ["drawer", '1', '2', '3', '4', 'photo'], [], ["phone", "drawer", '1', '2', '3'], [], []]
    #case_sight = [[], [], ["case", "phone"], [], [], []]
    dining_table = ["There's nothing on it..."]
    garret_sight = ['', "the red wall with a little hole.","the blue wall with a little hole.","the yellow wall with a little hole.","the crystal wall with three key holes."]
    global cabinet_1_o, cabinet_1_item, cabinet_1, cabinet_3_item, cabinet_3,  ceil_light_item  # second layer
    cabinet_1_o = [0, 1, 1, 1, 0]
    cabinet_1_item = ["", "cylinder", "photo piece", "matches", ""]
    cabinet_1 = ["", "was a cylinder", "was one photo piece", "were some matches", "a NOTE: CALL 377624"]
    cabinet_3 = ["", "was a newspaper", "was a treasure map", "was a knife"]
    cabinet_3_item= ["", "newspaper", "treasure map", "knife"]
    dining_table = ["Nothing's on it, empty..."]
    global case_3, case_3_o,peep_hole, front_door, rug
    peep_hole = [0]
    front_door = [2]
    case_3 = ["cylinder", "diary", "key"]
    rug=[0,0,0]
    case_3_o = [0]
    global wall_nums_new, wall_nums_general  # zero layer
    wall_nums_new = {1: """I am now facing the wall with a TV set and a cabinet.A small red bug is on the wall.
The TV is in the middle with the cabinet on the right...
The cabinet is painted yellow... This seemed familiar.""",
                     2: "I am now facing the opened curtain and a sash.",
                     3: """I am now facing the wall with a light switch, small case and a cabinet. A small green bug is on the wall.
The light switch is of reachable height on the wall... 
The small wooden case is on the left and the cabinet, greenish and perhaps slightly grey, is on the right.""",
                     4: """I am now facing the front door. A small white bug is beside the door. 
There's a welcoming rug on the floor saying:'WELCOME !'"""}
    wall_nums_general = {1: "I am now facing the wall with a TV set and a cabinet.A small red bug is on the wall.",
                         2: "I am now facing the opened curtain and a sash.",
                         3: "I am now facing the wall with a light switch, small case and a cabinet. A small green bug is on the wall.",
                         4: "I am now facing the front door. A small white bug is beside the door. On the floor is a welcoming rug."
                         }

# setting up--------------------------------------------------------------------------------------------------------------------------------------------------

def morning_scene():
    print("I felt dizzy...")
    sleep(0.8)
    print("My head seemed to be spinning...")
    sleep(0.8)
    print("I slowly sit up to find myself inside a dim room. A ray of light seemed to be shining in as I looked up.")
    print("Is it sunlight...")
    sleep(0.8)
    print("In front of me is a closed curtain, which is slightly open so light can escape inside.")
    sleep(0.8)
    print("... Perhaps I should open the curtain up completely...")
    sleep(0.5)

def morning_end():
    wall_nums_general[1] = "I am now facing the wall with a TV set and a cabinet."
    wall_nums_general[3] = "I am now facing the wall with a light switch, small case and a cabinet."
    wall_nums_general[4] = "I am now facing the front door. The welcoming rug on the floor seemed crumpled."
    for l in main_room_sight:
        if 'bug' in l:
            l.remove('bug')
    cabinet_1_o[4] = 1
    cabinet_1[4] = "Nothing's is there..."
    print("It suddenly seemed heavy...")
    sleep(0.8)
    print("My head feels heavy too...")
    sleep(0.8)
    print("conscious seems to be leaving me...")
    sleep(0.8)
    print("...")
    sleep(0.8)
    print("...")
    sleep(0.8)
    if 'cake box' in item_box: item_box.remove("cake box")


def afternoon_scene(num):
    print("I struggled to open my eyes...")
    sleep(0.8)
    print("The scene seemed to have slightly change...")
    sleep(0.8)
    print("The front door... Is it a welcoming rug?")
    sleep(0.8)
    print("It was afternoon now...")
    sleep(0.8)
    dining_table[0] = "There was a birthday cake."
    print(wall_nums_general[num])


def afternoon_end():
    print("The candles were slowly burning on the cake, casting a warm glow.")
    print("I suddenly felt sleepy as a flames danced elegantly on the cake.")
    sleep(0.8)
    print("...")
    sleep(0.8)
    print("...My eyelids felt heavy...")
    sleep(0.8)
    print("...")
    sleep(0.8)
    print("...I felt conscious leaving me...")
    sleep(0.8)
    print("...")
    sleep(0.5)
    print("...")
    sleep(0.5)
    print("...")
    sleep(0.5)
    return

def evening_st(face):
    print("Yawn...")
    sleep(0.5)
    print("...")
    sleep(0.8)
    print("How long did I sleep...")
    sleep(0.8)
    print("I slowly opened up my eyes...")
    sleep(0.8)
    print("Emmf...")
    sleep(0.8)
    print("Oh... a steel key was lying in my hand...")
    sleep(0.5)
    print("Better put that in the item box...")
    pick_up("steel key")
    sleep(0.5)
    print("...")
    sleep(0.8)
    print("I stood up and looked around.")
    print("Things seemed to be different in the room...")
    sleep(0.8)
    print("The curtain was closed...is it night perhaps...?")
    sleep(0.5)
    print("The dinning table was filled with uncooked raw food...")
    sleep(0.5)
    print("Are they materials for dinner?")
    sleep(0.5)
    print("I turn towards the front door...")
    sleep(0.5)
    print("Hum... the rug was removed...and...")
    sleep(0.5)
    print("I think what's revealed is a basement door...")
    main_room_sight[4].remove('rug')
    main_room_sight[3].remove('switch')
    wall_nums_general[2]= "The curtain was closed."
    ceil_light1[0]=1
    cabinet_3[1] = "was nothing"
    cabinet_3[2] = "was nothing"
    cabinet_3_item[1]=""
    cabinet_3_item[2]=""
    wall_nums_general[3]="I am now facing the wall with a  small case and a cabinet."
    wall_nums_general[4]= "I am now facing the front door. On the floor is a basement door."
    main_room_sight[4].append("basement door")
    cabinet_1[4] = "was nothing"
    dining_table = ["There were some raw seafood and vegetables needing dissections and cleaning."]
    print(f"I think {wall_nums_general[face]}")
    return


# Fixed scene--------------------------------------------------------------------------------------------------------------------

def pan_y_or_n(a):
    a = a.lower()
    while (a != 'y') & (a != 'n'):
        if a=="help": check_help(a)
        elif a=="quit": check_quit(a)
        elif a == "check the item box":
            print(','.join(item_box))
        elif a == "go back":
            return "go back"
        else:
            print("Sorry, invalid input!")
        a = input("> ")
        a = a.lower()
    return a


# Deciding move valid-----------------------------------------------------------------------------------------------------------------------------------------------------------

def check_help(move):
    if move != 'help':
        return
    choice = input("""What instructions do you want to see? (items/movements/all)
> """)
    while 1:
        fl = 0
        check_quit(choice.lower())
        if choice.lower()=='quit':
            choice = input("> ")
            continue
        if (choice.lower() == 'items') | (choice.lower() == 'all'):
            instructions_on_items()
            fl = 1
        if (choice.lower() == 'movements') | (choice.lower() == 'all'):
            instructions_on_movements()
            fl = 1
        if fl == 0:
            print("Beg your Pardon?")
            choice = input("> ")
            continue
        elif fl == 1:
            break
    print("Time to continue playing!")
    return

# Help------------------------------------------------------------------------------------------------------------------Help
def check_quit(move):
    if move == 'quit':
        print("Are you sure? This game cannot be saved. (Y/N)")
        choice = input("> ")
        choice = pan_y_or_n(choice)
        if choice.lower() == 'y':
            print("Good luck next time!")
            sleep(0.5)
            print("Quiting...", end='')
            sleep(0.5)
            exit(0)
        else:
            print("The game continues...")
            sleep(0.3)
        return
    else:
        return


# Quit-------------------------------------------------------------------------------------------------------------------Quit
def check_vb(move):
    move = move.split()
    tag = nltk.pos_tag(move)
    ans = 0
    for tup in tag:
        if "VB" in tup: ans += 1
    if ans == 0:
        print("There's no verb in sentence.")
        print(f"Detected part of speech: {tag}.")
        print("Hint: When a verb failed to be detected,")
        print("try to add a adjective, pronoun, or article before the noun after it.")
        print("      Also, check if the grammar is correct.")
        return 0
    if ans == 1:
        return 1
    if ans > 1:
        print("Whoa, I can only do one thing at a time.")
        print("There are multiple verbs in sentence.")
        print(f"Detected part of speech: {tag}.")
        print("Hint: When something shouldn't be a verb is detected,")
        print("try to add a adjective, pronoun, or article before the noun.")
        print("      Also, check if the grammar is correct.")
        return 2
# vb------------------------------------------------------------------------------------------------------------------------vb

def check_noun(move):
    move = move.split()
    tag = nltk.pos_tag(move)
    ans = 0
    for tup in tag:
        if "NN" or "NNS" in tup: ans += 1
    if ans == 0:
        print("Where or what...?")
        print(f"Detected part of speech: {tag}.")
        print("Hint: When a noun failed to be detected,")
        print("try to add or remove an adjective, pronoun, or article before it.")
        print("      Also, check if the grammar is correct.")
        return 0
    elif ans == 1:
        return 1
    elif ans > 1:
        if 'and' not in move : return 1
        print("Whoa, I can only do one thing at a time.")
        print("There are multiple nouns in sentence.")
        print(f"Detected part of speech: {tag}.")
        print("Hint:When multiple nouns detected, avoid nouns about general locations.(e.g. wall)")
        print("      Also, check if the grammar is correct")
        return 2
#noun-----------------------------------------------------------


def instructions_on_items():
    print("Instructions about items coming up...")
    sleep(0.8)
    print("""To put an item in your item box, please input: pick item up
To use the item, please input: take item in hand
To have a view of what's in your item box, please input: check the item box
""")
    sleep(0.5)
    choice = input("""Do you need an example? (Y/N)
> """)
    choice = pan_y_or_n(choice)
    if choice.lower() == 'y':
        print("Example coming up...")
        sleep(0.8)
        print("""> pick up key
Key is in your item box
> take key in hand
What do you want to do with the key?
> open lock
Lock is open
""")
    sleep(0.5)


def instructions_on_movements():
    print("Instructions about movements coming up...")
    sleep(0.8)
    print("""To face different sides of the inside of the house, please input: turn left/turn right/ turn around
To check the ceiling, please input: look up
To approach a place or item, please input: go to place/item
To leave a place or item, please input: go back
""")
    sleep(0.5)
    choice = input("""Do you need an example? (Y/N)
> """)
    choice = pan_y_or_n(choice)
    if choice.lower() == 'y':
        print("Example coming up...")
        sleep(0.8)
        print("""> Turn left
Turning... You are now facing the window.(you will get a brief description)
>go to the window
Moving... It is locked.(you will get a detailed description)
>go back
Moving... You backed away from the window.
""")
    sleep(0.5)


def welcome_pack():
    print("""****************************************************
******------Welcome to this escape game!------******
****************************************************""")
    sleep(0.5)
    choice = input("""When you see'> ', you can insert your move or your answer to the question above!
Please keep in mind that to move you must insert at least a verb and a noun.
Also, note that all numbers entered should be arabic numerals.
Need more brief instructions? (N/Y)
> """)
    choice = pan_y_or_n(choice)
    if choice.lower() == 'y':
        print("""Instructions coming up...""")
        sleep(0.5)
        instructions_on_items()
        instructions_on_movements()
    print("If you want to see the instructions again, just insert: help")
    print("If you want to quit, just insert: quit")
    print("Please note that all input are space sensitive.")
    print("However, all inputs are not case sensitive, no worries!")
    print("ps. You might be needing a pen and paper to briefly take down notes!")
    check = input("""Ready to start? (Y/N)
> """)
    check = pan_y_or_n(check)
    while check.lower() == 'n':
        print("Alright, take your time to think when it's asked again.")
        check = input("""Ready to start? (Y/N)
> """)
        check = pan_y_or_n(check)
        sleep(0.5)
        continue
    print("""Good luck and have fun!""")
    print("Loading", end='')
    sleep(0.2)
    print("...")
    sleep(0.2)
    print("Loading", end='')
    sleep(0.2)
    print("...")
    sleep(0.8)
    print()
    print()

# Welcome------------------------------------------------------------------------------------------------------------------

def pick_up(item):
    print(f"Putting {item} in item box...")
    sleep(0.5)
    if item not in item_box:
        item_box.append(item)
    return


def use_item(hand,item):
    print("Searching...")
    sleep(0.5)
    if hand == item:
        print("I already have it or them in my hands.")
    else:
        if item not in item_box:
            print("No luck! I have found nothing.")
        else:
            print(f"I have taken out the {item} from my item box.I have {item} in my hands now.")
            hand = item
    return hand

#fixed moves----------------------------------------------------------------------------------------------

def photo(hand, num, total):
    print("I examined the photo slowly...")
    sleep(0.5)
    if num < 3:
        print("The photo was not complete.")
        sleep(0.5)
        print("Can I do something about it? Perhaps putting some pieces back...(Y/N)")
        choice = input("> ")
        choice = pan_y_or_n(choice)
        if choice == 'n':
            print("I stopped staring at the incomplete photo and looked elsewhere.")
            return hand, num, total, 0
        else:
            if total == 0:
                print("Urr...")
                sleep(0.5)
                print("I don't think I've got any... Perhaps I should come back later.")
                return hand, num, total, 0
            else:
                while hand != "photo piece":
                    print("I think I'd better take it out first.")
                    choice = input("> ")
                    choice = choice.lower()
                    check_help(choice)
                    check_quit(choice)
                    num_vb = check_vb(choice)
                    if num_vb != 1: continue
                    num_noun = check_noun(choice)
                    if num_noun !=1: continue
                    elif ("take" in choice) & ("in hand" in choice):
                        tag = nltk.pos_tag(choice.split())
                        tmp = []
                        for tup in tag:
                            if (("NN" in tup)|("NNS" in tup)) & ("hand" not in tup)&("hands" not in tup): tmp.append(tup[0])
                        if len(tmp) == 0:
                            print("I need to choose something to take.")
                            print(f"Detected part of speech: {tag}.")
                            print("Hint: When a noun failed to be detected,")
                            print("try to add a adjective, pronoun, or article before it.")
                            print("      Also, check if the grammar is correct.")
                        elif len(tmp) > 2:
                            print("I can only hold one item at a time.")
                            print(f"Detected part of speech: {tag}.")
                            print("Hint: When an unexpected noun is detected,")
                            print("try to reduce nouns about general locations(eg. walls).")
                            print("      Also, check if the grammar is correct.")
                        else:
                            tmp = ' '.join(tmp)
                            hand=use_item(hand, tmp)
                    elif choice == "check the item box":
                        print(','.join(item_box))
                    elif choice == "go back":
                        print("I stopped examine the incomplete photo.")
                        return hand, num, total, 0
                    else:
                        print("I wasn't doing things logically...")
                        sleep(0.5)
                print("How many photo pieces do I want to put back...let's say...")
                while 1:
                    move = input("> ")
                    move = move.lower()
                    check_help(move)
                    check_quit(move)
                    num_vb = check_vb(move)
                    if num_vb != 1:
                        if ("put" in move)&("back" in move):
                            print("Perhaps try using the form 'put back...photo piece(s)'.")
                        continue
                    num_noun = check_noun(move)
                    if num_noun != 1: continue
                    if ("take" in move) & ("in hand" in move) & ("photo pieces" in move):
                        print("Searching...")
                        sleep(0.5)
                        print("Photo pieces are in my hands now.")
                    if ("take" in move) & ("in hand" in move):
                        tag = nltk.pos_tag(move.split())
                        tmp = []
                        for tup in tag:
                            if (("NN" in tup)|("NNS" in tup)) & ("hand" not in tup)&("hands" not in tup): tmp.append(tup[0])
                        if len(tmp) == 0:
                            print("I need to choose something to take.")
                            print(f"Detected part of speech: {tag}.")
                            print("Hint: When a noun failed to be detected,")
                            print("try to add a adjective, pronoun, or article before it.")
                            print("      Also, check if the grammar is correct.")
                        elif len(tmp) > 2:
                            print("I can only hold one item at a time.")
                            print(f"Detected part of speech: {tag}.")
                            print("Hint: When an unexpected noun is detected,")
                            print("try to reduce nouns about general locations(eg. walls).")
                            print("      Also, check if the grammar is correct.")
                        else:
                            tmp = ' '.join(tmp)
                            hand=use_item(hand, tmp)
                        continue
                    elif move == "go back":
                        print("Never mind, I'll come back again later.")
                        sleep(0.5)
                        return hand, num, total, 0
                    elif move == 'check the item box':
                        print(','.join(item_box))
                    else:
                        tag = nltk.pos_tag(move.split())
                        number = []
                        for tup in tag:
                            if 'CD' in tup:
                                number.append(tup[0])
                        if ('negative' in move) | ('-' in move):
                            print("... ...I must be out of my mind.")
                            continue
                        if len(number) == 0:
                            print("How many?")
                        elif len(number) >= 2:
                            print("Oops, I can only do one number at a time...")
                        else:
                            if not number[0].isdecimal():
                                print("Please use arabic numerals.")
                            else:
                                a = int(number[0])
                                if a > total:
                                    print("I haven't got that much... Perhaps I'll start with a smaller amount.")
                                else:
                                    print(f"{a} photo piece(s) was mended on the broken photo.")
                                    total -= a
                                    if total==0:
                                        item_box.remove("photo piece")
                                    num += a
                                    if num == 3:
                                        break
                                    else:
                                        print("I think more photo pieces are needed...")
                                        print("Am I going to continue mending? (Y/N)")
                                        choice = input("> ")
                                        choice = pan_y_or_n(choice)
                                        if (choice == 'n') | (choice == 'go back'):
                                            print("I will com back when more can be put on...")
                                            return hand, num, total, 0
    if num == 3:
        print("Alright... I think that's the last of them...")
        sleep(0.8)
        print("In front of me was a complete photo of a little girl in her princess gown. Kinda cute...")
        print("Small letters seemed to be written on it.")
        sleep(0.8)
        print("Turn...")
        sleep(0.8)
        print("it over...")
        while 1:
            move = input("> ")
            move = move.lower()
            check_help(move)
            check_quit(move)
            num_vb = check_vb(move)
            if num_vb != 1: continue
            num_noun = check_noun(move)
            if num_noun != 1: continue
            if move == "check the item box":
                print(','.join(item_box))
            elif ("take" in move) & ("in hand" in move):
                tag = nltk.pos_tag(move.split())
                tmp = []
                for tup in tag:
                    if (("NN" in tup)|("NNS" in tup)) & ("hand" not in tup)&("hands" not in tup): tmp.append(tup[0])
                if len(tmp) == 0:
                    print("I need to choose something to take.")
                    print(f"Detected part of speech: {tag}.")
                    print("Hint: When a noun failed to be detected,")
                    print("try to add a adjective, pronoun, or article before it.")
                    print("      Also, check if the grammar is correct.")
                elif len(tmp) > 2:
                    print("I can only hold one item at a time.")
                    print(f"Detected part of speech: {tag}.")
                    print("Hint: When an unexpected noun is detected,")
                    print("try to reduce nouns about general locations(eg. walls).")
                    print("      Also, check if the grammar is correct.")
                else:
                    tmp = ' '.join(tmp)
                    hand=use_item(hand, tmp)
            elif move == "go back":
                print("The clue is right before my eyes... Am I sure about this? (Y/N)")
                choice = input("> ")
                choice = pan_y_or_n(choice)
                if choice == 'n':
                    continue
                else:
                    print("I left from the completed photo reluctantly.")
                    return hand, 5, 0, 0
            elif move == "turn the photo over":
                print("I cautiously turned the photo over, afraid it may end up broken again.")
                print("On the back of it I found a small wooden key.")
                print("The moment I put it in the item box, light stated to fade")
                morning_end()
                return hand, 4, 0, 1
            elif move == "turn it over":
                print("I think I need to specify 'it'.")
            else:
                print("...?")
    if num == 4:
        print("This photo is complete.")
        return hand, 4, 0, 0
    elif num == 5:
        print("In front of me was a complete photo of a little girl in her princess gown. Kinda cute...")
        print("Small letters seemed to be written on it.")
        sleep(0.8)
        print("Turn...")
        sleep(0.8)
        print("it over...")
        while 1:
            move = input("> ")
            move = move.lower()
            check_help(move)
            check_quit(move)
            num_vb = check_vb(move)
            if num_vb != 1: continue
            num_noun = check_noun(move)
            if num_noun != 1: continue
            if move == "check the item box":
                print(','.join(item_box))
            elif ("take" in move) & ("in hand" in move):
                tag = nltk.pos_tag(move.split())
                tmp = []
                for tup in tag:
                    if (("NN" in tup)|("NNS" in tup)) & ("hand" not in tup)&("hands" not in tup): tmp.append(tup[0])
                if len(tmp) == 0:
                    print("I need to choose something to take.")
                    print(f"Detected part of speech: {tag}.")
                    print("Hint: When a noun failed to be detected,")
                    print("try to add a adjective, pronoun, or article before it.")
                    print("      Also, check if the grammar is correct.")
                elif len(tmp) > 2:
                    print("I can only hold one item at a time.")
                    print(f"Detected part of speech: {tag}.")
                    print("Hint: When an unexpected noun is detected,")
                    print("try to reduce nouns about general locations(eg. walls).")
                    print("      Also, check if the grammar is correct.")
                else:
                    tmp = ' '.join(tmp)
                    hand=use_item(hand, tmp)
            elif move == "go back":
                print("The clue is right before my eyes... Am I sure about this? (Y/N)")
                choice = input("> ")
                choice = pan_y_or_n(choice)
                if choice == 'n':
                    continue
                else:
                    print("I left from the completed photo reluctantly.")
                    return hand, 5, 0, 0
            elif move == "turn the photo over":
                print("I cautiously turned the photo over, afraid it may end up broken again.")
                print("On the back of it I found a small wooden key.")
                print("The moment I put it in the item box, light stated to fade")
                morning_end()
                return hand, 4, 0, 1
            elif move == "turn it over":
                print("I think I need to specify 'it'.")


def drawers1(hand, photo_piece, cylinder_num):
    print("I think I can try to open them by dragging.")
    ite = 0
    fl = 0
    while 1:
        move = input("> ")
        move = move.lower()
        check_help(move)
        check_quit(move)
        num_vb = check_vb(move)
        if num_vb == 0:
            if "dragging" in move:
                print("Please use the verb form.")
            continue
        if num_vb == 2: continue
        num_noun = check_noun(move)
        if num_noun != 1: continue
        if move == "check the item box":
            print(','.join(item_box))
            continue
        elif ("take" in move) & ("in hand" in move):
            tag = nltk.pos_tag(move.split())
            tmp = []
            for tup in tag:
                if (("NN" in tup)|("NNS" in tup)) & ("hand" not in tup)&("hands" not in tup): tmp.append(tup[0])
            if len(tmp) == 0:
                print("I need to choose something to take.")
                print(f"Detected part of speech: {tag}.")
                print("Hint: When a noun failed to be detected,")
                print("try to add a adjective, pronoun, or article before it.")
                print("      Also, check if the grammar is correct.")
            elif len(tmp) > 2:
                print("I can only hold one item at a time.")
                print(f"Detected part of speech: {tag}.")
                print("Hint: When an unexpected noun is detected,")
                print("try to reduce nouns about general locations(eg. walls).")
                print("      Also, check if the grammar is correct.")
            else:
                tmp = ' '.join(tmp)
                hand=use_item(hand, tmp)
            continue
        elif move == "go back":
            if (fl == 1)&(ite!=4):
                print(f"I think I'd better pick up the {cabinet_1_item[ite]} in drawer {ite} first.")
                continue
            else:
                print("I stretched a bit and stood up.")
            return hand, photo_piece, cylinder_num
        elif 'pick up' in move:
            if fl == 0:
                print("No open drawers.")
            elif fl == 1:
                if cabinet_1_item[ite] in move:
                    pick_up(cabinet_1_item[ite])
                    cabinet_1[ite] = "was nothing"
                    if cabinet_1_item[ite] == "photo piece":
                        photo_piece += 1
                    if cabinet_1_item[ite] == "cylinder":
                        cylinder_num+=1
                    print("I slowly closed the drawer.")
                    ite = 0
                    fl = 0
                else:
                    print("I can't pick up something that's not in sight...")
            continue
        # ---special cases
        if ("drawers" not in move) and ("drawer" not in move):
            print("...")
            sleep(0.4)
            print("I can't tell what my mind wants me to do.")
            continue
        if ('throw' in move)|('crush' in move)|('smash' in move) | ('break' in move) | ('tear' in move) | ('eat' in move) | ('nock' in move):
            print("...")
            sleep(0.4)
            print("I must be out of mind... I need to regain my thoughts.")
            continue
        if "drag" in move:
            if fl==1:
                tag = nltk.pos_tag(move.split())
                tmp = []
                for tup in tag:
                    if "CD" in tup:
                        tmp.append(tup[0])
                if (len(tmp)==1):
                    if (tmp[0].isdecimal())&(int(tmp[0])==a):
                        print("It's already opened.")
                        continue
                print("I can't do that for now... I'll Need to close the drawer first.")
                print("But I think I'd better pick up what's inside the drawer before closing it...")
                choice = input("> ")
                if "pick up" not in choice:
                    print("Alright, I'll check this drawer again later...")
                    print(f"I closed drawer {ite}.")
                    print("Now, I can retake the move.")
                    fl = 0
                    ite = 0
                else:
                    if cabinet_1_item[ite] in choice:
                        pick_up(cabinet_1_item[ite])
                        cabinet_1[ite] = "was nothing"
                        if cabinet_1_item[ite] == "photo piece":
                            photo_piece += 1
                        if cabinet_1_item[ite] == "cylinder":
                            cylinder_num += 1
                        print(f"I slowly closed drawer {ite}.")
                        ite = 0
                        fl = 0
                    else:
                        print("I can't pick up something that's not in sight...")
            else:
                move = move.split()
                tag = nltk.pos_tag(move)
                tmp = []
                for tup in tag:
                    if "CD" in tup:
                        tmp.append(tup[0])
                fl = 0
                if len(tmp) == 0:
                    print("There are four drawers but which to open?")
                    ite = 0
                elif len(tmp) > 1:
                    print("Whoa, one at a time.")
                else:
                    tag = nltk.pos_tag(move)
                    number = []
                    for tup in tag:
                        if 'CD' in tup:
                            number.append(tup[0])
                    if ('negative' in move) | ('-' in move):
                        print("... ...I must be out of my mind.")
                        continue
                    if len(number) == 0:
                        print("Beg your pardon?")
                    elif len(number) >= 2:
                        print("Oh...Urr... I can only open one drawer at a time.")
                    elif not (''.join(number)).isdecimal():
                        print("Please use arabic numerals.")
                        continue
                    else:
                        a = int(number[0])
                        if (a < 1) or (a > 4):
                            print("Let me check again... The four drawers are numbered from 1 to 4.")
                            continue
                        if cabinet_1_o[a] == 1:
                            print("Opened.")
                            print(f"There {cabinet_1[a]} in sight.")
                            if (cabinet_1[a] != "was nothing")&(a!=4):
                                ite = a
                                fl = 1
                            else:
                                print("I closed the drawer.")
                                continue
                        else:
                            print("It's locked...")
                            print("I think it needs a code to open...")
                            sleep(0.5)
                            print("Let's see...")
                            sleep(0.5)
                            print("Red... White... Green... Yellow...")
                            sleep(0.8)
                            print("There's also another small line of writing...")
                            sleep(0.5)
                            print("Let's see...")
                            print("Circle-1, Triangle-2, Wavy line-3, Star-4, Square-5...")
                            print("Straight Line-6, Cross-7, Rectangle-8, Dot-9.")
                            while 1:
                                print("Do I want to try open the drawer 4? (Y/N)")
                                choice = input("> ")
                                choice=pan_y_or_n(choice)
                                if choice=='n':
                                    print("Alright, I'll give up opening the drawer 4 for now.")
                                    break
                                else:
                                    print("Ok... I'll try to insert the correct code...")
                                code=input("> ")
                                if not code.isdecimal():
                                    print("Please insert only arabic numerals.")
                                else:
                                    if code != '1968':
                                        print("Wrong code!")
                                    else:
                                        cabinet_1_o[4] = 1
                                        print("With a clicking sound, the drawer slowly opened.")
                                        print(f"Inside it was {cabinet_1[4]}.")
                                        print("I closed drawer 4")
                                        break
        else:
            print("I think I need to drag if I want to open the drawers.")
    return hand, photo_piece, cylinder_num


def cabinet1(hand, already_mend, photo_piece, cylinder_num, face, time):
    print("Can I still remember this cabinet well? (Y/N)")
    choice = input("> ")
    choice = choice.lower()
    choice = pan_y_or_n(choice)
    if choice == 'n':
        print("There was a photo on top of it. Are there pieces missing?")
        if already_mend==0:
            sleep(0.5)
            print("One...")
            sleep(0.5)
            print("Two...")
            sleep(0.5)
            print("Three...")
            sleep(0.5)
        elif already_mend==1:
            sleep(0.5)
            print("One...")
            sleep(0.5)
            print("Two...")
            sleep(0.5)
        elif already_mend==2:
            sleep(0.5)
            print("One...")
            sleep(0.5)
        print("After counting, I studied th cabinet carefully.")
        print("There are four drawers numbered 1 to 4. Perhaps one can try to drag them.")
    while 1:
        move = input("> ")
        move = move.lower()
        check_help(move)
        check_quit(move)
        num_vb = check_vb(move)
        if num_vb != 1: continue
        num_noun = check_noun(move)
        if num_noun != 1: continue
        if ("take" in move) & ("in hand" in move):
            tag = nltk.pos_tag(move.split())
            tmp = []
            for tup in tag:
                if (("NN" in tup)|("NNS" in tup)) & ("hand" not in tup)&("hands" not in tup): tmp.append(tup[0])
            if len(tmp) == 0:
                print("I need to choose something to take.")
                print(f"Detected part of speech: {tag}.")
                print("Hint: When a noun failed to be detected,")
                print("try to add a adjective, pronoun, or article before it.")
                print("      Also, check if the grammar is correct.")
            elif len(tmp) > 2:
                print("I can only hold one item at a time.")
                print(f"Detected part of speech: {tag}.")
                print("Hint: When an unexpected noun is detected,")
                print("try to reduce nouns about general locations(eg. walls).")
                print("      Also, check if the grammar is correct.")
            else:
                tmp = ' '.join(tmp)
                hand=use_item(hand, tmp)
        elif move == "go back":
            print("I left the cabinet.")
            return hand, already_mend, photo_piece, cylinder_num, time
        elif move == "check the item box":
            print(','.join(item_box))
        else:
            if 'cabinet' in move:
                if "pick up" in move:
                    print("... It's way to large and heavy.")
                elif "go to" in move:
                    print("I am already here.")
            elif 'photo' in move:
                if "pick up" in move:
                    print("I cannot fit it in my item box.")
                elif "go to" in move:
                    print("I moved my head closer to the photo to take a better look.")
                    hand, already_mend, photo_piece, detect = photo(hand, already_mend, photo_piece)
                    if detect == 1:
                        time=2
                        afternoon_scene(face)
                        return hand, already_mend, photo_piece, cylinder_num, time
                elif ('throw' in move)|('crush' in move)|('smash' in move) | ('break' in move) | ('tear' in move) | ('eat' in move) | ('nock' in move):
                    print("...")
                    sleep(0.4)
                    print("I must be out of mind... I need to regain my thoughts.")
                else:
                    print("I might need to get a bit closer to the photo to do that.")
            elif 'drawer' in move:
                if "pick up" in move:
                    print("It's too heavy to pick up... And it cannot fit in my item box either.")
                elif 'go to' in move:
                    print("I slowly bent down to reach the drawers.")
                    hand, photo_piece, cylinder_num = drawers1(hand, photo_piece, cylinder_num)
                elif ('throw' in move)|('crush' in move)|('smash' in move) | ('break' in move) | ('tear' in move) | ('eat' in move) | ('nock' in move):
                    print("...")
                    sleep(0.4)
                    print("I must be out of mind... I need to regain my thoughts.")
                else:
                    print("I might need to get a bit closer to the drawers to do that.")
            else:
                tmp = []
                tag = nltk.pos_tag(move.split())
                for tup in tag:
                    if ("NN" == tup[1])|("NNS" == tup[1]): tmp.append(tup[0])
                if len(tmp) == 0:
                    print("invalid input!")
                    print(f"Detected part of speech: {tag}.")
                    print("Hint: When a noun failed to be detected,")
                    print("try to add a adjective, pronoun, or article before it.")
                    print("      Also, check if the grammar is correct.")
                elif len(tmp) > 2:
                    print("Whoa, one at a time.")
                    print(f"Detected part of speech: {tag}.")
                    print("Hint: When an unexpected noun is detected,")
                    print("try to reduce nouns about general locations(eg. walls).")
                    print("      Also, check if the grammar is correct.")
                else:
                    print(f"No {' '.join(tmp)} in sight...")
    return hand, already_mend, photo_piece, cylinder_num, time


def drawers3(hand):
    print("I think I can try to open them by dragging.")
    ite = 0
    fl = 0
    while 1:
        move = input("> ")
        move = move.lower()
        check_help(move)
        check_quit(move)
        num_vb = check_vb(move)
        if num_vb == 0:
            if "dragging" in move:
                print("Please use the verb form.")
            continue
        if num_vb == 2: continue
        num_noun = check_noun(move)
        if num_noun != 1: continue
        if move == "check the item box":
            print(','.join(item_box))
            continue
        elif ("take" in move) & ("in hand" in move):
            tag = nltk.pos_tag(move.split())
            tmp = []
            for tup in tag:
                if (("NN" in tup)|("NNS" in tup)) & ("hand" not in tup)&("hands" not in tup): tmp.append(tup[0])
            if len(tmp) == 0:
                print("I need to choose something to take.")
                print(f"Detected part of speech: {tag}.")
                print("Hint: When a noun failed to be detected,")
                print("try to add a adjective, pronoun, or article before it.")
                print("      Also, check if the grammar is correct.")
            elif len(tmp) > 2:
                print("I can only hold one item at a time.")
                print(f"Detected part of speech: {tag}.")
                print("Hint: When an unexpected noun is detected,")
                print("try to reduce nouns about general locations(eg. walls).")
                print("      Also, check if the grammar is correct.")
            else:
                tmp = ' '.join(tmp)
                hand=use_item(hand, tmp)
            continue
        elif move == "go back":
            if (fl == 1)&(ite==3):
                print(f"I think I'd better pick up the {cabinet_3_item[ite]} in drawer {ite} first.")
                continue
            else:
                print("I stretched a bit and stood up.")
            return hand
        elif ('throw' in move)|('crush' in move)|('smash' in move) | ('break' in move) | ('tear' in move) | ('eat' in move) | ('nock' in move):
            print("...")
            sleep(0.4)
            print("I must be out of mind... I need to regain my thoughts.")
            continue
        elif 'pick up' in move:
            if fl == 0:
                print("No open drawers.")
            elif fl == 1:
                if cabinet_3_item[ite] in move:
                    if ite == 1:
                        print("Cough...Cough...")
                        sleep(0.4)
                        print("It's too dusty... I can't pick it up.")
                        while 1:
                            print("I think I need to memorize that...")
                            print("Done memorizing? (N/Y)")
                            choice=input("> ")
                            choice = pan_y_or_n(choice)
                            if choice=='n':
                                print("Oh... I think I'll need more time to read it again.")
                                print("A car crash took place on Green Street...")
                                print("A famous writer...rushed to ICU...")
                                print("Leaving his five-year old daughter and wife...")
                                print("Daily News.\n2012.5.17")
                            elif choice=='y':
                                print("Alright! Time for my next move.")
                                break
                    elif ite == 2:
                        print("Oh, Urr...")
                        print("I think it's too fragile to be picked up.")
                        while 1:
                            print("I think I need to memorize that...")
                            print("Done memorizing? (N/Y)")
                            choice=input("> ")
                            choice = pan_y_or_n(choice)
                            if choice=='n':
                                print("Oh... I think I'll need more time to memorize.")
                                print("     x")
                                print("     |__")
                                print("        |")
                                print(" ____   |")
                                print("|    |__|")
                                print("|")
                                print("NOTE: one '|' indicates one move, while two '_'s indicates one move.")
                            elif choice=='y':
                                print("Alright! Time for my next move.")
                                break
                    else:
                        pick_up(cabinet_3_item[ite])
                        cabinet_3[ite] = "was nothing"
                    print("I slowly closed the drawer.")
                    ite = 0
                    fl = 0
                else:
                    print("I can't pick up something that's not in sight...")
            continue
        # ---special cases
        if ("drawers" not in move) and ("drawer" not in move):
            print("...")
            sleep(0.4)
            print("I can't tell what my mind wants me to do.")
            continue
        if "drag" in move:
            tag = nltk.pos_tag(move.split())
            tmp = []
            for tup in tag:
                if "CD" in tup:
                        tmp.append(tup[0])
            if (fl==1):
                if len(tmp)==1:
                    if(tmp[0].isdecimal())&(int(tmp[0])==a):
                        print("It's already opened.")
                        continue
            if (fl==1)&(ite==3):
                print("I can't do that for now... I'll Need to close the drawer first.")
                print("But I think I'd better pick up what's inside the drawer before closing it...")
                choice = input("> ")
                if "pick up" not in choice:
                    print("Alright, I'll check this drawer again later...")
                    print(f"I closed drawer {ite}.")
                    print("Now, I can retake the move.")
                    fl = 0
                    ite = 0
                else:
                    if cabinet_3_item[ite] in choice:
                        pick_up(cabinet_3_item[ite])
                        cabinet_3[ite] = "was nothing"
                        print(f"I slowly closed drawer {ite}.")
                        ite = 0
                        fl = 0
                    else:
                        print("I can't pick up something that's not in sight...")
            elif (fl==1)&((ite==2)|(ite==1)):
                print("I can't do that for now... I'll Need to close the drawer first.")
                while 1:
                    print(f"Am I done memorizing the {cabinet_3_item[ite]}? (N/Y)")
                    choice=input("> ")
                    choice = pan_y_or_n(choice)
                    if choice=='n':
                        if ite==2:
                            print("Oh... I think I'll need more time to memorize.")
                            print("     x")
                            print("     |__")
                            print("        |")
                            print(" ____   |")
                            print("|    |__|")
                            print("|")
                            print("NOTE: one '|' indicates one move, while two '_'s indicates one move.")
                        elif ite==1:
                            print("Oh... I think I'll need more time to read it again.")
                            print("A car crash took place on Green Street...")
                            print("A famous writer...rushed to ICU...")
                            print("Leaving his five-year old daughter and wife...")
                            print("Daily News.\n2012.5.17")
                    elif choice=='y':
                        print("Done! Now I can close the drawer then retake the move.")
                        fl=0
                        ite=0
                        break
            else:
                move = move.split()
                tag = nltk.pos_tag(move)
                tmp = []
                for tup in tag:
                    if "CD" in tup:
                        tmp.append(tup[0])
                fl = 0
                if len(tmp) == 0:
                    print("There are three drawers but which to open?")
                    ite = 0
                elif len(tmp) > 1:
                    print("Whoa, one at a time.")
                else:
                    tag = nltk.pos_tag(move)
                    number = []
                    for tup in tag:
                        if 'CD' in tup:
                            number.append(tup[0])
                    if ('negative' in move) | ('-' in move):
                        print("... ...I must be out of my mind.")
                        continue
                    if len(number) == 0:
                        print("Beg your pardon?")
                    elif len(number) >= 2:
                        print("Oh...Urr... I can only open one drawer at a time.")
                    elif not (''.join(number)).isdecimal():
                        print("Please use arabic numerals.")
                        continue
                    else:
                        a = int(number[0])
                        if (a < 1) or (a > 3):
                            print("Let me check again... The three drawers are numbered from 1 to 3.")
                            continue
                        print("Opened.")
                        print(f"There {cabinet_3[a]} in sight.")
                        if a==1:
                            print("The newspaper was titled white with black background...")
                            print("I took interest in it and read it.")
                            print("...")
                            sleep(0.8)
                            print("A car crash took place on Green Street...")
                            print("Urr...")
                            sleep(0.8)
                            print("A famous writer...rushed to ICU...")
                            print("And... umm...")
                            sleep(0.8)
                            print("Leaving his five-year old daughter and wife...")
                            print("Daily News.\n2012.1.17")
                            sleep(0.8)
                            print("It seemed familiar... ")
                            sleep(0.8)
                            print("... January... is it four months ago...?")
                            sleep(0.8)
                            print("But why can't I remember this...")
                        elif a==2:
                            print("     x")
                            print("     |__")
                            print("        |")
                            print(" ____   |")
                            print("|    |__|")
                            print("|")
                            print("NOTE: one '|' indicates one move, while two '_'s indicates one move.")
                        if cabinet_3[a] != "was nothing":
                            ite = a
                            fl = 1
                        else:
                            print("I closed the drawer.")
                            continue
        else:
            print("I think I need to drag if I want to open the drawers.")
    return hand

def cabinet3(hand):
    print("Can I still remember this cabinet well? (Y/N)")
    choice = input("> ")
    choice = choice.lower()
    choice = pan_y_or_n(choice)
    if choice == 'n':
        print("I studied the cabinet carefully...")
        sleep(0.5)
        print("I spotted a small yellow bug on it's top...")
        print("There are three drawers numbered 1 to 3. Perhaps I can try to drag them.")
    while 1:
        move = input("> ")
        move = move.lower()
        check_help(move)
        check_quit(move)
        num_vb = check_vb(move)
        num_noun = check_noun(move)
        if num_noun != 1: continue
        if num_vb != 1: continue
        if ("take" in move) & ("in hand" in move):
            tag = nltk.pos_tag(move.split())
            tmp = []
            for tup in tag:
                if (("NN" in tup)|("NNS" in tup)) & ("hand" not in tup)&("hands" not in tup): tmp.append(tup[0])
            if len(tmp) == 0:
                print("I need to choose something to take.")
                print(f"Detected part of speech: {tag}.")
                print("Hint: When a noun failed to be detected,")
                print("try to add a adjective, pronoun, or article before it.")
                print("      Also, check if the grammar is correct.")
            elif len(tmp) > 2:
                print("I can only hold one item at a time.")
                print(f"Detected part of speech: {tag}.")
                print("Hint: When an unexpected noun is detected,")
                print("try to reduce nouns about general locations(eg. walls).")
                print("      Also, check if the grammar is correct.")
            else:
                tmp = ' '.join(tmp)
                hand=use_item(hand, tmp)
        elif move == "go back":
            print("I left the cabinet.")
            return hand
        elif move == "check the item box":
            print(','.join(item_box))
        else:
            if 'cabinet' in move:
                if "pick up" in move:
                    print("... It's way to large and heavy.")
                elif "go to" in move:
                    print("I am already here.")
            elif 'bug' in move:
                if "go to" in move:
                    che = 0
                    tag=nltk.pos_tag(move.split())
                    for tup in tag:
                        if "JJ" in tup: che+=1
                    if che == 0:
                        print("...The yellow one?")
                    elif che>=2:
                        print("I believe there's only one bug in sight...")
                    else:
                        if "yellow" in move: bugs("yellow")
                elif ('throw' in move)|('crush' in move)|('smash' in move) | ('break' in move) | ('tear' in move) | ('eat' in move) | ('nock' in move):
                    print("Urr... It seemed that I can't touch it.")
                    clue[0]=1
                else:
                    print("... I don't think I want to do that...")
            elif ('drawers' in move)|('drawer' in move):
                if "pick up" in move:
                    print("It's too heavy to pick up... And it cannot fit in my item box either.")
                elif 'go to' in move:
                    print("I slowly bent down to reach the drawers.")
                    hand = drawers3(hand)
                elif ('smash' in move) | ('break' in move) | ('tear' in move) | ('eat' in move) | ('nock' in move):
                    print("...")
                    sleep(0.4)
                    print("I must be out of mind... I need to regain my thoughts.")
                else:
                    print("I might need to get a bit closer to the drawers to do that.")
            else:
                tmp = []
                tag = nltk.pos_tag(move.split())
                for tup in tag:
                    if ("NNS" == tup[1])|("NN" == tup[1]): tmp.append(tup[0])
                if len(tmp) == 0:
                    print("invalid input!")
                    print(f"Detected part of speech: {tag}.")
                    print("Hint: When a noun failed to be detected,")
                    print("try to add a adjective, pronoun, or article before it.")
                    print("      Also, check if the grammar is correct.")
                elif len(tmp) > 2:
                    print("Whoa, one at a time.")
                    print(f"Detected part of speech: {tag}.")
                    print("Hint: When an unexpected noun is detected,")
                    print("try to reduce nouns about general locations(eg. walls).")
                    print("      Also, check if the grammar is correct.")
                else:
                    print(f"No {' '.join(tmp)} in sight...")


def case(hand, cylinder_num,time):
    fl = 0
    print("I think I can try to open the case by pulling its handle.")
    while 1:
        move = input("> ")
        move = move.lower()
        check_help(move)
        check_quit(move)
        num_vb = check_vb(move)
        if num_vb == 0:
            if "pulling" in move:
                print("Please use the verb form.")
            continue
        if num_vb == 2: continue
        num_noun = check_noun(move)
        if num_noun != 1: continue
        if move == "check the item box":
            print(','.join(item_box))
            continue
        elif ("take" in move) & ("in hand" in move):
            tag = nltk.pos_tag(move.split())
            tmp = []
            for tup in tag:
                 if (("NN" in tup) | ("NNS" in tup)) & ("hand" not in tup)&("hands" not in tup): tmp.append(tup[0])
            if len(tmp) == 0:
                print("I need to choose something to take.")
                print(f"Detected part of speech: {tag}.")
                print("Hint: When a noun failed to be detected,")
                print("try to add a adjective, pronoun, or article before it.")
                print("      Also, check if the grammar is correct.")
            elif len(tmp) > 2:
                print("I can only hold one item at a time.")
                print(f"Detected part of speech: {tag}.")
                print("Hint: When an unexpected noun is detected,")
                print("try to reduce nouns about general locations(eg. walls).")
                print("      Also, check if the grammar is correct.")
            else:
                tmp = ' '.join(tmp)
                hand = use_item(hand, tmp)
            continue
        elif move == "go back":
            if fl == 1:
                print("Am I done checking things in the case? (Y/N)")
                choice = input("> ")
                choice = pan_y_or_n(choice)
                if choice=='y':
                    print("Alright... I think I can close it now...")
                    print("Squeak...")
                    sleep(0.5)
                    print('I closed the case.')
                    fl=0
                    case_3_o[0]=0
                    print("Now, do I want to stand up? (Y/N)")
                    choic = input("> ")
                    choic = pan_y_or_n(choic)
                    if choic=='y':
                        print("I stretched a bit and stood up.")
                        return hand,cylinder_num
                    else:
                        print("Ok... I'll keep on studying it...")
                        continue
                elif choice == 'n':
                    print("I think I'll keep checking...")
                    sleep(0.4)
                    print("The wooden case opened with a squeaky tone...")
                    print("Inside it was ",end='')
                    num = 0
                    if 'key' in case_3:
                        print("a key",end='')
                        num += 1
                    if 'cylinder' in case_3:
                        if num == 1: print(", ",end='')
                        print("a cylinder",end='')
                        num += 1
                    if num == 1:
                        print(" and ",end='')
                    elif num == 2:
                        print(", and ",end='')
                    print("a diary.")
                    sleep(0.5)
                    print("...")
                    sleep(0.5)
                    print("The diary was turned to a page... do I want to read it? (Y/N)")
                    choi=input("> ")
                    choi=pan_y_or_n(choi)
                    if choi=='n': continue
                    print("On the page it read: ")
                    print("""Monday, January 16th
Dear diary,
It is going to be my 5th birthday soon! Alright it's still about four months away, but I am excited anyways!
Though daddy's busy, he promised to come home with a cake and play his traditional treasure hunt with me! Happy! 
FYI: Mom's fish soup rocks! And I overheard that she's going to make that for my birthday! ! !""")
                    continue
            print("I stood up and shut the case's door or remained it shut.")
            return hand, cylinder_num
        elif ('throw' in move) | ('crush' in move) | ('smash' in move) | ('break' in move) | ('tear' in move) | ('eat' in move) | ('nock' in move):
            print("...")
            sleep(0.4)
            print("I must be out of mind... I need to regain my thoughts.")
            continue
        elif ("open" in move) | ("drag" in move) | ("unlock" in move):
            print("I need to pull the handle to open the case.")
        elif "go to" in move:
            if "case" in move:
                print("I am already here...")
            else:
                print("I can go no closer to anything.")
        elif 'pull' in move:
            if 'handle' not in move:
                print("The only thing in sight that I could pull is the door handle...")
                continue
            if case_3_o[0]==1:
                print("Case already opened.")
                continue
            print("Crack...")
            sleep(0.5)
            print("Crack...")
            sleep(0.5)
            print("It's locked...")
            print("Wait... There's something small written on it...")
            sleep(0.5)
            print("Urr...")
            sleep(0.5)
            times=-1
            while 1:
                fn=0
                times+=1
                if times > 0:
                    while 1:
                        print("Do I want to take another turn or stop? (take another turn/stop)")
                        choice = input("> ")
                        choice = choice.lower()
                        if "stop" in choice:
                            print("I stopped trying to open the case.")
                            fn=1
                            break
                        elif choice == "take another turn":
                            print("OK...")
                            break
                        else:
                            print("...? Beg your pardon?")
                            continue
                if fn==1: break
                print("Hint: Date (YYYY/MM/DD).")
                code = input("> ")
                if not code.isdecimal():
                    print("The date needs to be composed of all arabic numerals.")
                    print("Perhaps I can leave out the slashes and blanks next time.")
                else:
                    if code == '20120117':
                        fl = 1
                        case_3_o[0]=1
                        print("The wooden case opened with a squeaky tone...")
                        print("Inside it was ",end='')
                        num = 0
                        if 'key' in case_3:
                            print("a key",end='')
                            num += 1
                        if 'cylinder' in case_3:
                            if num == 1: print(", ",end='')
                            print("a cylinder",end='')
                            num += 1
                        if num == 1:
                            print(" and ",end='')
                        elif num == 2:
                            print(", and ",end='')
                        print("a diary.")
                        sleep(0.5)
                        print("...")
                        sleep(0.5)
                        print("The diary was turned to a page... do I want to read it? (Y/N)")
                        choi=input("> ")
                        choi=pan_y_or_n(choi)
                        if choi=='n': break
                        print("On the page it read: ")
                        print("""Monday, January 16th
Dear diary,
It is going to be my 5th birthday soon! Alright it's still about four months away, but I am excited anyways!
Though daddy's busy, he promised to come home with a cake and play his traditional treasure hunt with me! Happy! 
FYI: Mom's fish soup rocks! And I overheard that she's going to make that for my birthday! ! !""")
                        break
                    elif code == '20120517':
                        case_3_o[0]=1
                        if (clue[2] == 2)|(time!=2):
                            print("The door wouldn't budge... Perhaps I entered the wrong code.")
                            continue
                        print("The case is empty...")
                        print("Is it indicating that I should lay down something...?")
                        while 1:
                            print("Do I want to lay down anything? (Y/N)")
                            choice = input("> ")
                            choice = pan_y_or_n(choice)
                            if choice == 'n':
                                print("Alright... I might be mistaken...")
                                print("I closed the case.")
                                case_3_o[0]=0
                                break
                            else:
                                print("Ok... What to do next?")
                                while 1:
                                    ft=0
                                    ite = input("> ")
                                    ite = ite.lower()
                                    if ("place" in ite)|("put" in ite):
                                        print("...Perhaps the verb I was looking for should be 'lay'?")
                                        continue
                                    check_help(ite)
                                    check_quit(ite)
                                    num_vb = check_vb(ite)
                                    if num_vb == 0: continue
                                    if num_vb == 2: continue
                                    num_noun = check_noun(ite)
                                    if num_noun != 1: continue
                                    if ite == "check the item box":
                                        print(','.join(item_box))
                                        continue
                                    elif ("take" in ite) & ("in hand" in ite):
                                        tag = nltk.pos_tag(ite.split())
                                        tmp = []
                                        for tup in tag:
                                            if (("NN" in tup) | ("NNS" in tup)) & ("hand" not in tup)&("hands" not in tup): tmp.append(tup[0])
                                        if len(tmp) == 0:
                                            print("I need to choose something to take.")
                                            print(f"Detected part of speech: {tag}.")
                                            print("Hint: When a noun failed to be detected,")
                                            print("try to add a adjective, pronoun, or article before it.")
                                            print("      Also, check if the grammar is correct.")
                                        elif len(tmp) > 2:
                                            print("I can only hold one item at a time.")
                                            print(f"Detected part of speech: {tag}.")
                                            print("Hint: When an unexpected noun is detected,")
                                            print("try to reduce nouns about general locations(eg. walls).")
                                            print("      Also, check if the grammar is correct.")
                                        else:
                                            tmp = ' '.join(tmp)
                                            hand = use_item(hand, tmp)
                                        continue
                                    elif ite == "go back":
                                        if 'present' in item_box:
                                            print("Am I sure about this? (Y/N)")
                                            choice = input("> ")
                                            choice = pan_y_or_n(choice)
                                            if choice == 'n':
                                                print("Alright, keep moving...")
                                                continue
                                        print("I paused for a moment...")
                                        sleep(0.5)
                                        print("Perhaps I needed more time to think before taking action.")
                                        sleep(0.5)
                                        ft=1
                                        break
                                    elif "set" in ite:
                                        print("...Am I thinking of another verb--'lay', perhaps?")
                                    elif "lay" in ite:
                                        if hand not in ite:
                                            print("I don't have that in my hands right now... Perhaps I should take it out first?")
                                            continue
                                        if hand != 'present':
                                            print("...")
                                            sleep(0.5)
                                            print("...")
                                            sleep(0.5)
                                            print("Nothing happened...")
                                            print(f"So I took the {hand} out again...")
                                        else:
                                            print("The moment I laid the present inside the case, some memories started to flood back...")
                                            print("I have such a certain feeling that if I put the present here, someone will come and find it with joy.")
                                            item_box.remove('present')
                                            sleep(0.5)
                                            print("After doing that, I closed the case's door.")
                                            case_3_o[0]=0
                                            clue[2] = 2
                                            ft=1
                                            break
                                    else:
                                        print("I don't think I am doing things logically...")
                                        sleep(0.3)
                                        print("Perhaps I should regain my thoughts...")
                                if ft==1:
                                    break
                        continue
                    else:
                        print("The door wouldn't budge... Perhaps I entered the wrong code.")
        elif 'pick up' in move:
            if "case" in move:
                print("Crack...")
                sleep(0.5)
                print("Crack...")
                sleep(0.5)
                print("Urr... The wood was cracking... It might fell apart if I picked it up...")
                continue
            if fl == 0:
                print("The case was not opened.")
            elif 'key' in move:
                if 'key' in case_3:
                    print("The key is picked up and I examined it.")
                    print("...")
                    sleep(0.5)
                    print("There's a small label on it saying: sash.")
                    print("Then I put into my item box.")
                    pick_up('key_sash')
                    case_3.remove('key')
                else:
                    print("I already picked that up from the case.")
            elif 'cylinder' in move:
                if 'cylinder' in case_3:
                    print("The cylinder is picked up and put into my item box.")
                    pick_up('cylinder')
                    case_3.remove('cylinder')
                    cylinder_num += 1
                else:
                    print("I already picked that up from the case.")
            elif 'diary' in move:
                print("Oof... It's so dusty...")
                sleep(0.5)
                print("And the leaves are so fragile...")
                sleep(0.5)
                print("I don't think it's a good idea picking it up... Let me rethink...")
                print("Do I need to take my time to memorize it? (Y/N)")
                choice = input("> ")
                choice = pan_y_or_n(choice)
                if choice == 'y':
                    print("I need more time... OK, Umm...")
                    print("On the page the diary was turned to read: ")
                    print("""Monday, January 16th
Dear diary,
It is going to be my 5th birthday soon! Alright it's still about four months away, but I am excited anyways!
Though daddy's busy, he promised to come home with a cake and play his traditional treasure hunt with me! Happy! 
FYI: Mom's fish soup rocks! And I overheard that she's going to make that for my birthday! ! !""")
                else:
                    print("Alright, what's next?")
                    continue
                while 1:
                    print("Done memorizing? (Y/N)")
                    choice = input("> ")
                    choice = pan_y_or_n(choice)
                    if choice == 'n':
                        print("I need more time... OK, Umm...")
                        print("On the page the diary was turned to read: ")
                        print("""Monday, January 16th
Dear diary,
It is going to be my 5th birthday soon! Alright it's still about four months away, but I am excited anyways!
Though daddy's busy, he promised to come home with a cake and play his traditional treasure hunt with me! Happy! 
FYI: Mom's fish soup rocks! And I overheard that she's going to make that for my birthday! ! !""")
                    else:
                        print("Alright, what's next?")
                        break
            else:
                tmp = []
                tag = nltk.pos_tag(move.split())
                for tup in tag:
                    if "NN" == tup[1]: tmp.append(tup[0])
                if len(tmp) == 0:
                    print("invalid input!")
                    print(f"Detected part of speech: {tag}.")
                    print("Hint: When a noun failed to be detected,")
                    print("try to add a adjective, pronoun, or article before it.")
                    print("      Also, check if the grammar is correct.")
                elif len(tmp) > 2:
                    print("Whoa, one at a time.")
                    print(f"Detected part of speech: {tag}.")
                    print("Hint: When an unexpected noun is detected,")
                    print("try to reduce nouns about general locations(eg. walls).")
                    print("      Also, check if the grammar is correct.")
        else:
            print("I think I need to pull on the handle if I want to open the case.")
    return hand, cylinder_num


def phone(time):
    while 1:
        print("Am I going to make a call? (Y/N)")
        choice = input("> ")
        choice = pan_y_or_n(choice)
        if choice == "n":
            print("Alright, I will come back later.")
            print("I put done the phone.")
            return
        print("Who do I want to call?")
        move = input("> ")
        if not move.isdecimal():
            print("Phone numbers need to be all arabic numerals and without spaces...")
            continue
        if (move != "377624")|(time!=1):
            print(".", end='')
            sleep(0.3)
            print(".", end='')
            sleep(0.3)
            print(".")
            sleep(0.5)
            print(".", end='')
            sleep(0.3)
            print(".", end='')
            sleep(0.3)
            print(".")
            sleep(0.5)
            print("Hum... nobody answered. Perhaps I got the wrong number...")
        else:
            print("Thank you for calling us! The cake will be delivered to your door.")
            clue[1] = 1
            print("Ting~~Tong~~")
            sleep(0.5)
            print("Someone's ringing the doorbell...")
            print("I'd better check it through the peephole.")
            front_door[0]=0
            peep_hole[0]=1


def case3(time,hand, cylinder_num):
    print("Can I still remember this case well? (Y/N)")
    choice = input("> ")
    choice = choice.lower()
    choice = pan_y_or_n(choice)
    if choice == 'n':
        print("I studied the case carefully...")
        sleep(0.5)
        print("It was a small wooden case... I think it can be opened...")
        print("On the top of the case was a phone.")
    while 1:
        move = input("> ")
        move = move.lower()
        check_help(move)
        check_quit(move)
        num_vb=check_vb(move)
        if num_vb!=1:continue
        num_noun = check_noun(move)
        if num_noun != 1: continue
        if ("take" in move) & ("in hand" in move):
            tag = nltk.pos_tag(move.split())
            tmp = []
            for tup in tag:
                if ("NN" in tup) & ("hand" not in tup)&("hands" not in tup): tmp.append(tup[0])
            if len(tmp) == 0:
                print("I need to choose something to take.")
                print(f"Detected part of speech: {tag}.")
                print("Hint: When a noun failed to be detected,")
                print("try to add a adjective, pronoun, or article before it.")
                print("      Also, check if the grammar is correct.")
            elif len(tmp) > 2:
                print("I can only hold one item at a time.")
                print(f"Detected part of speech: {tag}.")
                print("Hint: When an unexpected noun is detected,")
                print("try to reduce nouns about general locations(eg. walls).")
                print("      Also, check if the grammar is correct.")
            else:
                tmp = ' '.join(tmp)
                hand = use_item(hand, tmp)
        elif move == "go back":
            print("I left the case.")
            return hand, cylinder_num
        elif move == "check the item box":
            print(','.join(item_box))
        else:
            if 'phone' in move:
                if "pick up" in move:
                    print("Oh... it's plugged into the wall...")
                    print("I don't think it's a wise idea to pull it out...")
                elif "go to" in move:
                    print("I approached the phone...")
                    phone(time)
                elif ('smash' in move) | ('break' in move) | ('tear' in move) | ('eat' in move) | ('nock' in move) | (
                        'throw' in move):
                    print("...")
                    sleep(0.4)
                    print("I must be out of mind... I need to regain my thoughts.")
                else:
                    print("I might need to get a bit closer to the phone to do that.")
            elif 'case' in move:
                if "pick up" in move:
                    print("Crack...")
                    sleep(0.5)
                    print("Crack...")
                    sleep(0.5)
                    print("Urr... The wood was cracking... It might fell apart if I picked it up...")
                elif 'go to' in move:
                    print("I bent done so I could reach the case's door.")
                    hand, cylinder_num = case(hand, cylinder_num,time)
                elif ('smash' in move) | ('break' in move) | ('tear' in move) | ('eat' in move) | ('nock' in move) | (
                        'crush' in move):
                    print("...")
                    sleep(0.4)
                    print("I must be out of mind... I need to regain my thoughts.")
                elif ("open" in move) | ("drag" in move) | ("unlock" in move) | ("pull" in move):
                    print("I think I need to get a little closer to reach the case's door.")
                else:
                    print("I don't think that's a logical move... Perhaps I should come up with another thought.")
            else:
                tmp = []
                tag = nltk.pos_tag(move.split())
                for tup in tag:
                    if "NN" == tup[1]: tmp.append(tup[0])
                if len(tmp) == 0:
                    print("invalid input!")
                    print(f"Detected part of speech: {tag}.")
                    print("Hint: When a noun failed to be detected,")
                    print("try to add a adjective, pronoun, or article before it.")
                    print("      Also, check if the grammar is correct.")
                elif len(tmp) > 2:
                    print("Whoa, one at a time.")
                    print(f"Detected part of speech: {tag}.")
                    print("Hint: When an unexpected noun is detected,")
                    print("try to reduce nouns about general locations(eg. walls).")
                    print("      Also, check if the grammar is correct.")
                else:
                    print(f"No {' '.join(tmp)} in sight...")
    return hand, cylinder_num


def tvset(time, hand):
    if (time!=2)|(clue[2]==1):
        print("The TV is black...")
        print("Nothing's special about it so I stepped back.")
        return hand
    times=0
    while 1:
        if times!=0:
            while 1:
                print("Do I want to take another turn or go back and try again later?(take another turn/go back)")
                choice=input("> ")
                choice=choice.lower()
                if "go back" in choice:
                    print("I backed away from the tv set.")
                    return 0
                elif choice=="take another turn":
                    print("OK...")
                    break
                else:
                    print("...? Beg your pardon?")
                    continue
        print("Please insert TV+num...(For example TV111).")
        num=input("> ")
        num=num.lower()
        if num=="tv118":
            print("Number 12 is shown on TV...")
            num=input("> ")
            num=num.lower()
            if num=="tv12":
                print("Number 56 is shown on TV...")
                num=input("> ")
                num=num.lower()
                if num=='tv56':
                    print("There seemed to be something shown on TV...")
                    sleep(0.5)
                    print("Umm...")
                    sleep(0.8)
                    print("I think it reads:'Time for present! Check what's on the table!'")
                    print("I walked up to the dining table...")
                    clue[2]=1
                    time, hand = diningtable(time, 1, hand)
                    break
                else:
                    print("Nothing's on TV...")
                    times+=1
                    continue
            else:
                print("Nothing's on TV...")
                times+=1
                continue
        else:
            print("Nothing's on TV...")
            times+=1
            continue
    print("The TV went black again so I backed away.")
    return hand

def peephole(num):
    if num==0: print("There's nothing outside...")
    elif num==1:
        print("Hum... It seemed that the deliveryman just left...")
        sleep(0.5)
        print("Oh, there's a cute pinkish cake box with little white dotes on the door step.")
        print("Let me take a more careful look...")
        sleep(0.5)
        print("...")
        sleep(0.8)
        print("It was neatly wrapped with red and blue ribbons, tightened into a big lovely bowknot...")
        print("...")
        sleep(0.8)
        print("On the ribbons tied some balloons...")
        sleep(0.5)
        print("...")
        sleep(0.8)
        print("There seemed to be something written on them...")
        sleep(0.5)
        print("...")
        sleep(0.8)
        print("Then as if a gust of wind had blown by, the balloons are suddenly pressed against the peephole.")
        print("On them wrote: 321456987, 3695147, and 1235789")
        print("               Hint: Still using pattern lock for your phone?")
        print("                     Left to right! Top to bottom!")


def welcomerug(time,hand, photo_piece):
    if time==1:
        print("I slowly bent down to check the rug...")
        print("...")
        if rug[1]==1:
            print("Nothing special...")
            print("I stood up again.")
            return hand, photo_piece
        sleep(0.5)
        print("The rug was overall flat with a corner cocked up.")
        print("There seemed to be something under it...")
        print("...")
        sleep(0.5)
        print("Should I drag it to see what's underneath...?")
        while 1:
            move = input("> ")
            move = move.lower()
            check_help(move)
            check_quit(move)
            num_vb=check_vb(move)
            if num_vb == 0:
                if "dragging" in move:
                    print("Please use the verb form.")
                    continue
            if num_vb == 2: continue
            num_noun = check_noun(move)
            if num_noun != 1: continue
            if ("take" in move) & ("in hand" in move):
                tag = nltk.pos_tag(move.split())
                tmp = []
                for tup in tag:
                    if ("NN" in tup) & ("hand" not in tup)&("hands" not in tup): tmp.append(tup[0])
                if len(tmp) == 0:
                    print("I need to choose something to take.")
                    print(f"Detected part of speech: {tag}.")
                    print("Hint: When a noun failed to be detected,")
                    print("try to add a adjective, pronoun, or article before it.")
                    print("      Also, check if the grammar is correct.")
                elif len(tmp) > 2:
                    print("I can only hold one item at a time.")
                    print(f"Detected part of speech: {tag}.")
                    print("Hint: When an unexpected noun is detected,")
                    print("try to reduce nouns about general locations(eg. walls).")
                    print("      Also, check if the grammar is correct.")
                else:
                    tmp = ' '.join(tmp)
                    hand = use_item(hand, tmp)
            elif move == "go back":
                print("I stood up and stepped away from the rug.")
                return hand, photo_piece
            elif move == "check the item box":
                print(','.join(item_box))
            elif ('throw' in move) | ('crush' in move) | ('smash' in move) | ('break' in move) | ('tear' in move) | ('eat' in move) | ('nock' in move):
                print("...")
                sleep(0.4)
                print("I must be out of mind... I need to regain my thoughts.")
                continue
            elif "drag" in move:
                if "rug" in move:
                    print("Dragging...")
                    sleep(0.5)
                    print("Dragging...")
                    sleep(0.5)
                    if rug[1]==1:
                        print("... Nothing seemed to be under it...")
                        continue
                    print("A photo piece was revealed.")
                    pick_up("photo piece")
                    photo_piece+=1
                    rug[1]=1
                    continue
                else:
                    print("...?")
                    sleep(0.4)
                    print("I can only see the rug right now.")
            else:
                print("...")
                sleep(0.5)
                print("I wasn't doing things logically...")
    elif time==2:
        print("I slowly bent down to check the rug...")
        print("...")
        if rug[2]>=3:
            print("Nothing special...")
            print("I stood up again.")
            return hand, photo_piece
        sleep(0.5)
        print("The rug was overall flat, but slightly wrinkled in the middle...")
        print("...")
        sleep(0.5)
        print("What do I want to do next?")
        while 1:
            move = input("> ")
            move = move.lower()
            check_help(move)
            check_quit(move)
            num_vb=check_vb(move)
            if num_vb == 0:
                if "dragging" in move:
                    print("Please use the verb form.")
                    continue
            if num_vb == 2: continue
            num_noun = check_noun(move)
            if num_noun != 1: continue
            if ("take" in move) & ("in hand" in move):
                tag = nltk.pos_tag(move.split())
                tmp = []
                for tup in tag:
                    if ("NN" in tup) & ("hand" not in tup)&("hands" not in tup): tmp.append(tup[0])
                if len(tmp) == 0:
                    print("I need to choose something to take.")
                    print(f"Detected part of speech: {tag}.")
                    print("Hint: When a noun failed to be detected,")
                    print("try to add a adjective, pronoun, or article before it.")
                    print("      Also, check if the grammar is correct.")
                elif len(tmp) > 2:
                    print("I can only hold one item at a time.")
                    print(f"Detected part of speech: {tag}.")
                    print("Hint: When an unexpected noun is detected,")
                    print("try to reduce nouns about general locations(eg. walls).")
                    print("      Also, check if the grammar is correct.")
                else:
                    tmp = ' '.join(tmp)
                    hand = use_item(hand, tmp)
            elif move == "go back":
                print("I stood up and stepped away from the rug.")
                return hand, photo_piece
            elif "go to" in move:
                if "rug" in move: print("I'm already here...")
                else: print("There was nothing but the rug in front of me...")
            elif move == "check the item box":
                print(','.join(item_box))
            elif "pick up" in move:
                if "note" in move:
                    print("...")
                    sleep(0.5)
                    print("Urr...")
                    print("It's stuck... If I pull on it I might be ripped...")
                    sleep(0.5)
                    print("...")
                    sleep(0.5)
                    print("I think I'll need to remember the message written on it...")
                    print("TV118")
                    while 1:
                        print("Done remembering?(N/Y)")
                        choice=input("> ")
                        choice=pan_y_or_n(choice)
                        if choice=='n':
                            print("TV118")
                        else:
                            print("Alright... Oh no... It slipped into the crack on the ground.")
                            break
                elif "family photo" in move:
                    print("I already picked that up...")
                    continue
                else:
                    print("... I don't see it...")
                    sleep(0.4)
                    print("Perhaps I thought wrong...")
            elif ('throw' in move) | ('crush' in move) | ('smash' in move) | ('break' in move) | ('tear' in move) | ('eat' in move) | ('nock' in move):
                print("...")
                sleep(0.4)
                print("I must be out of mind... I need to regain my thoughts.")
                continue
            elif "drag" in move:
                if "rug" in move:
                    print("Dragging...")
                    sleep(0.5)
                    print("Dragging...")
                    sleep(0.5)
                    rug[2]+=1
                    if rug[2]==2:
                        print("There's a note reading: TV118.")
                    elif rug[2]==3:
                        sleep(0.5)
                        print("... A family photo revealed...")
                        sleep(0.5)
                        print("They all smiled so happily on it...")
                        sleep(0.5)
                        print("But why are there only two of them...")
                        sleep(0.5)
                        print("It seemed so familiar that I was reaching for it before I knew it.")
                        pick_up("family photo")
                        clue[3]=1
                    else:
                        print("Nothing seemed to be under it...")
                    continue
                else:
                    print("...?")
                    sleep(0.4)
                    print("I can only see the rug right now.")
            else:
                if "rug" in move:
                    print("I think I can move the rug by dragging.")
                    continue
                print("...")
                sleep(0.5)
                print("I wasn't doing things logically...")
    return hand,photo_piece


def frontdoor(hand):
    print("I examined the front door.")
    print("There was a small glass peephole on it.")
    print("It was a plain wooden door painted yellow...")
    print("A doorknob was on the right.")
    while 1:
        move = input("> ")
        move = move.lower()
        check_help(move)
        check_quit(move)
        num_vb = check_vb(move)
        if num_vb == 0:
            if ("pulling" in move)| ("opening" in move)|("dragging" in move)|("turning" and "handle" in move):
                print("Please use the verb form.")
            continue
        if num_vb == 2: continue
        num_noun=check_noun(move)
        if num_noun!=1: continue
        if move == "check the item box":
            print(','.join(item_box))
            continue
        elif ("take" in move) & ("in hand" in move):
            tag = nltk.pos_tag(move.split())
            tmp = []
            for tup in tag:
                 if (("NN" in tup) | ("NNS" in tup)) & ("hand" not in tup)&("hands" not in tup): tmp.append(tup[0])
            if len(tmp) == 0:
                print("I need to choose something to take.")
                print(f"Detected part of speech: {tag}.")
                print("Hint: When a noun failed to be detected,")
                print("try to add a adjective, pronoun, or article before it.")
                print("      Also, check if the grammar is correct.")
            elif len(tmp) > 2:
                print("I can only hold one item at a time.")
                print(f"Detected part of speech: {tag}.")
                print("Hint: When an unexpected noun is detected,")
                print("try to reduce nouns about general locations(eg. walls).")
                print("      Also, check if the grammar is correct.")
            else:
                tmp = ' '.join(tmp)
                hand = use_item(hand, tmp)
            continue
        elif move == "go back":
            if front_door[0]==1:
                print("Do I want to close the door and leave now? (Y/N)")
                choice=input("> ")
                choice=pan_y_or_n(choice)
                if choice=='n':
                    print("I don't think I wanted to go back at this moment...")
                    continue
                else:
                    print("Click... I closed the front door")
                    sleep(0.5)
                    print("Click...")
                    sleep(0.5)
                    print("Click... It's locked again")
                    front_door[0]=0
            print("I left the front door.")
            return hand
        elif "peephole" in move:
            if 'go to' in move:
                peephole(peep_hole[0])
            elif ('lick' in move)|('bump' in move)|('throw' in move) | ('crush' in move) | ('smash' in move) | ('break' in move) | ('tear' in move) | ('eat' in move) | ('nock' in move):
                print("...")
                sleep(0.4)
                print("I must be out of mind... I need to regain my thoughts.")
                continue
            else:
                print("Perhaps I need to go a little closer to the peephole to do that.")
        elif ("balloons" in move)|("ribbons" in move)|("cake box" in move):
            if front_door[0]!=1:
                print("Urr... I think need to open the door first...")
                continue
            if "cake box" in move:
                if "go to" in move:
                    print("It's already within my reach.")
                elif "pick up" in move:
                    pick_up("cake box")
                    print("I slowly closed the front door.")
                    front_door[0]=2
            elif "ribbons" in move:
                print("Oops... It's slippery and I almost untied it.")
                print("Perhaps I should try to pick up the cake box instead.")
            else:
                print("...")
                sleep(0.4)
                print("Umm... I can see no such thing(s) in sight...")
        elif ("door" in move)&("front" not in move):
            print("...?")
            print("...the front door is all I could see...")
            print("Was I thinking of that?")
        elif ("front door" in move)|("doorknob" in move)|("handle" in move):
            if "go to" in move: print("I am already here...")
            elif ('lick' in move)|('bump' in move)|('throw' in move) | ('crush' in move) | ('smash' in move) | ('break' in move) | ('tear' in move) | ('eat' in move) | ('nock' in move):
                print("...")
                sleep(0.4)
                print("I must be out of mind... I need to regain my thoughts.")
                continue
            elif ("open" in move)|("turn" in move)|("pull" in move)|("drag" in move)|("push" in move)|("twist" in move):
                if front_door[0]==2:
                    print("Nothing's outside... Why should I bother?")
                    continue
                elif front_door[0]==1:
                    print("Already opened...")
                print("Clinking...")
                sleep(0.5)
                print("...")
                sleep(0.5)
                print("Clinking...")
                sleep(0.5)
                print("Oh... It's locked...")
                print("I studied the doorknob carefully...")
                print("It seemed like a passcode lock...")
                print("Hum...")
                sleep(0.5)
                print("...There are three empty spaces...")
                sleep(0.5)
                print("...")
                print("A picture was next to the doorknob...")
                sleep(0.5)
                print("...An alphabet chart...")
                sleep(0.5)
                print("And... Three balloons...?")
                while 1:
                    print("Am I going to insert the code? (Y/N)")
                    choice=input("> ")
                    choice=pan_y_or_n(choice)
                    if choice=='n':
                        print("Never mind that now...")
                        print("I stopped trying to open the door")
                        break
                    else:
                        print("And the code should be?")
                        code=input("> ")
                        code=code.lower()
                        if ' ' in code:
                            print("There shouldn't be any spaces...")
                            continue
                        if code=='snz':
                            front_door[0]=1
                            print("Click...")
                            sleep(0.5)
                            print("Click...")
                            sleep(0.5)
                            print("Click...")
                            sleep(0.5)
                            print("With three clear clicking sound, the door swooshed open.")
                            print("The cake box was just in front of me. All balloons seemed to have flown away.")
                            front_door[0]=1
                            break
                        else:
                            print("Click...Squeak...")
                            print("The front door had no sign of opening...")
        elif "go to" in move:
            print("I can only see the front door right now...")
            print("I can only go closer to the peephole to see what's outside...")
        else:
            print("... ...?")
            print("My brain wasn't functioning logically...")
    return hand

def bugs(color):
    if color == 'red':
        print("The bug was startled and flew in a circular trajectory.")
    elif color == 'white':
        print("The bug lay still, with a few flaps in its wings.")
    elif color == 'green':
        print("The bug was startled and flew straight up and down.")
    elif color == 'yellow':
        print("The bug was startled and flew in a rectangular trajectory.")
    print(f"I stepped away from the {color} bug.")
    return

def switch(hand):
    while 1:
        move=input("> ")
        move=move.lower()
        check_help(move)
        check_quit(move)
        if move=="go back":
            print("I backed away from the switch.")
            return ceil_light1
        elif move=="check the item box":
            print(','.join(item_box))
            continue
        elif ("take" in move)&("in hand" in move):
            tag=nltk.pos_tag(move.split())
            tmp=[]
            for tup in tag:
                if (("NN" in tup)|("NNS" in tup))&("hand" not in tup)&("hands" not in tup): tmp.append(tup[0])
            if len(tmp) == 0:
                print("I need to choose something to take.")
                print(f"Detected part of speech: {tag}.")
                print("Hint: When a noun failed to be detected,")
                print("try to add a adjective, pronoun, or article before it.")
                print("      Also, check if the grammar is correct.")
            elif len(tmp) > 2:
                print("I can only hold one item at a time.")
                print(f"Detected part of speech: {tag}.")
                print("Hint: When an unexpected noun is detected,")
                print("try to reduce nouns about general locations(eg. walls).")
                print("      Also, check if the grammar is correct.")
            else:
                tmp = ' '.join(tmp)
                hand=use_item(hand, tmp)
            continue
        if "switch" in move:
            if("flick" in move) | ("turn" in move) | ("press" in move)| ("flip" in move):
                ceil_light1[0]=1-ceil_light1[0]
                if ceil_light1[0]==0:
                    print("I flicked the switch to turn off the ceil light.")
                elif ceil_light1[0]==1:
                    print("I flicked the switch to turn on the ceil light.")
            elif("smash" in move)|("break" in move):
                print("At the risk of having electric shock? Umm... I don't think so.")
            else:
                num_vb = check_vb(move)
                if num_vb!=1: continue
                else: print("I can't do that with a switch.")
        else :
            print("...?")
            print("I can see nothing but the switch.")
    return hand


def sash(time, hand):
    fl=0
    if time==3:
        print("I can't get to it... it's behind the curtain...")
        return hand
    print("I stood in front of the sash.")
    if time==1:
        print("The sun wasn't fully up yet.")
        print("Thick morning mist was still looming part of the tree tops.")
        print("The sky was faintly lit, with a cold bluish color.")
        sleep(0.5)
    elif time==2:
        print("The sun was setting slowly afar, dying the sky in a pinkish color.")
        print("Slowly, orange and red and yellow and purple were all poured into the pink sky, forming a fascinating scene.")
        sleep(0.5)
    print("I figured the perhaps the sash can be slid to the side.")
    while 1:
        move = input("> ")
        move = move.lower()
        check_help(move)
        check_quit(move)
        num_vb=check_vb(move)
        if num_vb == 0:
            if "sliding" in move:
                print("Please use the verb form.")
                continue
        if num_vb == 2: continue
        num_noun = check_noun(move)
        if num_noun != 1: continue
        if ("take" in move) & ("in hand" in move):
            tag = nltk.pos_tag(move.split())
            tmp = []
            for tup in tag:
                if ("NN" in tup) & ("hand" not in tup)&("hands" not in tup): tmp.append(tup[0])
            if len(tmp) == 0:
                print("I need to choose something to take.")
                print(f"Detected part of speech: {tag}.")
                print("Hint: When a noun failed to be detected,")
                print("try to add a adjective, pronoun, or article before it.")
                print("      Also, check if the grammar is correct.")
            elif len(tmp) > 2:
                print("I can only hold one item at a time.")
                print(f"Detected part of speech: {tag}.")
                print("Hint: When an unexpected noun is detected,")
                print("try to reduce nouns about general locations(eg. walls).")
                print("      Also, check if the grammar is correct.")
            else:
                tmp = ' '.join(tmp)
                if (tmp=='key'):
                    print("Which key? I think I need to specify that...")
                    continue
                elif (tmp=="sash key")|(tmp=="sash's key"):
                    print("...?")
                    sleep(0.3)
                    print("Perhaps I was thinking of key_sash?")
                    continue
                hand = use_item(hand, tmp)
        elif move == "go back":
            print("I left the sash.")
            return hand
        elif "go to" in move:
            if "sash" in move: print("I'm already here...")
            elif "outside" in move: print("I need to open the sash first...")
            else: print("There was nothing but the sash in front of me...")
        elif move == "check the item box":
            print(','.join(item_box))
        elif ('throw' in move) | ('crush' in move) | ('smash' in move) | ('break' in move) | ('tear' in move) | ('eat' in move) | ('nock' in move):
            print("...")
            sleep(0.4)
            print("I must be out of mind... I need to regain my thoughts.")
            continue
        elif ("open" in move)|("unlock" in move)|("move" in move)|("drag" in move)|("pull" in move)|("push" in move):
            if "sash" not in move:
                print("...?")
                sleep(0.4)
                print("All there was in front of me is the sash, nothing else.")
                continue
            print("I think I can slide the sash to open it.")
        elif "slide" in move:
            if "sash" not in move:
                print("...?")
                sleep(0.4)
                print("All there was in front of me is the sash, nothing else.")
                continue
            if hand=='key_sash':
                print("I insert the sash's key into its keyhole and slid open the sash.")
                if time==1:
                    print("I could feel cold morning breeze upon my cheeks.")
                    print("I felt refreshed...")
                    sleep(0.5)
                    print("All normal, so I stepped back and slid close the sash.")
                elif time==2:
                    print("Under the warm glow of the sunset, the road into the small forest seemed queer but enchanting.")
                    sleep(0.5)
                    if fl==1:
                        print("I just admired the view peacefully...")
                        continue
                    print("...A strong feeling inside of me was telling me to go in.")
                    sleep(0.5)
                    print("But do I remember the way...?")
                    print("Forward-1, backward-2, left-3, right-4.")
                    times=0
                    while 1:
                        if times!=1:
                            print("Do I want to continue moving? (Y/N)")
                            choice=input("> ")
                            choice=pan_y_or_n(choice)
                            if choice=='n':
                                print("Ok... I slowly closed the sash.")
                                break
                            else:
                                print("I insisted to keep trying.")
                            print("Do I need a hint? (Y/N)")
                            choice=input("> ")
                            choice=pan_y_or_n(choice)
                            if choice=='y':
                                print("Hint: treasure map.")
                        code = input("> ")
                        if not code.isdecimal(): print("Please insert only arabic numerals, no spaces.")
                        else:
                            if code!='11442411131':
                                print("Umm... I ended up getting nowhere.")
                                print("Perhaps I went in the wrong way at some point...")
                                print("I went back to the sash, empty-handed.")
                                continue
                            else:
                                print("Umm... I examined my surroundings...")
                                sleep(0.5)
                                print("I and in the middle of a circle of giant trees...")
                                sleep(0.5)
                                print("Wait... there's something on the ground...")
                                sleep(0.5)
                                print("Hum... It's a pack of candles...")
                                print("I suppose I'll pick it up and go back...")
                                pick_up("candles")
                                print("I went back to the sash.")
                                fl=1
                continue
            print("I tried hard to slide it...")
            sleep(0.5)
            print("... Oof")
            sleep(0.5)
            print("Urr...")
            sleep(0.3)
            print("The sash couldn't be moved an inch!")
            print("Perhaps it's locked...")
            print("I think I need to take out its key first...")
        else:
            print("...")
            sleep(0.5)
            print("I wasn't doing things logically...")
    return hand

def diningtable(time, face, hand):
    tmp_there=["fish", "shrimp", "lobster", "starfish", "crab", "molluscs","vegetables"]
    tmp_cut=[]
    if time==1:
        print(dining_table[0])
        if "cake box" in item_box:
            clue[1]=2
            print("I took out the cake box and set it onto the dining table.")
            item_box.remove("cake box")
            dining_table[0]="There lay the cake box I just set on."
        print("I went away.")
        print(f"{wall_nums_general[face]} Again")
        return time, hand
    elif time==2:
        print(dining_table[0])
        print("And...")
        sleep(0.5)
        print("I examined it more carefully...")
        sleep(0.5)
        if (clue[2]==1)&("present" not in item_box):
            print("And...A small present.")
        else:
            print("And...Nothing else...")
        while 1:
            move=input("> ")
            move=move.lower()
            check_help(move)
            check_quit(move)
            num_noun = check_noun(move)
            if num_noun != 1: continue
            if ("candle" in move)&("take" not in move)&("in hand" not in move):
                if ("put on" in move)|("insert" in move)|("place" in move)|("plant" in move):
                    if candon[0]==1:
                        print("I already did that...")
                        continue
                    if hand!="candles":
                        print("I don't have them in my hands now...")
                        print("perhaps I should take it out first?")
                        continue
                    print("How many candles do I want to put onto the cake?")
                    times=-1
                    while 1:
                        times+=1
                        if times!=0:
                            print("Do I want to keep trying?(N/Y)")
                            choice=input("> ")
                            choice=pan_y_or_n(choice)
                            if choice=='n':
                                print("Alright, I'll come back later...")
                                break
                            else:
                                print("How many candles do I want to put onto the cake?")
                        num_candles=input("> ")
                        if not num_candles.isdecimal():
                            print("Please insert arabic numerals.")
                            continue
                        if num_candles!='5':
                            print("Urr...")
                            sleep(0.4)
                            print("Why can't I open the rip open the candle package?")
                            continue
                        else:
                            print("I opened the package and took the candles out...")
                            sleep(0.5)
                            print("One...")
                            sleep(0.5)
                            print("Two...")
                            sleep(0.5)
                            print("Three...")
                            sleep(0.5)
                            print("Four...")
                            sleep(0.5)
                            print("Five...")
                            sleep(0.5)
                            print("And... done!")
                            candon[0]=1
                            break
                elif ("light" in move)|("lit" in move)|("ignite" in move)|("kindle" in move):
                    if candon[0]==0:
                        print("I haven't put the candles on the cake yet...")
                        continue
                    elif candon[0]==2:
                        print("Already burning...")
                        continue
                    if hand!="matches":
                        print(f"I can't ignite the candles with {hand}!")
                        print("Perhaps I'll be needing some matches...")
                        print("Have I got any?")
                        continue
                    print("I stroke a match and lit up all five candles.")
                    time=3
                    afternoon_end()
                    evening_st(face)
                    return time, hand
                continue
            num_vb = check_vb(move)
            if num_vb == 0:
                if ("cutting" in move)| ("slicing" in move):
                    print("...Did I mean to cut?")
                continue
            if num_vb == 2: continue
            if move=="go back":
                print("I left the dining table.")
                sleep(0.5)
                print("Ok...")
                print(f"I think {wall_nums_general[face]} Again.")
                return time, hand
            elif move=="check the item box":
                print(','.join(item_box))
                continue
            elif ("take" in move) & ("in hand" in move):
                tag = nltk.pos_tag(move.split())
                tmp = []
                for tup in tag:
                    if (("NN" in tup) | ("NNS" in tup)) & ("hand" not in tup)&("hands" not in tup): tmp.append(tup[0])
                if len(tmp) == 0:
                    print("I need to choose something to take.")
                    print(f"Detected part of speech: {tag}.")
                    print("Hint: When a noun failed to be detected,")
                    print("try to add a adjective, pronoun, or article before it.")
                    print("      Also, check if the grammar is correct.")
                elif len(tmp) > 2:
                    print("I can only hold one item at a time.")
                    print(f"Detected part of speech: {tag}.")
                    print("Hint: When an unexpected noun is detected,")
                    print("try to reduce nouns about general locations(eg. walls).")
                    print("      Also, check if the grammar is correct.")
                else:
                    tmp = ' '.join(tmp)
                    hand = use_item(hand, tmp)
                continue
            elif ('bite' in move)|('lick' in move)|('bump' in move)|('throw' in move) | ('crush' in move) | ('smash' in move) | ('break' in move) | ('tear' in move) | ('eat' in move) | ('nock' in move):
                if (('bite' in move)|('lick' in move)|('eat' in move)|('swallow' in move)|("grab" in move))&("cake" in move):
                    print("This cake wasn't for me...")
                    continue
                print("...")
                sleep(0.4)
                print("I must be out of mind... I need to regain my thoughts.")
                continue
            elif (("open" in move)|("unwrap" in move)|("unbox" in move))&("present" in move):
                print("The present wasn't for me...")
            elif "go to" in move:
                if ("present" not in move)&("cake" not in move):
                    print("...?")
                    sleep(0.5)
                    print("What or where...? I can't see it...")
                    continue
                else:
                    print("It's already within reach.")
            elif "pick up" in move:
                if "cake" in move:
                    print("It's not for me...")
                elif "present" in move:
                    pick_up("present")
                elif "flame" in move:
                    print("I don't think I am capable of doing that...")
                elif "candles" in move:
                    print("... Why? I just put it on.")
                else:
                    print("...?")
                    sleep(0.5)
                    print("It seemed to be out of sight...")
            elif ('cut' in move)|("slice" in move):
                if "cake" in move:
                    print("It's not time to cut the cake yet...")
                    if candon[0]==0:
                        print("I think I need to put the candles on first...")
                    elif candon[0]==1:
                        print("I believe that I need to lit up the candles first...")
                elif ("present" in move)|("candles" in move)|("flame" in move):
                    print("I don't think I am capable of doing that...")
                else:
                    print("...?")
                    sleep(0.5)
                    print("It seemed to be out of sight...")
            else:
                print("...")
                sleep(0.4)
                print("I must regain my though...")
                print("There's no point in taking that move...")
    elif time==3:
        fl=0
        print(dining_table[0])
        print("I stood still for a moment...")
        print("A feeling rose inside of me... Perhaps I should help dissect something.")
        while 1:
            move=input("> ")
            move=move.lower()
            check_help(move)
            check_quit(move)
            num_vb = check_vb(move)
            if num_vb == 0:
                if ("cutting" in move)| ("slicing" in move) |("slice" in move):
                    print("I was thinking of the word 'cut' perhaps?")
                continue
            if num_vb == 2: continue
            num_noun = check_noun(move)
            if num_noun != 1: continue
            if move=="go back":
                print("I left the dining table.")
                print(f"{wall_nums_general[face]} Again.")
                return time,hand
            elif move=="check the item box":
                print(','.join(item_box))
                continue
            elif ("take" in move) & ("in hand" in move):
                tag = nltk.pos_tag(move.split())
                tmp = []
                for tup in tag:
                    if (("NN" in tup) | ("NNS" in tup)) & ("hand" not in tup)&("hands" not in tup): tmp.append(tup[0])
                if len(tmp) == 0:
                    print("I need to choose something to take.")
                    print(f"Detected part of speech: {tag}.")
                    print("Hint: When a noun failed to be detected,")
                    print("try to add a adjective, pronoun, or article before it.")
                    print("      Also, check if the grammar is correct.")
                elif len(tmp) > 2:
                    print("I can only hold one item at a time.")
                    print(f"Detected part of speech: {tag}.")
                    print("Hint: When an unexpected noun is detected,")
                    print("try to reduce nouns about general locations(eg. walls).")
                    print("      Also, check if the grammar is correct.")
                else:
                    tmp = ' '.join(tmp)
                    hand = use_item(hand, tmp)
                continue
            elif ('lick' in move)|('bump' in move)|('throw' in move) | ('crush' in move) | ('smash' in move) | ('break' in move) | ('tear' in move) | ('eat' in move) | ('nock' in move):
                if (('lick' in move)|('eat' in move)|('swallow' in move)|("grab" in move))&("cake" in move):
                    print("The food was raw... And I believe that they wasn't prepared for me...")
                print("...")
                sleep(0.4)
                print("I must be out of mind... I need to regain my thoughts.")
                continue
            elif (("open" in move)|("unwrap" in move)|("unbox" in move))&("present" in move):
                print("...")
                sleep(0.4)
                print("I must be out of mind... I need to regain my thoughts.")
                continue
            elif "go to" in move:
                if ("seafood" not in move)&("vegetables" not in move):
                    print("...?")
                    sleep(0.5)
                    print("What or where...? I can't see it...")
                    continue
                else:
                    print("It's already within reach.")
            elif "pick up" in move:
                if "seafood" in move:
                    print("It's not for me to take...")
                elif "vegetable" in move:
                    print("It's not for me to take...")
                else:
                    print("...?")
                    sleep(0.5)
                    print("It seemed to be out of sight...")
            elif ("cut" in move)|("dissect" in move):
                if hand!="knife":
                    print(f"I can't cut or dissect with {hand}!")
                    print("Perhaps I'll be needing a knife...")
                    continue
                if "vegetables" in move:
                    if "vegetables" in tmp_cut: print("I already cut those...")
                    else:
                        print("I cut them up.")
                        tmp_there.remove("vegetables")
                        tmp_cut.append("vegetables")
                elif "seafood" in move:
                    print("What kind of seafood do I want to cut or dissect? (Fish/Shrimp/Lobster/Starfish/Crab/Molluscs)")
                    choice=input("> ")
                    choice=choice.lower()
                    if choice not in tmp_there:
                        if choice in tmp_cut: print("I already cut those...")
                        else: print("I don't see that type of seafood in sight...")
                    else:
                        print(f"I dissected the {choice}.")
                        tmp_there.remove(choice)
                        tmp_cut.append(choice)
                        if choice=='fish':
                            print("...")
                            sleep(0.5)
                            print("Wait...")
                            sleep(0.5)
                            print("I think there was something in the fish's gut...")
                            sleep(0.5)
                            print("Oh... There were two keys...")
                            sleep(0.5)
                            print("One is made of glass... Umm...")
                            sleep(0.5)
                            print("And... The other is a key labeled with basement.")
                            sleep(0.5)
                            print("I'd better pick them up...")
                            pick_up("glass key")
                            pick_up("key_basement")
                else:
                    ft=0
                    for a in tmp_there:
                        if a in move.split():
                            print(f"I dissected the {a}.")
                            tmp_there.remove(a)
                            tmp_cut.append(a)
                            if a=='fish':
                                print("...")
                                sleep(0.5)
                                print("Wait...")
                                sleep(0.5)
                                print("I think there was something in the fish's gut...")
                                sleep(0.5)
                                print("Oh... There were two keys...")
                                sleep(0.5)
                                print("One is made of glass... Umm...")
                                sleep(0.5)
                                print("And... The other is a key labeled with basement.")
                                sleep(0.5)
                                print("I'd better pick them up...")
                                pick_up("glass key")
                                pick_up("key_basement")
                            ft=1
                            break
                    if ft==0:
                        for a in tmp_cut:
                            if a in move:
                                ft=1
                                print("I already cut those...")
                                break
                        if ft==0:
                            print("It's not in sight...")
                            print("I should think of other things to cut or dissect...")
            else:
                print("...")
                sleep(0.4)
                print("I must regain my though...")
                print("There's no point in taking that move...")

def basement(hand):
    print("Approaching the basement door...")
    print("Now I am in front of the basement door.")
    print("I think I can try to open the basement door by pulling its handle.")
    while 1:
        move = input("> ")
        move = move.lower()
        check_help(move)
        check_quit(move)
        num_vb=check_vb(move)
        if num_vb == 0:
            if "pulling" in move:
                print("Please use the verb form.")
            continue
        if num_vb == 2: continue
        num_noun = check_noun(move)
        if num_noun != 1: continue
        if ("take" in move) & ("in hand" in move):
            tag = nltk.pos_tag(move.split())
            tmp = []
            for tup in tag:
                if ("NN" in tup) & ("hand" not in tup)&("hands" not in tup): tmp.append(tup[0])
            if len(tmp) == 0:
                print("I need to choose something to take.")
                print(f"Detected part of speech: {tag}.")
                print("Hint: When a noun failed to be detected,")
                print("try to add a adjective, pronoun, or article before it.")
                print("      Also, check if the grammar is correct.")
            elif len(tmp) > 2:
                print("I can only hold one item at a time.")
                print(f"Detected part of speech: {tag}.")
                print("Hint: When an unexpected noun is detected,")
                print("try to reduce nouns about general locations(eg. walls).")
                print("      Also, check if the grammar is correct.")
            else:
                tmp = ' '.join(tmp)
                if (tmp=='key'):
                    print("Which key? I think I need to specify that...")
                    continue
                elif (tmp=="basement key")|(tmp=="basement's key"):
                    print("...?")
                    sleep(0.3)
                    print("Perhaps I was thinking of key_basement?")
                    continue
                hand = use_item(hand, tmp)
        elif move == "go back":
            print("I left the basement door.")
            return hand
        elif ('throw' in move) | ('crush' in move) | ('smash' in move) | ('break' in move) | ('tear' in move) | ('eat' in move) | ('nock' in move):
            print("...")
            sleep(0.4)
            print("I must be out of mind... I need to regain my thoughts.")
            continue
        elif ("open" in move) | ("drag" in move) |("unlock" in move):
            print("I need to pull the handle to open the case.")
        elif "go to" in move:
            if "basement door" in move: print("I'm already here...")
            elif "basement" in move: print("I need to open the door first...")
            else: print("There was nothing but the basement door in front of me...")
        elif 'pull' in move:
            if 'handle' not in move:
                print("The only thing in sight that I could pull is the door handle...")
                continue
            print("Clunk...")
            sleep(0.5)
            print("Clunk...")
            sleep(0.5)
            print("It's locked...")
            if hand!= "key_basement":
                print("I'd better take out the key first.")
                continue
            else:
                print("I inserted the key into the lock and turned it slowly...")
                sleep(0.5)
                print("Click...")
                sleep(0.5)
                print(".... Creak....")
                sleep(0.5)
                print("I slowly opened the basement's door.")
                break
        elif move == "check the item box":
            print(','.join(item_box))
        else:
            print("...")
            sleep(0.4)
            print("I wasn't doing things logically...")
    print("There was a long winding stairway... ")
    sleep(0.5)
    print("I slowly went down the stairs...")
    sleep(0.5)
    print("Hum...")
    sleep(0.5)
    print("There's not much in here...")
    print("All I could see was a ladder on the ground and a wall filled with family photos.")
    if clue[3]==1:
        print("Wait... There seemed to be one family photo missing...")
        print("Oh... I remembered picking up one when I was moving the rug earlier!")
        if hand!="family photo":
            hand="family photo"
            print("I took out the family photo from the item box and stuck it back onto the wall.")
        else:
            print("I stuck the photo back onto the wall.")
        item_box.remove("family photo")
        hand="my hands"
        print("After sticking, I stared at the wall and was somehow lost in thought...")
        sleep(0.5)
        print("I couldn't remember what I was thinking of, but the moment I regained my concentration...")
        sleep(0.5)
        print("...I felt my cheeks were a little wet, and so were my eyes...")
        sleep(0.5)
        print("Although I was walking towards the ladder, my mind is still lingered to that wall...")
        sleep(0.5)
        print("...Lingered to all the photos of three, and that particular one of two...")
    else:
        print("I walked up to the ladder.")
    while 1:
            move = input("> ")
            move = move.lower()
            check_help(move)
            check_quit(move)
            num_vb=check_vb(move)
            if num_vb != 1: continue
            num_noun = check_noun(move)
            if num_noun != 1: continue
            if ("take" in move) & ("in hand" in move):
                tag = nltk.pos_tag(move.split())
                tmp = []
                for tup in tag:
                    if ("NN" in tup) & ("hand" not in tup)&("hands" not in tup): tmp.append(tup[0])
                if len(tmp) == 0:
                    print("I need to choose something to take.")
                    print(f"Detected part of speech: {tag}.")
                    print("Hint: When a noun failed to be detected,")
                    print("try to add a adjective, pronoun, or article before it.")
                    print("      Also, check if the grammar is correct.")
                elif len(tmp) > 2:
                    print("I can only hold one item at a time.")
                    print(f"Detected part of speech: {tag}.")
                    print("Hint: When an unexpected noun is detected,")
                    print("try to reduce nouns about general locations(eg. walls).")
                    print("      Also, check if the grammar is correct.")
                else:
                    tmp = ' '.join(tmp)
                    hand = use_item(hand, tmp)
            elif move == "go back":
                print("Am I done checking the basement? (Y/N)")
                ans=input("> ")
                ans=pan_y_or_n(ans)
                if ans=='y':
                    print("I climbed up the stairs.")
                    return hand
                else:
                    print("Keep checking...")
            elif move == "check the item box":
                print(','.join(item_box))
            elif ('throw' in move) | ('crush' in move) | ('smash' in move) | ('break' in move) | ('tear' in move) | ('eat' in move) | ('nock' in move):
                print("...")
                sleep(0.4)
                print("I must be out of mind... I need to regain my thoughts.")
                continue
            elif "pick up" in move:
                if "ladder" in move: pick_up("ladder")
                else:
                    print("All I could see was the ladder...")
                    continue
            elif "go to" in move:
                if ("wall" in move)&("family photo" in move):
                    print("Hum... it disappeared...")
                elif "ladder" in move:
                    print("I could already reach the ladder.")
                else:
                    print("...?")
            else:
                print("...")
                sleep(0.4)
                print("I wasn't doing things logically...")
    return hand

def hidden_scene():
    print("Hey mom! The cake daddy promised was delivered!")
    print("No honey... why... Oh! There's a cake delivered?! That's... too good... to be true.(murmur)")
    sleep(0.8)
    print("...")
    sleep(0.5)
    print("...")
    sleep(0.8)
    print("Hey mom! I found a present in the case!!! That's a really good place to hide it! He sure knows how to play a treasure hunt!")
    print("... He sure does...Umm..")
    print("M-o-m! You are not even a little overjoyed that I found it this year without father's hint?")
    print("Why... why.. dear, I am just to astonished to speak! Congratulations sweetie! Yor find this year's present all on your own!")
    sleep(0.8)
    print("...")
    sleep(0.5)
    print("...")
    sleep(0.8)
    print("Hey mom! The fish was already cleaned!! Fish soup! Fish soup!! Fish soup!!!")
    print("Alright...! Coming right up.")
    print("Hey, I told you daddy would be celebrating my birthday this year as well! No matter what faraway places they say he went to!")
    print("Of...of course! Darling! Remember, not just birthdays, he will always be there for you!")
    print("Yeah! I know! He's just hiding himself as a big treasure hunt!")
    print("Hum?")
    print("Oops, please forget that... Oh alright... This letter was supposed to be for me, but I'll let you read it after dinner.")
    sleep(0.8)
    print("...")
    sleep(0.5)
    print("...")
    sleep(0.8)
    print("""Dear my little apple cheek,
Happy birthday!
I want to do something grand for this year!
I hid myself as a big bonus present!
I will hide as hard as I can if you are trying to find me.
Just remember that I will always be watching out for you even if you haven't find me yet.
Stay happy and lively every day even if you might forfeit a little when you can't find me for a long time.
Cause... I am a really good hider! Ha ha ha!
But just in case that your mom and I set a date in advance to make it all clear to you about where exactly I was hiding.
Don't be mislead by anyone else's words about where I am!
And I am sure that you have the ability to hold your curiosity until the time comes right? No spoil alerts!
Good luck every day!
Love
Father""")


def bonus():
    print("As I tightened the rope around the pole, memories started flooding back to me.")
    sleep(0.8)
    print("I saw a little girl smiling and laughing and running to greet me happily from the inside the room...")
    sleep(0.8)
    print("I watched how excitement and surprise crawled upon her face as she found the present I'd hidden...")
    sleep(0.8)
    print("I appreciated the scene where she shut her eyes tight, making her wish in such a pondering sense...")
    print("and blew out all candles in one go...")
    sleep(0.8)
    print("I saw myself, holding her up with both my hands as if making her flying around...")
    sleep(0.8)
    print("My eyes begun to water as the scene halted at the point when me, her and my wife were sticking our family photo on that special wall.")
    sleep(0.8)
    print("I would never broke the promise to celebrate every one of my little girls birthday... Even if it's the end of the world...")
    sleep(0.8)
    print("I even did it this time... though this might be the last time I could keep my promise...")
    sleep(0.8)
    print("There must be something I can do...")
    sleep(0.5)
    print("There must be some thing I can make up with...")
    sleep(0.3)
    print("There must... There must... There must!")
    sleep(0.5)
    print("Suddenly I found a pen and paper in the corner, I dashed at them and begun scratching a small letter.")
    sleep(0.3)
    print("But...How will I guarantee that she'll find it...")
    sleep(0.5)
    print("Oh she will... She must... This garret is our secrete magic chamber after all.")
    sleep(0.8)
    print("...")
    sleep(0.8)
    print("...")
    sleep(0.8)
    print("Just when I finish writing the letter, a force was pulling me to go.")
    return
def garret(hand,cylinder_num,face):
    if hand!="ladder":
        print("The garret door was out of reach...")
        print("Perhaps I should take the ladder in my hands first...")
        return hand
    fl=0
    print("I Slowly opened the garret door and went in.")
    print("...")
    sleep(0.5)
    print("Whoa")
    sleep(0.5)
    print("Oh... All light was on... It's so bright comparing to the living room...")
    sleep(0.5)
    print("Ok... let me examine it...")
    sleep(0.5)
    print("I believe I am inside a room shaped like a rectangular pyramid...")
    sleep(0.5)
    print("... Oof...There was really not much room in here...")
    sleep(0.5)
    print("... There are four walls...")
    print("One is blue...")
    sleep(0.5)
    print("One is yellow...")
    sleep(0.5)
    print("One is red...")
    sleep(0.5)
    print("And... The last one is crystal")
    sleep(0.5)
    print("The colored walls seemed to have one little hole on each of them...")
    print("Under the holes wrote the same small words...")
    sleep(0.5)
    print("Umm...'c-y-l-i-n-d-e-r'... cylinder.")
    sleep(0.5)
    print("On the crystal wall was three key holes... there seemed to be numbers on it...")
    print("From left to right...")
    print("2100....0900....1700....")
    sleep(0.5)
    print("And... Umm...")
    sleep(0.5)
    print("Oh... a purple pole was in the middle to hold up the four walls.")
    print("... I think I should insert something into the holes...")
    ft=0
    while 1:
        print("What do I want do insert? (Keys/Cylinders)")
        move=input("> ")
        move=move.lower()
        if move=="keys":
            if crystal_wall[0]==1:
                print("The keys were already insert into the holes correctly...")
                continue
            print("I took out the keys with my hands...")
            print("2000....0900....1700")
            print("But in which order I should put them in? (1-wooden key  2-steel key  3-glass key)")
            code=input("> ")
            if not code.isdecimal():
                print("Please use arabic numerals. Leave out the blanks as well!")
                continue
            if code=="312":
                print("Click...")
                sleep(0.5)
                print("Click...")
                sleep(0.5)
                print("Click...")
                sleep(0.5)
                print("... Crack...Crack")
                sleep(0.5)
                print("the crystal wall was split in the middle and opened sideways...")
                sleep(0.5)
                print("I looked down...")
                sleep(0.5)
                print("Whoa... It's really high... I think I'll need to tie a rope to the pole and climb down...")
                crystal_wall[0]=1
                if "rope" in item_box:
                    print("I took the rope in hand and tied one end of it on the purple pole.")
                    if (clue[0]+clue[1]+clue[2]+clue[3])==6:
                        bonus()
                        ft=1
                        sleep(0.3)
                        print("But I know she'll stay strong and optimistic!")
                    print("Tightly as I grabbed the rope, I climbed slowly down on to the ground.")
                    print("The moment I touched the ground I suddenly felt light again...")
                    sleep(0.5)
                    print("So light that I felt relief and anticipation rising inside of me...")
                    sleep(0.5)
                    print("Perhaps I am on my next journey...")
                    sleep(0.5)
                    print("...")
                    sleep(0.5)
                    print("...")
                    sleep(0.5)
                    print("""*********************************************************************
******------Congratulations! You've successfully escaped!------******
*********************************************************************""")
                    if ft==0:
                        print("There is still a bonus story to get by collecting all the clues hidden!")
                        print("Feel free to try again to look for the bonus clues!")
                    elif ft==1:
                        print("Also, congratulations on finding all the hidden clues!")
                        print("Here's another hidden scene for you!!")
                        hidden_scene()
                        print("Hope you enjoyed the background stories!!!")
                    print("Loading",end='')
                    sleep(0.8)
                    print("...")
                    sleep(0.8)
                    print("Loading", end='')
                    sleep(0.8)
                    print("...")
                    sleep(0.8)
                    print("""****************************************************
*********------Thank you for playing!------*********
****************************************************""")
                    exit(0)
                else:
                    continue
            else:
                print("Urr...Do I need a Hint? (Y/N)")
                choice=input("> ")
                choice=pan_y_or_n(choice)
                if choice=='n':
                    print("Alright...")
                else:
                    print("To open the crystal wall")
                    print("I need to line the keys")
                    print("Maybe reflect on the past scenes")
                    print("Everything one can then see")
        elif move=="cylinders":
            if rope_yes[0]==1:
                print("I already inserted all cylinders into the right places...")
                continue
            if cylinder_num<2:
                print("Umm... I don't think I have enough cylinders...")
                sleep(0.5)
                print("Perhaps I should go down and find more...")
                sleep(0.5)
                print("... I climbed down the ladder and took it in my hands.")
                print(wall_nums_general[face])
                return hand
            else:
                print("I only have two cylinders in my hands now...")
                print("Which two colors will I choose? (Red/Blue/Yellow)--(IN A and B format)")
                lcolor=['red','blue','yellow']
                colors=input("> ")
                colors=colors.lower()
                if (" and " not in colors)|(len(colors.split(' '))!=3):
                    print("Please use the correct format---insert 'A and B' ")
                    continue
                pick=list(colors.split(" and "))
                fc=1
                for a in pick:
                    if a not in lcolor:
                        fc=0
                        print("I couldn't see a wall of such a color...")
                        sleep(0.4)
                        print("Perhaps I though wrong...")
                        break
                if fc==0: continue
                if ('red' in pick)&('blue' in pick):
                    print("Click...")
                    sleep(0.5)
                    print("Clunk...")
                    sleep(0.5)
                    print("Puff...")
                    sleep(0.5)
                    print("A rope dropped in front of me...")
                    print("I think I'd better pick it up...")
                    pick_up('rope')
                    rope_yes[0]=1
                    if crystal_wall[0]==0: continue
                    print("I took the rope in hand and tied one end of it on the purple pole.")
                    if (clue[0] + clue[1] + clue[2] + clue[3]) == 6:
                        bonus()
                        ft = 1
                        sleep(0.3)
                        print("But I know she'll stay strong and optimistic!")
                    print("Tightly as I grabbed the rope, I climbed slowly down on to the ground.")
                    print("The moment I touched the ground I suddenly felt light again...")
                    sleep(0.5)
                    print("So light that I felt relief and anticipation rising inside of me...")
                    sleep(0.5)
                    print("Perhaps I am on my next journey...")
                    sleep(0.5)
                    print("...")
                    sleep(0.5)
                    print("...")
                    sleep(0.5)
                    print("""*********************************************************************
******------Congratulations! You've successfully escaped!------******
*********************************************************************""")
                    if ft == 0:
                        print("There is still a bonus story to get by collecting all the clues hidden!")
                        print("Feel free to try again to look for the bonus clues!")
                    elif ft == 1:
                        print("Also, congratulations on finding all the hidden clues!")
                        print("Here's another hidden scene for you!!")
                        hidden_scene()
                        print("Hope you enjoyed the background stories!!!")
                    print("Loading", end='')
                    sleep(0.8)
                    print("...")
                    sleep(0.8)
                    print("Loading", end='')
                    sleep(0.8)
                    print("...")
                    sleep(0.8)
                    print("""****************************************************
*********------Thank you for playing!------*********
****************************************************""")
                    exit(0)
                else:
                    print("...")
                    sleep(0.4)
                    print("Nothing happened...")
                    continue
        else:
            print("...?")
            sleep(0.5)
            print("I don't think that's a necessary move...")
    return hand

# Items-----------------------------------------------------------------------------------------------------------------Items

def turn(ins, face):
    if ins == 'left':
        face += 1
    elif ins == 'right':
        face -= 1
    elif ins == 'around':
        face -= 2
    else:
        print("It's not a valid move, I must have thought wrong...")
        return face

    if face > 4:
        face -= 4
    elif face < 1:
        face += 4

    if face in wall_nums_new:
        print(wall_nums_new[face])
        wall_nums_new.pop(face)
    else:
        print(wall_nums_general[face])
    return face


def look_up(photo_piece):
    print("I think I want to check the ceiling...")
    sleep(0.5)
    if ceil_light1[0] == 0:
        print("In the middle is a multi-layered crystal ceiling light, and a closed garret door in a corner.")
    else:
        print("In the middle, the multi-layered crystal ceiling light dazzles brightly. A closed garret door was in a corner.")
        if ceil_light1[1]==0:
            print("Something seemed to be dangling on the, rather low, layer of the light...")
            sleep(0.5)
            print("I jumped to reach it.")
            sleep(0.5)
            print("It seemed like a photo piece... I think I'll put it in my item box.")
            pick_up("photo piece")
            photo_piece+=1
            ceil_light1[1]=1
    print("I finished checking and stopped looking at the ceiling.")
    return photo_piece


#facings--------------------------------------------------------------------------------------------------------------------


def enter(time,p_or_i, face, hand, already_mend, photo_piece, cylinder_num):
    if face == 1:
        if p_or_i == "tv set":
            hand = tvset(time, hand)
        elif p_or_i == 'cabinet':
            hand, already_mend, photo_piece, cylinder_num,time = cabinet1(hand, already_mend, photo_piece, cylinder_num, face, time)
    elif face == 2:
        if p_or_i == 'curtain':
            if time==3:
                print("It seemed that my hands run right through it...")
            else:
                print("Already opened, nothing's special about it.")
                print("I stepped back from the curtain.")
        elif p_or_i == 'sash':
            sash(time,hand)
    elif face == 3:
        if p_or_i == "case":
            hand,cylinder_num = case3(time,hand,cylinder_num)
        elif p_or_i == "cabinet":
            hand = cabinet3(hand)
        elif p_or_i == "switch":
            switch(ceil_light1)
    elif face == 4:
        if p_or_i == "front door":
            hand = frontdoor(hand)
        elif p_or_i=="rug":
            hand, photo_piece=welcomerug(time, hand, photo_piece)
        elif p_or_i=="basement door":
            hand = basement(hand) 
    return hand, already_mend, photo_piece,cylinder_num,time

def go_to(time,p_or_i, face, hand, already_mend, photo_piece, cylinder_num):
    print(f"Approaching {p_or_i}...")
    sleep(0.5)
    hand, already_mend, photo_piece,cylinder_num,time = enter(time,p_or_i, face, hand, already_mend, photo_piece,cylinder_num)
    return hand, already_mend, photo_piece,cylinder_num,time
#goto
# def portable_items(item):

# def unportable_items():

def main():
    setting()
    photo_piece = 0
    already_mend = 0
    cylinder_num = 0
    curtain = 0
    facing = 2
    wrong1 = 0
    wrong2 = 0
    time=1
    hand = "my hands"
    # init--------------------------------------------------------------------------------------------------------------------------init
    welcome_pack()
    morning_scene()
    while 1:
        move = input("> ")
        move = move.lower()
        check_help(move)
        check_quit(move)
        num_noun=check_noun(move)
        if num_noun!=1: continue
        if move == 'go back':
            print("I am already in the very beginning scene.")
            continue
        if curtain == 0:
            if ("go to" in move) & ("curtain" in move):
                print("I now can reach the curtain to open it")
                fl = 0
                while 1:
                    move = input("> ")
                    move = move.lower()
                    check_help(move)
                    check_quit(move)
                    if move == "go back":
                        if fl == 0:
                            print("Really? Shouldn't I open the curtain first?")
                            fl = 1
                            continue
                        print("I stepped back from the curtain.")
                    elif ("open" in move) | ("draw" in move):
                        if "curtain" in move:
                            curtain = 1
                            print("The instance I drew open the curtain, ")
                            print("morning sun lit up the whole room with a rather cold glow.")
                            print("In front of me now is a closed sash.")
                            print("In sight was a grass field and a winded path into the shady woods.")
                            print("I wondered what the room would look like, so I backed away from the sash and begun my examine.")
                            sleep(0.5)
                            print("...")
                            sleep(0.8)
                            print("I think I am inside a living room...")
                            sleep(0.8)
                            print("There's a dining table in the middle...")
                            sleep(0.5)
                            print("... I finished examine the room and turned to face the wall with the sash and the curtain")
                            break
                        else:
                            print("I could see nothing but the curtain...")
                            print("What should I do next?")
                    else:
                        print("... ... ?")
            elif ("curtain" in move) & ("go to" not in move):
                num_vb = check_vb(move)
                if num_vb != 1: continue
                print("I cannot reach the curtain. Perhaps I should go closer to it.")
            else:
                print("It's pitch black.")
                print("I cannot do anything in this kind of darkness.")
        elif move == "check the item box":
            print(','.join(item_box))
        elif (len(list(move.split())) == 2) & ('turn' in move):
            move = list(move.split())
            facing = turn(move[1], facing)
        elif move == 'look up':
            photo_piece=look_up(photo_piece)
        elif (('smash' in move)|('eat' in move)|("kill" in move)|("touch" in move)|("feel" in move)|("slap" in move)|("hit" in move)&("white" not in move))&("bug" in move):
            print("Urr... It seemed that I can't touch it!")
            clue[0]=1
        elif "go to" in move:
            words = nltk.word_tokenize(move)
            tag = nltk.pos_tag(words)
            tmp = []
            for tup in tag:
                if "NN" in tup:
                    tmp.append(tup[0])
            if len(tmp) == 0:
                print("What or where? I can't understand my mind...")
                if wrong1 <= 5:
                    print(f"Detected part of speech: {tag}.")
                    print("Hint: When a noun failed to be detected, try to add a adjective, pronoun, or article before it.")
                    print("      When multiple nouns detected, avoid nouns about general locations.(e.g. wall)")
                    print("      Also, check if the grammar is correct")
                    wrong1 += 1
                sleep(0.5)
            elif len(tmp) > 2:
                print("Whoa, I can only focus on one thing at a time.")
            else:
                tmp = ' '.join(tmp)
                if tmp == 'dining table':
                    time, hand=diningtable(time, facing, hand)
                elif tmp == "table":
                    print("I need to specify which table...")
                    print("The dining table perhaps...?")
                elif tmp == 'bug':
                    if time>=2:
                        print("I checked every corner, but there's no bug in the room anymore.")
                        print("Perhaps they flew away sometime earlier...")
                        continue
                    che = 0
                    for tup in tag:
                        if "JJ" in tup: che+=1
                    if che == 0:
                        print("What kind of bug am I looking for?")
                    elif che>=2:
                        print("I believe I can only see one bug right now...")
                    else:
                        if (facing == 1) & ("red" in move):
                            bugs("red")
                        elif (facing == 3) & ("green" in move):
                            bugs("green")
                        elif (facing == 4) & ("white" in move):
                            bugs("white")
                        else:
                            print("No such bug in sight.")
                elif tmp == 'door':
                    if "garret" in move:
                        garret(hand, cylinder_num, facing)
                    else: print("I need to decide which specific door would I go to.")
                elif (tmp == "light") | (tmp == "ceiling light"):
                    print("...I don't think I can do that...")
                else:
                    if tmp not in main_room_sight[facing]:
                        print(f"I cannot see any {tmp} in sight.")
                        if wrong2 <= 5:
                            print(f"Detected part of speech: {tag}.")
                            print("Hint: When a noun failed to be detected, try to add a adjective, pronoun, or article before it.")
                            print("      When multiple nouns detected, avoid nouns about general locations.(e.g. wall)")
                            print("      Also, check if the grammar is correct")
                            wrong2 += 1
                    else:
                        hand, already_mend, photo_piece,cylinder_num,time = go_to(time, tmp, facing, hand, already_mend, photo_piece, cylinder_num)
        elif move == "check the item box":
            print(','.join(item_box))
        elif ("take" in move) & ("in hand" in move):
            tag = nltk.pos_tag(move.split())
            tmp = []
            for tup in tag:
                if (("NN" in tup)|("NNS" in tup)) & ("hand" not in tup)&("hands" not in tup): tmp.append(tup[0])
            if len(tmp) == 0:
                print("I need to choose something to take.")
                print(f"Detected part of speech: {tag}.")
                print("Hint: When a noun failed to be detected,")
                print("try to add a adjective, pronoun, or article before it.")
                print("      Also, check if the grammar is correct.")
            elif len(tmp) > 2:
                print("I can only hold one item at a time.")
                print(f"Detected part of speech: {tag}.")
                print("Hint: When an unexpected noun is detected,")
                print("try to reduce nouns about general locations(eg. walls).")
                print("      Also, check if the grammar is correct.")
            else:
                tmp = ' '.join(tmp)
                hand=use_item(hand, tmp)
        else:
            print("I can't reach anything right now...")
            print("Perhaps I should go closer to them...")
    return

main()
