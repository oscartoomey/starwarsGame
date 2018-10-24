from map import locations
from items import items
from player import *
from music import *
from equip import *
from gameparser import normalise_input
from time import sleep, clock


# Take timed input, timed in seconds.
def fight(max_time,enemy):
    # Record the time before and after the user types their input.
    print("Enemy: {}".format(enemy["name"]))
    print("You have {} seconds to take {} out.".format(max_time,enemy))
    sleep(1)
    print("Enter the next word quickly!:")
    sleep(0.5)
    print(".")
    sleep(0.5)
    print(".")
    sleep(0.5)
    print(".")
    sleep(0.5)
    print("Fight!")
    start_time = clock()
    end_time = clock()
    # Check if they were fast enough and gave the correct input.
    time_taken = end_time - start_time
    while True:
        killwords = enemy["killwords"]
        correct = random.choice(killwords)
        user_input = input(correct + "\n")
        if user_input == correct and time_taken <= max_time:
            enemy["health"] = enemy["health"] - luke["damage"]
            print(enemy["health"])
            if enemy["health"] <= 0:
                return True
        else:
            luke["health"] = luke["health"] - enemy["damage"]
            print(luke["health"])
            if luke["health"] <= 0:
                print("Luke has been killed!")
                exit


# Items in inventory
def list_of_items(items):

    # Create a string of items
    string_of_items = ""
    for item in items:
        if item != items[len(items) - 1]:
            string_of_items = string_of_items + item["name"] + ", "
        else:
            string_of_items = string_of_items + item["name"]
    return string_of_items


# Items in the location
def print_location_items(location):
    # If there are no items, 
    if location["items"] == []:
        return


# Print the current location
def print_location(player):

    # Introduce location
    print("You're currently located in the " + player["location"]["name"] + "...")
    # Describe location
    print(player["location"]["description"])
    print()
    # Display items in location
    print_location_items(player["location"])


# Available exits
def exit_leads_to(exits, direction):
    return locations[exits[direction]]["name"]


# Valid exits
def is_valid_exit(chosen_exit, exits):

    return chosen_exit in exits


# Print exits
def print_exit(direction, leads_to):

    print("GO " + direction.upper() + " to " + leads_to + ".")


# Print menu
def print_menu(exits, location_items, inv_items):

    print("You can:")
    # Iterate over available exits
    for direction in exits:
        # Print exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))

    # Item options
    for item in location_items:
        print("TAKE " + item["id"].upper() + " to take " + item["name"] + ".")
    for item in inv_items:
        print("DROP " + item["id"].upper() + " to drop " + item["name"] + ".")
    if inv_items != []:
        print("EQUIP")

    print("What do you want to do?")


# Execute Functions
# Execute go
def execute_go(player, direction):
    if is_valid_exit(direction, player["location"]["exits"]):
        player["location"] = move(player["location"]["exits"], direction)
    else:
        print("You cannot go there.")

# Execute take
def execute_take(player, item_id):

    found = False

    for item in player["location"]["items"]:
        if item_id == item["id"] and inventory_mass(player["inventory"]) + item["mass"] <= player["max_mass"]:
            player["inventory"].append(item)
            player["location"]["items"].remove(item)
            found = True
            print(item_id, " added to inventory")
# OPTIONAL - MASS CAPACITY FUNCTION
        elif inventory_mass(player["inventory"]) + item["mass"] > player["max_mass"]:
            print("You've reach your maximum mass capacity")
            # Display mass status
            print("You're carrying" + str(inventory_mass(player["inventory"]) +
                  item["mass"]) + "kg, this is too much!")
            return
    # Necessary reject
    if found == False:
        print("You cannot take that.")


# Execute drop
def execute_drop(player, item_id):

    success = False
    for items in player["inventory"]:
        if item_id == items["id"]:
            player["location"]["items"].append(items)
            player["inventory"].remove(items)
            print(items["name"] + " dropped.")
            success = True
    if success == False:
        print("You cannot drop that.")


