def welcome_message(active_player):
    print(f"Welcome to 'How To Get Away With MURDER!'\n\n{active_player.name} just woke up in a small room in the Atlanta Tech Village with a dead body on the floor, bloody clothes and hands, with all evidence pointing to {active_player.pronoun2}.\nAfter looking around, it doesn't look like anyone has noticed yet. \n{active_player.name} has dreams of becoming a top notch programmer and knows that no one will believe {active_player.pronoun} wasn't the murderer.\nIn fact, {active_player.name} isn't even sure {active_player.pronoun} didn't do it. \n\nHelp {active_player.name} get away with this murder so one day {active_player.pronoun2} programming dreams can be achieved. \n\nNavigate through the school and gather items that will help {active_player.pronoun2} escape past the guard with the body to make it to the parking lot. \nBut beware -- everything you find will not be helpful and don't leave too much evidence around or you may be discovered. \nOnce you feel like you won't attract too much attention(alert level), try to sneak past the security desk and out of the door. \n\n\n****GOOD LUCK!****\n\n\nTIPS: \n*You must bring picked up items back to the murder room to use them. \n*Carrying too many items at once will raise your alert level.\n\n\n")


def arcade_screen():
    print('''
            _______   ______         ___      .______        ______     ___       _______   _______ 
            |       \ /      |       /   \     |   _  \      /      |   /   \     |       \ |   ____|
            |  .--.  |  ,----'      /  ^  \    |  |_)  |    |  ,----'  /  ^  \    |  .--.  ||  |__   
            |  |  |  |  |          /  /_\  \   |      /     |  |      /  /_\  \   |  |  |  ||   __|  
            |  '--'  |  `----.    /  _____  \  |  |\  \----.|  `----./  _____  \  |  '--'  ||  |____ 
            |_______/ \______|   /__/     \__\ | _| `._____| \______/__/     \__\ |_______/ |_______|


                                                                                                                                                                    
                  (       )                                                                                                                                            
                  )\   ( /(                  (       )   (  (      )     )      (                                                                                      
                  (((_)  )\())  (    (   (    ))\   ( /(   )\))(  ( /(    (      ))\                                                                                     
                  )\___ ((_)\   )\   )\  )\  /((_)  )(_)) ((_))\  )(_))   )\  ' /((_)_                                                                                   
                  ((/ __|| |(_) ((_) ((_)((_)(_))   ((_)_   (()(_)((_)_  _((_)) (_)) (_)                                                                                  
                   | (__ | ' \ / _ \/ _ \(_-</ -_)  / _` | / _` | / _` || '  \()/ -_) _                                                                                   
                    \___||_||_|\___/\___//__/\___|  \__,_| \__, | \__,_||_|_|_| \___|(_)                                                                                  
                                                            |___/                          

 _______        ______            __ ___                    _____                                _  __           __          
/_  __(_)______/_  __/__ ________/_  __/__  ___            / ___/_ _____ ___ ___   __ _  __ __  / |/ /_ ____ _  / /  ___ ____
 / / / / __/___// / / _ `/ __/___// / / _ \/ -_)          / (_ / // / -_|_-<(_-<  /  ' \/ // / /    / // /  ' \/ _ \/ -_) __/
/_/ /_/\__/    /_/  \_,_/\__/    /_/  \___/\__/           \___/\_,_/\__/___/___/ /_/_/_/\_, / /_/|_/\_,_/_/_/_/_.__/\__/_/   
                                                                                       /___/                                                          
''')


def caught_graphic():
    print('''
                       _____________________
    /  .       .      (<$$$$$$>#####<::::::>)
   .      .     .  _/~~~~~~~~~~~~~~~~~~~~~~~~~\_   .       .   .   \\
.(          . .  /~                             ~\ . .   .
  ( . .        .~                                 ~.      .         )
           ()\/_____                           _____\/()   .    .  ).
(         .-''      ~~~~~~~~~~~~~~~~~~~~~~~~~~~     ``-.  ...
.  . . .-~              __________________              ~-.  .    /
 .   ..`~~/~~~~~~~~~~~~TTTTTTTTTTTTTTTTTTTT~~~~~~~~~~~~\~~'    . ) .
    . .| | | #### #### || | | | [] | | | || #### #### | | | .
   (   ;__\|___________|++++++++++++++++++|___________|/__;.   .
     .  (~~====___________________________________====~~~)
 ( .  .. \------_____________[ POLICE ]__________-------/ ..  .     )
         .  |      ||         ~~~~~~~~       ||      |
             \_____/                          \_____/
''')


