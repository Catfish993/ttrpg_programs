import random
import items
import json

with open("Dynamic Economy/og_inventory.json", "r") as f:
    inventory = json.load(f)

with open("Dynamic Economy/updated_inventory.json", "r") as f:
    updated_inventory = json.load(f)

class Econ:

    # simulate an economy
    def __init__(self):
        pass

    def econ_flux(self):

        # soooo messy please clean up :(

        for x in items.tags:

            num = random.randint(1,3)

            # Refactor
            # checking if the tag is in the updated_inventory
            # if true, getting the old price and updating it to the new price
            # writing that new price to updated_inventory.json

            if num == 1:
                # price increase
                print(f"\nIncreasing prices for tag: {x}")
                for name, data in updated_inventory.items():
                    if data["tag"] == x:
                        old_price = data["price"]
                        new_price = round(old_price * 1.5)
                        data["price"] = new_price
                        print(f"{name} price increased from {old_price} to {new_price}gp")
                        with open("Dynamic Economy/updated_inventory.json", "w") as f:
                            json.dump(updated_inventory, f, indent=4)
            if num == 2:
                print(f"\nDecreasing prices for tag: {x}")
                for name, data in updated_inventory.items():
                    if data["tag"] == x:
                        old_price = data["price"]
                        new_price = round(old_price / 1.5)
                        data["price"] = new_price
                        print(f"{name} market price reset from {old_price} to {new_price} gp")
                        with open("Dynamic Economy/updated_inventory.json", "w") as f:
                            json.dump(updated_inventory, f, indent=4)
                    
            if num == 3:
                print(f"\nResetting prices for tag: {x}")
                for name, data in updated_inventory.items():
                    if data["tag"] == x:
                        print(f"{name} Market price reset.")

                        # This currently writes over everything. Needs to be more dynamic

                        with open("Dynamic Economy/updated_inventory.json", "w") as f:
                            json.dump(inventory, f, indent=4)


class Items:

    def __init__(self, item, quantity, price, tag):

        self.item = str(item).lower()
        self.quantity = int(quantity)
        self.price = int(price)
        self.tag = str(tag).lower()

        # Add to global inventory
        new_item = {
            "quantity": self.quantity,
            "price": self.price,
            "tag": self.tag
        }

        inventory[self.item] = new_item

        try:
            with open("Dynamic Economy/og_inventory.json", "r") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}

        data[self.item] = new_item

        with open("Dynamic Economy/og_inventory.json", "w") as f:
            json.dump(data, f, indent=4)

        if self.tag in items.tags:
            print("tag found in list. not adding. ")
        else:
            print("adding tag")
            items.tags.append(self.tag)

    def show_all_items(self):
        for name, data in inventory.items():
            print(f"{name.title()}: {data['quantity']} units, {data['price']}gp [{data['tag']}]")

    def show_items_with_tag(self, tag: str):
        tagged_items = {
        name: data for name, data in inventory.items()
        if data["tag"] == tag.lower()
    }
        
        if tagged_items == {}:
            print(f"No items with tag found.")
        else:
            print(f"Items with {self.tag}: {tagged_items}")

new_items = Items("Long Bow", 20, 20, "test")
new_items.show_all_items()

new_econ = Econ()
new_econ.econ_flux()

