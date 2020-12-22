from classes import Character, Location, Item
from subprocess import call
import os
import time
os.system('cls' if os.name == 'nt' else 'clear')
from pygame import mixer
# Liz's Room
#print("You are in Liz Carley room. Take a\n look around, but don't take\n too long, it will look suspicious if she\n catches you.")


# # Elevator
#print("You are in the elevator. This gives you access to anywhere in the building")

# # Roof
# print("You are on the roof.\n Its a stormy evening and walking around dripping\n water might draw a few eyes.\n Better hurry and gather supplies")

# Kitchen
#print("You are in the kitchen.\n This is the busiest room in the building.\n You should do what you need to do quickly.")

# # Gym
#print("You are in the gym.\n Its pretty hot in here. Sweating might\n not be the best idea today, I wouldnt\n take too long in here")

# Parking Garage
#print("CONGRATULATIONS\n\n The body is in the car are you got away with MURDER\n\n now what????????")

# Community Center
#print("You are in the community center.\n Its a lot of cameras in here!")

        # We need some info here about the game....so you know what character you want to choose, must use items in Josh's room!
        #'''
        #Please choose a player
        #Crystal starts with alert level of 40. Resourceful. Power: She can move to any room without the elevator.
        #Jojo starts with alert level of 10. Sneaky. Power: She can carry 1 extra item.
        #Kurtis starts with alert level of 30. Detail oriented. Power: After #, his alert level penalty is decreased by half points.
        #Joshua starts with alert level of 5. Obsessive compulsive. Power: Doesn't leave a mess
        #'''
        # Here we need to set the scene!
        #first time instructions count 
        #print("Welcome to 'How To Get Away With MURDER!'\n #active_player.name has just woke up in a small room\n in the Atlanta Tech Village with a dead body\n on the floor #(keeping vague)with all evidence pointing to them.\n Looking around, it doesn't look like anyone has\n noticed yet.active_player.name has dreams of being a top notch programmer\n and know that noone will believe they\n weren't the murderer, in fact\n active_player.name isn't even sure they didn't do it.\n Help active_player.name get away with this murder\n so one day their programming dreams can be achieved.\n Navigate through the school and gather items\n that will help escape pas the guard\n with the body to\n make it to the parking lot.\n But beware -- everything you \n find will not be helpful and dont leave \n too much evidence around or you\n may be discovered. Once you feel\n your you won't attract too much attention(alert level), try\n to sneak past the security desk and out the\n door. GOOD LUCK!\n\n\nTIPS:\n You must bring picked up items back to the murder room to use\nCarrying to many items at once will raise your alert level  ")
        #description 
        #print("You are in your first room, the 'MURDER ROOM'")





# this is our main program


# Character Instantiation
crystal = Character('Crystal', 40, "Crystal starts with alert level of 40. Resourceful. Power: She can move to any room without the elevator.")
jojo = Character('JoJo', 10, "Jojo starts with alert level of 10. Sneaky. Power: She can carry 1 extra item.")
kurtis = Character('Kurtis', 30, "Kurtis starts with alert level of 30. Detail oriented. Power: After 80, his alert level penalty is decreased by half points.")
joshua = Character('Joshua', 5, "Joshua starts with alert level of 5. Obsessive compulsive. Power: Doesn't leave a mess")
annalise = Character('Annalise Keating', 0, "No mistakes!")
main_players = [crystal, jojo, kurtis, joshua]

# Location Instantiation
josh_room = Location("Sean's hide-out", "You are in your first room, the 'MURDER ROOM'")
liz_office = Location("Liz's Office", "You are in Liz Carley room. Take a\n look around, but don't take\n too long, it will look suspicious if she\n catches you.")
elevator = Location("Elevator", "You are in the elevator. This gives you access to anywhere in the building")
roof = Location("Roof", "You are on the roof.\n Its a stormy evening and walking around dripping\n water might draw a few eyes.\n Better hurry and gather supplies")
kitchen = Location("Kitchen", "You are in the kitchen.\n This is the busiest room in the building.\n You should do what you need to do quickly.")
gym = Location("Gym", "You are in the gym.\n Its pretty hot in here. Sweating might\n not be the best idea today, I wouldnt\n take too long in here")
security_desk = Location("Security Desk", "security desk description")
parking_garage = Location("Parking Garage", "parking garage description")
community_center = Location("Community Center", "You are in the community center.\n Its a lot of cameras in here!")
location_keys = {
    josh_room: [liz_office, kitchen, elevator],
    liz_office: [josh_room, kitchen, elevator],
    kitchen: [liz_office, josh_room, elevator],
    elevator: [liz_office, josh_room, kitchen, roof, community_center, gym],
    roof: [elevator],
    community_center: [elevator],
    gym: [elevator]
}


