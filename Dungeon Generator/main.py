import os
import logging
import random
import data
import utils

# Dungeon Inhabitants
dungeon_monsters = ["goblin", "orc", "Adventuring party"]


class room_generator:

    def __init__(self,rooms):
        
        self.rooms = int(rooms)
        
    def MakeRooms(self):
        entrance = random.choice(data.entrance)
        self.theme = random.choice(data.simple_dungeon_themes)
        print(f'Theme: {self.theme}')
        print(f"Entrance: {entrance}")

        for i in range(1, self.rooms + 1):

            rooms = []
            self.themed_room = room_generator.theme_room()
            
            # roll room type
            room_type = utils.roll_d100()

            if room_type <= 16:
                # Empty
                rooms.append(f"{i}){self.themed_room} Empty")
            if 17 <= room_type <= 20:
                # Unguarded Treasure
                # TODO: add treasure generator
                rooms.append(f"{i}){self.themed_room} Unguarded Treasure")
            if 21 <= room_type <= 60:
                # Monster
                monster_encounter = monster_generator.generate_monster_encounter()
                rooms.append(f"{i}){self.themed_room} {monster_encounter}")
            if 61 <= room_type <= 84:
                # Monster with Treasure
                # TODO: add treasure generator
                monster_encounter = monster_generator.generate_monster_encounter()
                rooms.append(f"{i}){self.themed_room} {monster_encounter}")
            if 85 <= room_type <= 88:
                # Special
                special = random.choice(data.special_rooms)
                rooms.append(f"{i}){self.themed_room} {special}")
            if 89 <= room_type <= 96:
                # Trap
                trap = dungeon_traps.add_traps()
                rooms.append(f"{i}){self.themed_room} {trap}")
            if 97 <= room_type <= 100:
                # Trap with Treasure
                trap = dungeon_traps.add_traps()
                rooms.append(f"{i}){self.themed_room} {trap}, Treasure")

            print(rooms)

    def theme_room(self):

        for _ in range(self.rooms):

            if self.theme == "Ancient Tomb":
                themed_room = random.choice(data.ancient_tomb_rooms)
                return themed_room
            if self.theme == "Abandoned Mine":
                themed_room = random.choice(data.abandoned_mine_rooms)
                return themed_room
    
class monster_generator():

    def __init__(self):
        pass

    def add_monster(self):
        monster = random.choice(dungeon_monsters)
        return monster   
    
    def monster_activity(self):
        monster_activity = random.choice(data.activity)
        return monster_activity
    
    def reaction_roll(self):
        reaction_roll = utils.roll_2d6()

        if reaction_roll <= 2:
            return "Immediate Attack"
        if 3 <= reaction_roll <= 7:
            return "Unfavorable"
        if 8 <= reaction_roll <= 11:
            return "Favorable"
        if reaction_roll >= 12:
            return "Very Favorable"
        
    def generate_monster_encounter(self):

        monster = monster_generator.add_monster()
        monster_activity = monster_generator.monster_activity()
        reaction_roll = monster_generator.reaction_roll()
    
        return f"Inhabitant: {monster}, Activity: {monster_activity}, Reaction upon seeing Pc's: {reaction_roll}"

class Traps():

    def __init__(self):
        pass
        
    def add_traps(self):
        traps = random.choice(data.traps)
        return traps
    
room_generator = room_generator(5)
monster_generator = monster_generator()
dungeon_traps = Traps()

room_generator.MakeRooms()


