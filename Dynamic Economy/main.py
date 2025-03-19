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

items = {
    "sword": {
        "amount": 20,
        "price": 20,
        "tag": "steel"
    }
}

class Econ:

    # simulate an economy
    def __init__(self):

        self.tags = [
            "Steel",
            "Iron",
            "Leather",
            "Wood"
        ]
        pass

    def econ_flux(self):
        num = random.randint(1,3)
        
        num_picks = random.randint(0, len(self.tags))
        
        tag_selection = random.sample(self.tags, k=num_picks)
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

    def __init__(self, item, quantity, price):

        self.item = item
        self.quantity = quantity
        self.price = price

    
    # method takes items and applies return valies from econ class
    # 

new_econ = Econ()
new_econ.econ_flux()
