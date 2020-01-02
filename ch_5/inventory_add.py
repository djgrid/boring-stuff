# This assignment builds on the previous one by adding a 
# function to add items to the inventory via a list.
# 
# I opted to print out the inventory once, run the add
# function and then print it again to show that things
# were added. 

def listInvent(invent):
    item_count = 0
    print("You curently have:")
    for item, count in invent.items():
        print(str(count) + " " + item)
        item_count = item_count + count
    print("That is total of " + str(item_count) + " items.")

def updateInvent(items):
 	for item in items:
 		if item in player_inventory:
 			player_inventory[item] += 1
 		else:
 			player_inventory[item] = 1

player_inventory = {'gumball': 20, 'potion': 5, 'torch': 2, 
				    'gnome head': 6, 'alpaca': 1}


print("Before:")
listInvent(player_inventory)
print(" ")

loot_crate = ['gumball', 'torch', 'gumball', 'gnome head', 'lucky item']

updateInvent(loot_crate)
print("After:")
listInvent(player_inventory)
