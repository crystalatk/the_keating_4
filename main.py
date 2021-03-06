from pygame import mixer
from classes import Character, Location, Item
from arcade import tic_tac_toe, number_guess
from ascii_art import welcome_message, arcade_screen, game_start_graphic, caught_graphic, get_away_graphic, win_graphic, guess_number_graphic, casual_past_security, elevator_going_down, sneak_past_security, walking_the_hallway
from subprocess import call
import os
import time
os.system('cls' if os.name == 'nt' else 'clear')
mixer.init()

# Music


def sound(file):
    sound = mixer.Sound(f"audio/{file}")
    return mixer.Sound.play(sound)


# this is our main program

# Character Instantiation
crystal = Character('Crystal', 40, "she", "her",
                    "Crystal starts with alert level of 40. Resourceful. Power: She can move to any room without the elevator.")
jojo = Character('JoJo', 10, "she", "her",
                 "JoJo starts with alert level of 10. Sneaky. Power: She can carry 1 extra item.")
kurtis = Character('Kurtis', 30, "he", "his",
                   "Kurtis starts with alert level of 30. Detail oriented. Power: After 80, his alert level penalty is decreased by half points.")
joshua = Character('Joshua', 5, "he", "his",
                   "Joshua starts with alert level of 5. Obsessive compulsive. Power: Doesn't leave a mess")
annalise = Character('Annalise Keating', 0, "she", "her", "No mistakes!")
main_players = [crystal, jojo, kurtis, joshua]

# Location Instantiation
josh_room = Location(
    "Sean's hide-out", "\nYou are in your first room, the 'MURDER ROOM'.")
liz_office = Location(
    "Liz's Office", "\nTake a look around, but don't take too long, it will look suspicious if she catches you.")
elevator = Location(
    "Elevator", "\nThis gives you access to anywhere in the building.")
roof = Location(
    "Roof", "\nIt's a stormy evening and walking around dripping water might draw a few eyes. Better hurry and gather supplies.")
kitchen = Location(
    "Kitchen", "\nThis is the busiest room in the building. You should do what you need to do quickly.")
gym = Location(
    "Gym", "\nIt's pretty hot in here. Sweating might not be the best idea today, I wouldn't take too long in here.")
security_desk = Location("Security Desk", "security desk description")
parking_garage = Location("Parking Garage", "parking garage description")
community_center = Location(
    "Community Center", "\nYou are in the community center. Its a lot of cameras in here!")
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
monitor = Item("monitor", josh_room, "pass", False, 40)
jacket = Item("jacket", josh_room, "shirt", False, -25)
bag_of_chips = Item("bag of chips", josh_room, "pass", "pass", 35)
items_josh_room = [monitor, jacket, bag_of_chips]

# Liz's Room
tshirt = Item("t-shirt", liz_office, "shirt", False, -20)
# input code in book and if you can solve unlocks ryan phone number and he distracts security guard for you
book = Item("book", liz_office, "pass", "pass")
keyboard = Item("keyboard", liz_office, "pass", "pass", 20)
items_liz_office = [tshirt, book, keyboard]

# # Elevator
key_card = Item("Dropped Key Card", elevator, "pass", "pass")
trash_can = Item("Trash Can", elevator, "pass", "pass", 0, -10)
items_elevator = [key_card, trash_can]

# # Roof
tarp = Item("tarp", roof, "pass", "pass", 0, -25)
chair = Item("chair", roof, "pass", False, 20)
firepit = Item("firepit", roof, "pass", False, 20)
items_roof = [tarp, chair, firepit]

# Kitchen
sink = Item("sink", kitchen, "hands", False,  -15)
bleach = Item("bleach", kitchen, "hands", "pass", 0, -10)
freezer = Item("freezer", kitchen, "pass", False)
items_kitchen = [sink, bleach, freezer]

# # Gym
shower = Item("shower", gym, "hands", False, -5)
shower_curtain = Item("shower curtain", gym, "pass", "pass", 0, -5)
weights = Item("weights", gym, "pass", "pass", 0, 35)
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
pillows = Item("Pillow", community_center, "pass", False, 15)
ping_pong = Item("Ping Pong", community_center, "pass", False, 10)
rug = Item("Rug", community_center, "pass", "pass", 0, -5)
blankets = Item("Blanket", community_center, "pass", "pass", 0, -15)
items_community_center = [arcade_game,
                          pillows, ping_pong, rug, blankets]

