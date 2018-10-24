from player import *
from items import *
from gameparser import *

#function returns weapon if it is valid

def equip(player):
    if player["inventory"] == []:
        print("Cant equip anything.")
        return None #if nothing in inventory returns none
    running = True
    while running == True:
        print("Select your weapon:")
        for i in player["inventory"]:
            print(i["name"]) #prints available inventory
        weapon = input("Enter the weapon you want to equip: ")
        weapon = normalise_input(weapon) #normalise player input
        weapon = weapon[0] #gains string from the normalised input
        for i in player["inventory"]: #checks the inventory if valid
            if weapon == i["name"].lower():
                running = False
                return i #returns the id of the weapon
            else:
                print("not a valid entry")