# Execute command
def execute_command(player, command):

    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(player, command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(player, command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(player, command[1])
        else:
            print("Drop what?")
    
    elif command[0] == "equip" and len(player["inventory"]) != 0:
        newDamage = None
        while newDamage == None:
            newDamage = equip()
        player["damage"] = newDamage

    else:
        print("This makes no sense.")


# Inventory mass
def inventory_mass(inventory):

    # Original mass
    x = 0

    # Adding mass to the inventory
    for item in inventory:
        x += item["mass"]

    # Returning the new mass
    return x


# Menu
def menu(exits, location_items, inv_items):

    # Display menu
    print_menu(exits, location_items, inv_items)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    # Return the input
    return normalised_user_input


# Print the player's health
def print_health(player):
    print("Your current health is " + str(player["health"]) + "/" + str(player["max_health"]) + ".")


# Move
def move(exits, direction):
    return locations[exits[direction]]

def deathstar():
    if player["location"] == location_deathstar:
        print("Storm troopers wait for you once you arrive to the ship, take them out!")
        fight(5,stormtrooper)
        fight(5,stormtrooper)
        fight(3,stormtrooper)
        
        
# Display starwars ascii and wait for input.
def ready_to_play():
    print(r"            _________  ___  _____                                        ")
    print(r"           / __   __| / _ \ |  _ \                                       ")
    print(r"     ______> \ | |   |  _  ||    /_____________________________          ")
    print(r"    / _______/ |_|   |_| |_||_|\______________________________ \         ")
    print(r"   / /                                                        \ \        ")
    print(r"  | |                                                          | |       ")
    print(r"  | |                                                          | |       ")
    print(r"  | |                                                          | |       ")
    print(r"  | |                                                          | |       ")
    print(r"  | |                  Press Enter to Play                     | |       ")
    print(r"  | |                                                          | |       ")
    print(r"  | |                                                          | |       ")
    print(r"  | |                                                          | |       ")
    print(r"  | |                                                          | |       ")
    print(r"   \ \____________________________    _   ___   ____   _______/ /        ")
    print(r"    \___________________________  |  | | / _ \ |  _ \ / _______/         ")
    print(r"                                | |/\| ||  _  ||    / > \                ")
    print(r"                                 \_/\_/ |_| |_||_|\_\|__/                ")
    input()


# Allow the player to choose a character.
def choose_character():
    print(r" ________________________     _________________________ ")
    print(r"|        .......         |   |      .x%%%%%%x.         |")
    print(r"|      ::::::;;::.       |   |     ,%%%%%%%%%%%        |")
    print(r"|    .::;::::;::::.      |   |    ,%%%'  )'  \%        |")
    print(r"|   .::::::::::::::      |   |   ,%x%) __   _ Y        |")
    print(r"|   ::`_```_```;:::.     |   |   :%%% ~=-. <=~|        |")
    print(r"|   ::=-) :=-`  ::::     |   |   :%%::. .:,\  |        |")
    print(r"| `::|  / :     `:::     |   |   `;%:`\. `-' .'        |")
    print(r"|   '|  `~'     ;:::     |   |    ``x`. -===-;         |")
    print(r"|    :-:==-.   / :'      |   |     / `:`.__.;          |")
    print(r"|    `. _    .'.d8:      |   |  .d8b.  :: ..`.         |")
    print(r"| _.  |88bood88888._     |   | d88888b.  '  /8         |")
    print(r"|~  `-+8888888888P  `-. _|   |d888888888b. ( 8b       /|")
    print(r"|-'     ~~^^^^~~  `./8 ~ |   |~   ~`888888b  `8b     /:|")
    print(r"|8b /  /  |   \  \  `8   |   |  ' ' `888888   `8. _ /:/|")
    print(r"|P        `          8   |   |'      )88888b   8b |):X |")
    print(r"|                    8b  |   |   ~ - |888888   `8b/:/:\|")
    print(r"|                    `8  |   |       |888888    88\/~~;|")
    print(r"|                     8b |   |       (888888b   88|  / |")
    print(r"|         .           `8 |   |\       \888888   8-:   /|")
    print(r"|________/_\___________8_|   |_\_______\88888_.'___\__/|")
    print()
    print(r"L u k e  S k y w a l k e r         H a n   S o l o      ")
    print()
    print(r" Jedi Knight, Strong with         Smuggler, Pirate      ")
    print(r"the force, has a lightsaber     has a gun and Chewie!   ")

    # Ask the user who to play as, repeat as long as they give invalid input.
    choice = input("Would you like to play as Luke or Han?").lower().strip()
    while choice != "luke" and choice != "han":
        print("You can only choose Luke or Han.")
        choice = input("Would you like to play as Luke or Han?").lower().strip()
    
    if choice == "luke":
        return luke
    else:
        return han


# Check if the player has won.
def has_won(player):
    return item_leia in player["inventory"]


# Main function
def main():
    # Introduction (ready to play etc)
    ready_to_play()

    # Show the title sequence
    intro()

    print()

    # Allow the user to select a character
    player = choose_character()

    while not has_won(player):
        # Print status
        print_location(player)
        print_health(player)

        # Show possible actions
        command = menu(player["location"]["exits"],
                       player["location"]["items"], player["inventory"])

        # Execute the user's commands
        execute_command(player, command)

    print()
    print("Congratulations, the universe is safe again thanks to your efforts!")
    print("Now Darth Vader (or Kirill if you prefer) has been defeated and peace")
    print("has been restored to the galaxy once again...   for now...")


if __name__ == "__main__":
    main()