def get_away_graphic():
    print('''
                  ___..................____
           _..--''~_______   _____...----~~~\\
       __.'    .-'~       \\~      [_`.7     \\
 .---~~      .'            \\           __..--\\_
/             `-._          \\   _...~~~_..---~  ~~~~~~~~~~~~--.._
\              /  ~~~~~~----_\`-~_-~~__          ~~~~~~~---.._    ~--.__
 \     _       |==            |   ~--___--------...__          `-   _.--"""|
  \ __/.-._\   |              |            ~~~~--.  `-._ ___...--~~~_.'|_Y |
   `--'|/~_\\  |              |     _____           _.~~~__..--~~_.-~~~.-~/
     | ||| |\\_|__            |.../.----.._.        | Y |__...--~~_.-~  _/
      ~\\\ || ~|..__---____   |||||  .'~-. \\       |_..-----~~~~   _.~~
        \`-'/ /     ~~~----...|\'''|  |/"_"\ \\   |~~'           __.~
         \`~~~'                 ~~-:  ||| ~| |\\  |        __..~~
                                   ~~|||  | | \\/  _.---~~
                                     \\\  //  | ~~~
                                      \`-'/  / 
                                       `~~~~'
''')


def game_start_graphic():
    print('''
  _    _                 _                     _                                          _ _   _     
 | |  | |               | |                   | |                                        (_) | | |    
 | |__| | _____      __ | |_ ___     __ _  ___| |_    __ ___      ____ _ _   _  __      ___| |_| |__  
 |  __  |/ _ \ \ /\ / / | __/ _ \   / _` |/ _ \ __|  / _` \ \ /\ / / _` | | | | \ \ /\ / / | __| '_ \ 
 | |  | | (_) \ V  V /  | || (_) | | (_| |  __/ |_  | (_| |\ V  V / (_| | |_| |  \ V  V /| | |_| | | |
 |_|  |_|\___/ \_/\_/    \__\___/   \__, |\___|\__|  \__,_| \_/\_/ \__,_|\__, |   \_/\_/ |_|\__|_| |_|
                                     __/ |                                __/ |                       
                                    |___/                                |___/                        
                                                                                                                                                                                          
                                                                                                                                                                                          
                    @@@@@@@@@@   @@@  @@@  @@@@@@@   @@@@@@@   @@@@@@@@  @@@@@@@   
                    @@@@@@@@@@@  @@@  @@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  
                    @@! @@! @@!  @@!  @@@  @@!  @@@  @@!  @@@  @@!       @@!  @@@  
                    !@! !@! !@!  !@!  @!@  !@!  @!@  !@!  @!@  !@!       !@!  @!@  
                    @!! !!@ @!@  @!@  !@!  @!@!!@!   @!@  !@!  @!!!:!    @!@!!@!   
                    !@!   ! !@!  !@!  !!!  !!@!@!    !@!  !!!  !!!!!:    !!@!@!    
                    !!:     !!:  !!:  !!!  !!: :!!   !!:  !!!  !!:       !!: :!!   
                    :!:     :!:  :!:  !:!  :!:  !:!  :!:  !:!  :!:       :!:  !:!  
                    :::     ::   ::::: ::  ::   :::   :::: ::   :: ::::  ::   :::  
                      :      :     : :  :    :   : :  :: :  :   : :: ::    :   : :   
''')


def win_graphic():
    print('''
                    .-\'''-.                                                   ___      ___      ___   
                   '   _    \                                               .'/   \  .'/   \  .'/   \  
                 /   /` '.   \                              .--.   _..._   / /     \/ /     \/ /     \ 
 .-.          .-.   |     \  '                       _     _|__| .'     '. | |     || |     || |     | 
  \ \        / /|   '      |  '                /\    \\\   //.--..   .-.   .| |     || |     || |     | 
   \ \      / / \    \     / /                 `\\\  //\\\ // |  ||  '   '  ||/`.   .'|/`.   .'|/`.   .' 
    \ \    / /   `.   ` ..' /_    _              \`//  \\'/  |  ||  |   |  | `.|   |  `.|   |  `.|   |  
     \ \  / /       '-...-'`| '  / |              \|   |/   |  ||  |   |  |  ||___|   ||___|   ||___|  
      \ `  /               .' | .' |               '        |  ||  |   |  |  |/___/   |/___/   |/___/  
       \  /                /  | /  |                        |__||  |   |  |  .'.--.   .'.--.   .'.--.  
       / /                |   `'.  |                            |  |   |  | | |    | | |    | | |    | 
   |`-' /                 '   .'|  '/                           |  |   |  | \_\    / \_\    / \_\    / 
    '..'                   `-'  `--'                            '--'   '--'  `''--'   `''--'   `''--' 
    ''')


def guess_number_graphic():
    print('''
        _______  __   __  _______  _______  _______    __   __  __   __    __    _  __   __  __   __  _______  _______  ______   
        |       ||  | |  ||       ||       ||       |  |  |_|  ||  | |  |  |  |  | ||  | |  ||  |_|  ||  _    ||       ||    _ |  
        |    ___||  | |  ||    ___||  _____||  _____|  |       ||  |_|  |  |   |_| ||  | |  ||       || |_|   ||    ___||   | ||  
        |   | __ |  |_|  ||   |___ | |_____ | |_____   |       ||       |  |       ||  |_|  ||       ||       ||   |___ |   |_||_ 
        |   ||  ||       ||    ___||_____  ||_____  |  |       ||_     _|  |  _    ||       ||       ||  _   | |    ___||    __  |
        |   |_| ||       ||   |___  _____| | _____| |  | ||_|| |  |   |    | | |   ||       || ||_|| || |_|   ||   |___ |   |  | |
        |_______||_______||_______||_______||_______|  |_|   |_|  |___|    |_|  |__||_______||_|   |_||_______||_______||___|  |_|

 ______       ______       ______       ______       ______       ______       ______       ______       ______       ______       ______  
|      |     |      |     |      |     |      |     |      |     |      |     |      |     |      |     |      |     |      |     |      | 
|___   |     |___   |     |___   |     |___   |     |___   |     |___   |     |___   |     |___   |     |___   |     |___   |     |___   | 
  __|  |       __|  |       __|  |       __|  |       __|  |       __|  |       __|  |       __|  |       __|  |       __|  |       __|  | 
 |_____|      |_____|      |_____|      |_____|      |_____|      |_____|      |_____|      |_____|      |_____|      |_____|      |_____| 
   __           __           __           __           __           __           __           __           __           __           __    
  |__|         |__|         |__|         |__|         |__|         |__|         |__|         |__|         |__|         |__|         |__|   
  ''')


