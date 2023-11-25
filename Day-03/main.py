print("""  
                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \\
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
          jgs |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`                                                                                                                                                                                                                                                                                                                
""")

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choose_direction = input("You are at a cross road. Where do you want to go? Type 'left' or 'right' \n")
if choose_direction.lower() == 'left':
    choose_action = input("You came to a lake. There is an island in the middle of the lake. Type 'wait' to wait for "
                          "a boat or 'swim' to swim across. \n")
    if choose_action.lower() == "wait":
        choose_color = input("You arrive at the island unharmed. There is a house with 3 doors. Red, yellow and blue "
                             "which color do you choose? \n")
        if choose_color.lower() == 'yellow':
            print("Congratulations! you found the treasure.")
            print("""
                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \\'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-'
            """)
        else:
            print("You entered in room of beasts. Game Over")

    else:
        print("You killed by the monster in lake. Game Over")
else:
    print("You Killed by the Dragon. Game Over")
