import os
import logging
import random

# Dungeon Inhabitants
dungeon_monsters = ["goblin", "orc", "Adventuring party"]
activity = ["Sleeping", "Fighting", "Preparing an Ambush"]

# Traps
traps = ["Spike Trap", "Pit Trap"]


class RoomGenerator:

    def __init__(self,rooms):
        
        self.rooms = int(rooms)
        
    def MakeRooms(self):

        print("Entrance:")

        for i in range(1, self.rooms + 1):
            
            monster = monster_generator.add_monster()
            monster_activity = monster_generator.monster_activity()
            print(f"Room: {i} Inhabitant: {monster} Activity: {monster_activity}")
    
class MonsterGenerator():

    def __init__(self):
        pass

    def add_monster(self):
        monster = random.choice(dungeon_monsters)
        return monster   
    
    def monster_activity(self):
        monster_activity = random.choice(activity)
        return monster_activity
    
class Traps():

    def __init__(self):
        pass
        
    def add_traps():
        traps = random.choice(traps)
        return traps
    
room_generator = RoomGenerator(10)
monster_generator = MonsterGenerator()
dungeon_traps = Traps()

room_generator.MakeRooms()


