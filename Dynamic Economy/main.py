# Simulates and prints dynamic prices for items found in markets
# Items inlude weapons, armor, dungeoneering gear, food, building materials. 
# End goal is to have all the items in BFRPG simulated

# For items
# a dictionary with the key value pair being the amount and the price

# Util methods
    # taking price and increasing or decreasing 
    # taking quantity '

# Thoughts
    # classify items with tags. That will help simulate a more believable econ. 
    # tags: steel, iron, leather, wood

import random
import items

class Econ:

    # simulate an economy
    def __init__(self):
        pass

    def econ_flux(self):
        num = random.randint(1,3)
        
        # chooses a random amount of item tags to affect
        num_picks = random.randint(0, len(items.tags))
        
        # assigns the tags to be effected
        tag_selection = random.sample(items.tags, k=num_picks)
        print(num)
        print(tag_selection)

        if num == 1:
            # price increase
            pass
        if num == 2:
            # price decrease
            pass
        if num == 3:
            # price reset
            pass

class Items:

    def __init__(self, item, quantity, price, tag):

        self.item = str(item).lower()
        self.quantity = int(quantity)
        self.price = int(price)
        self.tag = str(tag).lower()

        items.inventory[self.item] = {
            "amount": self.quantity,
            "price": self.price,
            "tag": self.tag
        }

        if any(x in self.tag for x in items.tags):
            print("tag found in list. not adding. ")
        else:
            print("adding tag")
            items.tags.append(self.tag)

    def all_items(self):
       print(items.inventory) 

    def show_items_with_tag(self, tag: str):
        # print out items with specific tag
        tagged_items = {
        name: data for name, data in items.inventory.items()
        if data["tag"] == tag.lower()
    }
        
        if tagged_items == {}:
            print(f"No items with tag found.")
        else:
            print(tagged_items)

new_econ = Econ()
new_econ.econ_flux()

new_items = Items("Long Bow", 20, 20, "wood")
new_bow_items = Items("Short Bow", 20, 20, "wood")
new_items.all_items()
# new_items.show_items_with_tag('steel')