all_items = [monitor, jacket, bag_of_chips, tshirt, book, keyboard, key_card, trash_can, tarp, chair, firepit, sink, bleach,
             freezer, shower, shower_curtain, weights, security_desk, get_away_car, arcade_game, pillows, ping_pong, rug, blankets]

# Variables


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

arcade_menu = ["tic-tac-toe", "guess my number", "EXIT"]


# Functions
def error_statement():
    print("\nThat is not a valid option, try again:")


def choosing_active_player():
    print()  # Add in player stats and special characteristics
    print_menu(main_players)
    active_player = True
    while active_player == True:
        choosing_player = input("Please pick a player: ")
        if choosing_player == "1":
            active_player = crystal
        elif choosing_player == "2":
            active_player = jojo
        elif choosing_player == "3":
            active_player = kurtis
        elif choosing_player == "4":
            active_player = joshua
        elif choosing_player == "1000":
            active_player = annalise
        else:
            error_statement()
    os.system('cls||clear')
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
                error_statement()
        except ValueError:
            error_statement()
    player.items.pop(full_menu_remove_choice - 1)
    print("Your item has been removed")


def play_arcade_game():
    os.system('cls||clear')
    while True:
        arcade_screen()
        print("What would you like to play?")
        print_string_menu(arcade_menu)
        try:
            game_choice = int(input("Please choose: "))
            if game_choice > 3:
                error_statement()
                time.sleep(3)
                os.system('cls||clear')
            elif game_choice == 1:
                tic_tac_toe()
            elif game_choice == 2:
                number_guess()
            elif game_choice == 3:
                os.system('cls||clear')
                return True
        except ValueError:
            error_statement()
            time.sleep(3)
            os.system('cls||clear')


def print_main_menu(curr_loc, code):
    if len(location_keys[curr_loc]) == 1 and location_keys[curr_loc][0] == elevator:
        print_string_menu(elevator_only_menu)
    elif curr_loc == josh_room:
        print_string_menu(josh_room_menu)
    elif code == True:  # This doesn't seem like it is in the right order. Fix these options...
        print_string_menu(josh_room_menu_with_code)
    else:
        print_string_menu(main_menu)


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
                    item_loop = False
                    break
                # incorrect responce error catch
                else:
                    error_statement()
        elif len(list_option) == 0:
            print("\nThere are no items left in this room")
            item_loop = False
        else:
            try:
                item_chosen = int(input(
                    f"Which item would you like {player.name} to pick up or use?\nNote: To exit, press 9.\nPlease choose: "))
                if item_chosen == 9:
                    item_loop = False
                elif item_chosen > len(list_option):
                    error_statement()
                else:
                    choice_item = list_option[item_chosen-1]
                    if choice_item == arcade_game:
                        play_game = play_arcade_game()
                        return play_game
                    play_game = player.add_items(choice_item)
                    print(choice_item)
                    player.alert_banner()
                    # player.print_alert_status()
                    list_option.pop(item_chosen-1)
                    if len(list_option) > 0:
                        continue_choosing = input(
                            "Would you like to choose another item? y or n\n")
                        if continue_choosing.lower() == "y":
                            pass
                        elif continue_choosing.lower() == "n":
                            os.system('cls||clear')
                            item_loop = False
                        else:
                            error_statement()
            except ValueError:
                error_statement()
    return play_game


def main_menu_choice_2(location, player, list_option):
    play_game = True
    if len(player.items) > 0:
        print_menu(player.items)
        user_input = input("Press ENTER to continue")
    else:
        print("\n**You have no items in your inventory.**\n")
        return play_game
    if user_input == "041221":
        print("You have unlocked the secret line to Ryan!\nNo worries, Ryan knows how to get rid of a body.\nYou can continue practicing your programming...\n\n\n*****GAME OVER*****")
        win_graphic()
        play_game = "fart"
    elif location == josh_room:
        print_string_menu(list_option)
        while True:
            try:
                choice_item_use_menu = int(input("Please choose: "))
                if choice_item_use_menu == 1:
                    print_menu(player.items)
                    while True:
                        try:
                            user_choice = int(
                                input("Choose which item to use:"))
                            if user_choice <= len(player.items):
                                item_being_used = player.items[user_choice-1]
                                play_game = player.item_used(item_being_used)
                                return play_game
                            else:
                                error_statement()
                        except ValueError:
                            error_statement()
                if choice_item_use_menu == 2:
                    remove_item_from_inventory(player)
                    break
                if choice_item_use_menu == 3:
                    break
                else:
                    error_statement()
            except ValueError:
                error_statement()
    return play_game


