# This assignment was to write a funcation whose input is a 
# dictionary containing a player character's inventory
# and to print that inventory out in a format that would
# be readable by the player.

def listInvent(invent):
    item_count = 0
    print("You curently have:")
    for item, count in invent.items():
        print(item + " " + str(count))
        item_count = item_count + count
    print("That is total of " + str(item_count) + " items.")

player_inventory = {'gumball': 20, 'potion': 5, 'torch': 2, 'gnome head': 6, 'alpaca': 1}

listInvent(player_inventory)