# Items Instantiation
# Josh's Room
monitor = Item("monitor", josh_room, "pass", False, 10)
jacket = Item("jacket", josh_room, "shirt", False, -10)
bag_of_chips = Item("bag of chips", josh_room, "pass", "pass", 5)
items_josh_room = [monitor, jacket, bag_of_chips]

# Liz's Room
tshirt = Item("t-shirt", liz_office, "shirt", False, -10)
# input code in book and if you can solve unlocks ryan phone number and he distracts security guard for you
book = Item("book", liz_office, "pass", "pass")
keyboard = Item("keyboard", liz_office, "pass", "pass", 0, 15)
items_liz_office = [tshirt, book, keyboard]

# # Elevator
key_card = Item("Dropped Key Card", elevator, "pass", "pass")
trash_can = Item("Trash Can", elevator, "pass", "pass", 0, -10)
items_elevator = [key_card, trash_can]

# # Roof
tarp = Item("tarp", roof, "pass", "pass", 0, -15)
chair = Item("chair", roof, "pass", False, 15)
firepit = Item("firepit", roof, "pass", False, 10)
items_roof = [tarp, chair, firepit]

# Kitchen
sink = Item("sink", kitchen, "hands", False,  -10)
bleach = Item("bleach", kitchen, "hands", "pass", 0, -10)
freezer = Item("freezer", kitchen, "pass", False)
items_kitchen = [sink, bleach, freezer]

# # Gym
shower = Item("shower", gym, "hands", False, -5)
shower_curtain = Item("shower_curtain", gym, "pass", "pass", 0, -5)
weights = Item("weights", gym, "pass", "pass", 0, 15)
items_gym = [shower, shower_curtain, weights]

# # Security Desk
security_desk = Item("security desk", security_desk, "pass", "pass")
items_security_desk = [security_desk]

# Parking Garage
get_away_car = Item("Brittani in the get away car",
                    parking_garage, "pass", "pass", -100)
items_parking_garage = [get_away_car]

# Community Center
arcade_game = Item("Arcade Game", community_center, "pass", "pass")
pillows = Item("Pillow", community_center, "pass", False, 10)
ping_pong = Item("Ping Pong", community_center, "pass", False, 5)
rug = Item("Rug", community_center, "pass", "pass", 0, -5)
blankets = Item("Blanket", community_center, "pass", "pass", 0, -15)
items_community_center = [arcade_game,
                          pillows, ping_pong, rug, blankets]

all_items = [monitor, jacket, bag_of_chips, tshirt, book, keyboard, key_card, trash_can, tarp, chair, firepit, sink, bleach,
             freezer, shower, shower_curtain, weights, security_desk, get_away_car, arcade_game, pillows, ping_pong, rug, blankets]

# Menus

main_menu = ["Search for anything useful", "Look at my items",
             "Move to a new location", "Call the Police"]

elevator_only_menu = ["Search for anything useful", "Look at my items",
             "Go to the Elevator", "Call the Police"]

item_use_menu = ["Use item", "Get rid of an item", "exit"]

josh_room_menu = ["Search for anything useful", "Look at my items", "Move to a new location",
                  "Call the Police", "Attempt to Escape with the body"]

josh_room_menu_with_code = ["Search for anything useful", "Look at my items", "Move to a new location",
                            "Attempt to Escape with the body", "Call the Police", "Attempt to Escape with the body", "***Call Ryan***"]


# Functions

def choosing_active_player():
    print()  # Add in player stats and special characteristics
    print_menu(main_players)
    active_player = True
    while active_player == True:
        choosing_player = input("Please pick a player: ")
        if choosing_player == "1":
            active_player = crystal
        if choosing_player == "2":
            active_player = jojo  
        if choosing_player == "3":
            active_player = kurtis    
        if choosing_player == "4":
            active_player = joshua      
        if choosing_player == "1000":
            active_player = annalise
        else:
            print("Please choose provided options: ")
    print(active_player)
    return active_player


def print_string_menu(menu):
    for idx, choice in enumerate(menu):
        print(f"{idx+1}. {choice}")


def print_menu(menu):
    for idx, choice in enumerate(menu):
        # print(type(choice))
        print(f"{idx+1}. {choice.name}")


def print_location_options(location_options):
    location_name_list = []
    for location in location_options:
        location_name_list.append(location)
    for idx, choice in enumerate(location_name_list):
        print(f"{idx+1}. {choice.name}")