def main_menu_choice_3(location, player):
    location_list = []
    if len(location_keys[location]) == 1 and location_keys[location][0] == elevator:
        new_location = elevator
        print("\n\n***You must take the elevator to your next location.***")
    else:
        for loc in location_keys[location]:
            location_list.append(loc)
        print("Where would you like to go?")
        print_location_options(location_list)
        while True:
            try:
                location_choice = int(input("Please choose: "))
                if location_choice <= len(location_list):
                    new_location = location_list[location_choice - 1]
                    if location == elevator:
                        elevator_going_down()
                    else:
                        sound("footsteps.wav")
                        print("\n\nWalking.....")
                    break
                else:
                    error_statement()
            except ValueError:
                error_statement()
    return new_location


def main_menu_choice_5(location, player):
    os.system('cls||clear')
    print("You are trying to escape! Good luck.\nRememeber, if your alert level is too high, you will get caught!\nIt's time to sneak down to the lobby. You gather up the body and head down the hall. Hopefully, no one catches you!\n*-----")
    walking_the_hallway()
    if player.alert_level < 90 and player.hands[1] == False and player.shirt[1] == False:
        while True:
            escape_input = input(
                "You made it to the elevator! Please press 1 to go down to the garage.\nHopefully, no one joins you in the elevator!")
            if player.alert_level < 75 and escape_input == "1":
                elevator_going_down()
                print(
                    "You made it to the garage level without getting caught! Now you must sneak past the security guard! Good luck!")
                while True:
                    try:
                        escape_input = int(
                            input("Press 1 to sneak and 2 to act casual."))
                        if escape_input > 2:
                            error_statement()
                        elif player.alert_level < 60 and escape_input == 1:
                            sneak_past_security()
                            player.garage_scene()
                            return False
                        elif player.alert_level < 50 and escape_input == 2:
                            casual_past_security()
                            player.garage_scene()
                            return False
                        else:
                            player.losing_statement()
                            return False
                    except ValueError:
                        error_statement()
            elif player.alert_level < 75:
                error_statement()
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
        game_start_graphic()
        print("*****Player Characteristics******")
        for player in main_players:
            print(player.ability)
        active_player = choosing_active_player()
        sound("breathing.wav")
        welcome_message(active_player)
        curr_location = josh_room
        code_unlocked = False
        play_game = True
        hands = "dirty"
        shirt = "dirty"
        continue_on = input("Press ENTER to continue")
        while play_game:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(curr_location)
            curr_items_list = which_list(curr_location)
            same_location = True
            while same_location:
                active_player.alert_banner()
                print(f"What would you like {active_player.name} to do now?")
                elevator_only = False
                print_main_menu(curr_location, code_unlocked)
                main_menu_choice = input("Please choose: ")
                if main_menu_choice == "1":
                    play_game = main_menu_choice_1(
                        curr_items_list, active_player)
                    if play_game == "fart":
                        play_game = False
                        same_location = False
                elif main_menu_choice == "2":
                    play_game = main_menu_choice_2(
                        curr_location, active_player, item_use_menu)
                    if play_game == "fart":
                        play_game = False
                        same_location = False
                elif main_menu_choice == "3":  # Move to a new location
                    curr_location = main_menu_choice_3(
                        curr_location, active_player)
                    same_location = False
                elif main_menu_choice == "4":
                    play_game = False
                    same_location = False
                    print("The police are on their way! You lose!")
                    sound("siren.wav")
                    sound("siren2.wav")
                    caught_graphic()
                elif main_menu_choice == "5":
                    play_game = main_menu_choice_5(
                        curr_location, active_player)
                    same_location = False
                else:
                    error_statement()
        play_again = input("Would you like to play again? 'Y' or 'N': ")
        if play_again.lower() == 'y':
            continue_playing = True
        elif play_again.lower() == 'n':
            continue_playing = False
        else:
            error_statement()


play_game()
