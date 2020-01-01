# This function will take a list and then print out the items 
# separated by a comma with an "and" before the last word.
#
# While the instructions did not mention it I also added
# code to handle blank lists, single items, and just two items.

def comma(items):
    if len(items) == 0:
        print("Error: Blank list")
    elif len(items) == 1:
        print(items[0])
    elif len(items) == 2:
        print(items[0] + " and " + items[1])
    else:
        for i in range(len(items)):
            if i + 1 < len(items):
                print(items[i], end = ", ")
            else:
                print("and " + items[i])


oh_my = ["Lions", "Tigers", "Bears"]
the_who = ["Pete", "Roger", "Keith", "John"]
droids_were_looking_for = ["R2D2", "C3P0"]
big_mac = ["Two all-beef patties", "Special Sauce", "Lettuce", 
           "Cheese", "Pickles", "Onions", "a Sesame Seed Bun"]
solo = ["Han"]
blank_list = []

comma(oh_my)
comma(the_who)
comma(droids_were_looking_for)
comma(big_mac)
comma(solo)
comma(blank_list)