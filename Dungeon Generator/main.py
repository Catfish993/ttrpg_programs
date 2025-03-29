import os
import logging
import random
import data
import utils

# Dungeon Inhabitants
dungeon_monsters = ["goblin", "orc", "Adventuring party"]


# Traps
traps = ["Spike Trap", "Pit Trap"]


class room_generator:

    def __init__(self,rooms):
        
        self.rooms = int(rooms)
        
    def MakeRooms(self):

        print("Entrance:")

        for i in range(1, self.rooms + 1):
            
            monster = monster_generator.add_monster()
            monster_activity = monster_generator.monster_activity()
            reaction_roll = monster_generator.reaction_roll()
            print(f"Room: {i} Inhabitant: {monster} Activity: {monster_activity} Upon Seeing PC's: {reaction_roll}")
    
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
        
    def add_traps():
        traps = random.choice(traps)
        return traps
    
room_generator = room_generator(5)
monster_generator = monster_generator()
dungeon_traps = Traps()

room_generator.MakeRooms()