def tic_tac_toe_graphic():
    print('''
 _______  ___   _______         _______  _______  _______         _______  _______  _______ 
|       ||   | |       |       |       ||   _   ||       |       |       ||       ||       |
|_     _||   | |       | ____  |_     _||  |_|  ||       | ____  |_     _||   _   ||    ___|
  |   |  |   | |       ||____|   |   |  |       ||       ||____|   |   |  |  | |  ||   |___ 
  |   |  |   | |      _|         |   |  |       ||      _|         |   |  |  |_|  ||    ___|
  |   |  |   | |     |_          |   |  |   _   ||     |_          |   |  |       ||   |___ 
  |___|  |___| |_______|         |___|  |__| |__||_______|         |___|  |_______||_______|
  ''')


def walking_the_hallway():
    os.system('cls||clear')
    print("You are trying to escape! Good luck.\nRememeber, if your alert level is too high, you will get caught!\nIt's time to sneak down to the lobby. You gather up the body and head down the hall. Hopefully, no one catches you!")
    continue_on = input("Please press ENTER to continue.")
    print("*----")
    sound("footsteps.wav")
    time.sleep(1)
    os.system('cls||clear')
    print("You are trying to escape! Good luck.\nRememeber, if your alert level is too high, you will get caught!\nIt's time to sneak down to the lobby. You gather up the body and head down the hall. Hopefully, no one catches you!")
    print("Please press ENTER to continue.")
    print("**---")
    time.sleep(1)
    os.system('cls||clear')
    print("You are trying to escape! Good luck.\nRememeber, if your alert level is too high, you will get caught!\nIt's time to sneak down to the lobby. You gather up the body and head down the hall. Hopefully, no one catches you!")
    print("Please press ENTER to continue.")
    print("***--")
    time.sleep(1)
    os.system('cls||clear')
    print("You are trying to escape! Good luck.\nRememeber, if your alert level is too high, you will get caught!\nIt's time to sneak down to the lobby. You gather up the body and head down the hall. Hopefully, no one catches you!")
    print("Please press ENTER to continue.")
    print("****-")
    time.sleep(1)
    os.system('cls||clear')
    print("You are trying to escape! Good luck.\nRememeber, if your alert level is too high, you will get caught!\nIt's time to sneak down to the lobby. You gather up the body and head down the hall. Hopefully, no one catches you!")
    print("Please press ENTER to continue.")
    print("*****")
    time.sleep(1)
    os.system('cls||clear')


def elevator_going_down():
    sound("elevator.wav")
    os.system('cls||clear')
    print('''
    | * |
    |   |
    |   |
    |   |
    |   |
    ''')
    time.sleep(1)
    os.system('cls||clear')
    print('''
    |   |
    | * |
    |   |
    |   |
    |   |
    ''')
    time.sleep(1)
    os.system('cls||clear')
    print('''
    |   |
    |   |
    | * |
    |   |
    |   |
    ''')
    time.sleep(1)
    os.system('cls||clear')
    print('''
    |   |
    |   |
    |   |
    | * |
    |   |
    ''')
    time.sleep(1)
    os.system('cls||clear')
    print('''
    |   |
    |   |
    |   |
    |   |
    | * |
    ''')
    time.sleep(1)
    os.system('cls||clear')


def sneak_past_security():
    sound("footsteps.wav")
    os.system('cls||clear')
    print("*----")
    time.sleep(.5)
    os.system('cls||clear')
    print("-*---")
    time.sleep(.5)
    os.system('cls||clear')
    print("--*--")
    time.sleep(.5)
    os.system('cls||clear')
    print("---*-")
    time.sleep(.5)
    os.system('cls||clear')
    print("----*")
    time.sleep(.5)
    os.system('cls||clear')


def casual_past_security():
    sound("footsteps.wav")
    os.system('cls||clear')
    print("|----")
    time.sleep(.5)
    os.system('cls||clear')
    print("-|---")
    time.sleep(.5)
    os.system('cls||clear')
    print("--|--")
    time.sleep(.5)
    os.system('cls||clear')
    print("---|-")
    time.sleep(.5)
    os.system('cls||clear')
    print("----|")
    time.sleep(.5)
    os.system('cls||clear')
