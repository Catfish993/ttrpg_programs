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
        pass

class Items:

    def __init__(self, item, quantity, price):

        self.item = item
        self.quantity = quantity
        self.price = price
    
    # method takes items and applies return valies from econ class
    # 