def which_list(room):
    if room == josh_room:
        return items_josh_room
    if room == liz_office:
        return items_liz_office
    if room == elevator:
        return items_elevator
    if room == roof:
        return items_roof
    if room == kitchen:
        return items_kitchen
    if room == gym:
        return items_gym
    if room == security_desk:
        return items_security_desk
    if room == parking_garage:
        return items_parking_garage
    if room == community_center:
        return items_community_center


def remove_item_from_inventory(player):
    print_menu(player.items)
    while True:
        try:
            full_menu_remove_choice = int(
            input("Which item would you like to remove?"))
            if full_menu_remove_choice <= len(player.items):
                break
            else:
                print("That is not an option. ")
        except ValueError:
            print("That is not an option, please choose provided options: ")
    player.items.pop(full_menu_remove_choice - 1)
    print("Your item has been removed")


def main_menu_choice_1(list_option, player):
    item_loop = True
    play_game = True
    while item_loop:
        print_menu(list_option)
        if len(player.items) >= 5:
            while True:
                full_menu_choice = (input(
                    "You are already holding the maximum number of items. Would you like to remove one? y or n:  "))
                if full_menu_choice.lower() == "y":
                    remove_item_from_inventory(player)
                    break
                elif full_menu_choice == "n":
                    break
                # incorrect responce error catch
                else:
                    print("\nThat is not a valid option, try again:")
                    
        else:
            try:
                item_chosen = int(input(
                    "Which item would you like to pick up?\nNote: To exit, press 9.\nPlease choose: "))
                if item_chosen == 9:
                    item_loop = False
                elif item_chosen > len(list_option):
                    print("\nThat is not an option, try again:")
                else:
                    choice_item = list_option[item_chosen-1]
                    play_game = player.add_items(choice_item)
                    print(choice_item)
                    player.alert_banner()
                    #player.print_alert_status()
                    list_option.pop(item_chosen-1)
                    continue_choosing = input(
                        "Would you like to choose another item? y or n\n")
                    if continue_choosing.lower() == "y":
                        pass
                    elif continue_choosing.lower() == "n":
                        os.system('cls||clear')
                        item_loop = False
                    else:
                        print("That isn't an option. Please choose 'y' or 'n': ")
            except ValueError:
                print("Please choose an available menu choice!")
    return play_game


def main_menu_choice_2(location, player, list_option):
    play_game = True
    if len(player.items) > 0:
        print_menu(player.items)
    else:
        print("\n**You have no items in your inventory.**")
        return play_game
    if location == josh_room:
        print_string_menu(list_option)
        while True:
            try:
                choice_item_use_menu = int(input("Please choose: "))
                if choice_item_use_menu == 1:
                    print_menu(player.items)
                    while True:
                        try:
                            user_choice = int(input("Choose which item to use:")) 
                            if user_choice <= len(player.items):
                                item_being_used = player.items[user_choice-1]
                                play_game = player.item_used(item_being_used)
                                return play_game
                            else:
                                print("That is not a valid choice! Try again.")
                        except ValueError:
                            print("That is not an option. Please try again.")
                if choice_item_use_menu == 2:
                    remove_item_from_inventory(player)
                    break
                if choice_item_use_menu == 3:
                    break
                else:
                    print("Please choose an available menu choice")
            except ValueError:
                print("Please choose an available menu choice")
    return play_game


def main_menu_choice_3(location):
    location_list = []
    if len(location_keys[location]) == 1 and location_keys[location][0] == elevator:
        new_location = elevator
        print("\n\n***You must take the elevator to your next location.***")
    else:
        for location in location_keys[location]:
            location_list.append(location)
        print("Where would you like to go?")
        print_location_options(location_list)
        while True:
            try:
                location_choice = int(input("Please choose: "))
                if location_choice <= len(location_list):
                    new_location = location_list[location_choice - 1]
                    break
                else:
                    print("That is not a valid choice. Please try again.")
            except ValueError:
                print("That is not a valid choice. Please try again.")
    return new_location

