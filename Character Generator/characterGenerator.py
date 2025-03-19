import random
import Data
import util

class Character:

    races = ["Elf", "Human", "Dwarf", "Halfling"]
    archetypes = ["Cleric", "Fighter", "Spell Caster", "Thief"] 

    def __init__(self, name="", clan_name = "", gender="", race="", archetype =""):
        self.name = name
        self.gender = gender
        self.race = race
        self.archetype = archetype
        self.clan_name = clan_name
        self.abilities = {
    "Strength": 0,
    "Intelligence": 0,
    "Wisdom": 0,
    "Dexterity": 0,
    "Constitution": 0,
    "Charisma": 0
}

    def getStats(self):
        for ability in self.abilities:
            self.abilities[ability] = util.dice_4d6()
            print(f"{ability}: {self.abilities[ability]}") 

    def getRace(self):
        valid_races = ["Human"]
        if self.abilities["Constitution"] >= 9:
            valid_races.append("Dwarf")
        if self.abilities["Intelligence"] >=9:
            valid_races.append("Elf")
        if self.abilities["Dexterity"] >=9:
            valid_races.append("Halfling")
        
        self.race = random.choice(valid_races)
        return self.race
    
    def get_name(self):
        
        if self.name == "":
            if self.race == "Dwarf":
                self.name = random.choice(Data.dwarven_names)  
                return self.name
            if self.race == "Human":
                self.name = random.choice(Data.human_names)  
                return self.name
            if self.race == "Elf":
                self.name = random.choice(Data.elven_names)  
                return self.name
            if self.race == "Halfling":
                self.name = random.choice(Data.halfling_names)  
                return self.name
        else:
            self.name = self.name
            return self.name
        
    def get_clan_name(self):
        if self.race == "Dwarf":
            self.clan_name = random.choice(Data.dwarven_clans)
            return self.clan_name

    def get_archetype(self):
        
        valid_archetype = ["Fighter"]

        if self.abilities["Wisdom"] >=9:
            valid_archetype.append("Cleric")
        if self.abilities["Intelligence"] >=9 and self.race != "Dwarf" and self.race != "Halfling":
            valid_archetype.append("Magic User")
        if self.abilities["Dexterity"] >=9 and self.race != "Dwarf":
            valid_archetype.append("Thief")

        self.archetype = random.choice(valid_archetype)

    def clean_character_sheet(self):
        # modifies stats if they are too high
        if self.race == "Dwarf" and self.abilities["Charisma"] >17:
            self.abilities["Charisma"] = 17
        if self.race == "Elf" and self.abilities["Constitution"] >17:
            self.abilities["Constitution"] = 17
        if self.race == "Halfling" and self.abilities["Strength"] >17:
            self.abilities["Strength"] = 17

    def generate_character(self):
        self.getStats()
        self.getRace()
        self.get_name()
        self.get_clan_name()
        self.get_archetype()
        self.clean_character_sheet()

    def __str__(self):
        if self.race == "Dwarf":
            return f"Character(Race: {self.race}, Name: {self.name} {self.clan_name}, Class: {self.archetype})"
        else:
            return f"Character(Race: {self.race}, Name: {self.name}, Class: {self.archetype})"
        

character1 = Character()
character1.generate_character()
print(character1)