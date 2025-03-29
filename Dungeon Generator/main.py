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
        theme = random.choice(data.simple_dungeon_themes)
        print(f'Theme: {theme}')
        print(f"Entrance: {entrance}")

        for i in range(1, self.rooms + 1):

            rooms = []
            
            # roll room type
            room_type = utils.roll_d100()

            if room_type <= 16:
                # Empty
                rooms.append(f"{i})Empty")
            if 17 <= room_type <= 20:
                # Unguarded Treasure
                # TODO: add treasure generator
                rooms.append(f"{i})Unguarded Treasure")
            if 21 <= room_type <= 60:
                # Monster
                monster = monster_generator.add_monster()
                monster_activity = monster_generator.monster_activity()
                reaction_roll = monster_generator.reaction_roll()
                rooms.append(f"{i})Inhabitant {monster}, Activity: {monster_activity}. Upon Seeing the Pc's {reaction_roll}")
            if 61 <= room_type <= 84:
                # Monster with Treasure
                # TODO: add treasure generator
                monster = monster_generator.add_monster()
                monster_activity = monster_generator.monster_activity()
                reaction_roll = monster_generator.reaction_roll()
                rooms.append(f"{i})Inhabitant {monster}, Activity: {monster_activity}. Upon Seeing the Pc's {reaction_roll}, Add Treasure")
            if 85 <= room_type <= 88:
                # Special
                special = random.choice(data.special_rooms)
                rooms.append(f"{i}){special}")
            if 89 <= room_type <= 96:
                # Trap
                trap = dungeon_traps.add_traps()
                rooms.append(f"{i}){trap}")
            if 97 <= room_type <= 100:
                # Trap with Treasure
                trap = dungeon_traps.add_traps()
                rooms.append(f"{i}){trap}, Treasure")

            print(rooms)
    
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