def main_menu_choice_5(location, player):
    os.system('cls||clear')
    print("You are trying to escape! Good luck.\nRememeber, if your alert level is too high, you will get caught!\nIt's time to sneak down to the lobby. You gather up the body and head down the hall. Hopefully, no one catches you!\n*-----")
    player.walking_the_hallway()
    if player.alert_level < 90 and player.hands[1] == False and player.shirt[1] == False:
        while True:
            escape_input = input("You made it to the elevator! Please press 1 to go down to the garage.\nHopefully, no one joins you in the elevator!")
            if player.alert_level < 75 and escape_input == "1":
                player.elevator_going_down()
                print("You made it to the garage level without getting caught! Now you must sneak past the security guard! Good luck!")
                while True:
                    try:
                        escape_input = int(input("Press 1 to sneak and 2 to act casual."))
                        if escape_input > 2:
                            print("That isn't a choice! Choose a valid option quickly so you can escape!!!")
                        elif player.alert_level < 60 and escape_input == 1:
                            player.sneak_past_security()
                            player.garage_scene()
                            return False
                        elif player.alert_level < 50 and escape_input == 2:
                            player.casual_past_security()
                            player.garage_scene()
                            return False
                        else:
                            player.losing_statement()
                            return False
                    except ValueError:
                        print("C'mon! Pick an option! You are running out of time!")
            elif player.alert_level < 75:
                print("That isn't an option! Not when you have a body to move.\nYou need to choose the first floor quickly before someone jumps on the elevator with you!")
            else:
                player.losing_statement()
                return False
    else:
        player.losing_statement()
    return False

def play_game():
    continue_playing = True
    while continue_playing:
        os.system('cls||clear')
        print()# Here we can have a graphic for our game...
        # We need some info here about the game....so you know what character you want to choose, must use items in Josh's room!
        print('''
*****Player Characteristics******
Crystal starts with alert level of 40. Resourceful. Power: She can move to any room without the elevator.

Jojo starts with alert level of 10. Sneaky. Power: She can carry 1 extra item.

Kurtis starts with alert level of 30. Detail oriented. Power: After 80, his alert level penalty is decreased by half points.

Joshua starts with alert level of 5. Obsessive compulsive. Power: Doesn't leave a mess
        ''')  # Add in player stats and special characteristics
        active_player = choosing_active_player()
        welcome_message = f"Welcome to 'How To Get Away With MURDER!'\n\n{active_player.name} has just woke up in a small room \nin the Atlanta Tech Village with a dead body on the \nfloor, bloody clothes and hands with all evidence pointing \nto them.Looking around, it doesn't look like anyone \nhas noticed yet.{active_player.name} has dreams of being a top notch \nprogrammer and know that noone will believe they weren't \nthe murderer, in fact {active_player.name} isn't even sure they \ndidn't do it.Help {active_player.name} get away with this \nmurder so one day their programming dreams can be achieved. \nNavigate through the school and gather items that will help \nescape past the guard with the body to make it to the parking lot. \nBut beware -- everything you find will not be helpful and dont leave too much evidence around or you may be discovered. \nOnce you feel your you won't attract too much attention(alert level), try \nto sneak past the security desk and out of the door. GOOD LUCK! \nTIPS: \nYou must bring picked up items back to the murder room to use them. \nCarrying too many items at once will raise your alert level."
        print(welcome_message)
        curr_location = josh_room
        code_unlocked = False
        play_game = True
        hands = "dirty"
        shirt = "dirty"
        continue_on = input("Press enter to continue: ")
        while play_game:
            os.system('cls||clear')
            print(curr_location)
            curr_items_list = which_list(curr_location)
            same_location = True
            while same_location:
                active_player.alert_banner()
                #active_player.print_alert_status()
                print("What would you like to do now?")
                elevator_only = False
                if len(location_keys[curr_location]) == 1 and location_keys[curr_location][0] == elevator:
                    elevator_only = True
                    print_string_menu(elevator_only_menu)
                elif curr_location == josh_room:
                    print_string_menu(josh_room_menu)
                elif code_unlocked == True:
                    print_string_menu(josh_room_menu_with_code)
                else:
                    print_string_menu(main_menu)
                main_menu_choice = input("Please choose: ")
                if main_menu_choice == "1":
                    play_game = main_menu_choice_1(curr_items_list, active_player)
                if main_menu_choice == "2":
                    play_game = main_menu_choice_2(curr_location, active_player, item_use_menu)
                if main_menu_choice == "3":  # Move to a new location
                    curr_location = main_menu_choice_3(curr_location)
                    same_location = False
                if main_menu_choice == "4":
                    play_game = False
                if main_menu_choice == "5":
                    play_game = main_menu_choice_5(curr_location, active_player)
                    same_location = False
                else:
                    print("That is not a good idea, let's choose a valid option this time, silly!")
        play_again = input("Would you like to play again? 'y' or 'n': ")
        if play_again.lower() == 'y':
            continue_playing = True
        elif play_again.lower() == 'n':
            continue_playing = False
        else:
            print("That isn't a choice! Please choose a valid option.")




play_game()
