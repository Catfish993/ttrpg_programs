import random
import data
import util

class Character:

    def __init__(self, number_char = 1, name="", clan_name = "", gender="", race="", archetype ="", magic_spells="", cleric_spells=""):
        
        self.characters = []
        self.number_char = number_char
        self.name = name
        self.gender = gender
        self.race = race
        self.archetype = archetype
        self.clan_name = clan_name
        self.magic_spells = magic_spells
        self.cleric_spells = cleric_spells
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

    def get_race(self):
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
                self.name = random.choice(data.dwarven_names)  
                return self.name
            if self.race == "Human":
                self.name = random.choice(data.human_names)  
                return self.name
            if self.race == "Elf":
                self.name = random.choice(data.elven_names)  
                return self.name
            if self.race == "Halfling":
                self.name = random.choice(data.halfling_names)  
                return self.name
        else:
            self.name = self.name
            return self.name
        
    def get_clan_name(self):
        if self.race == "Dwarf":
            self.clan_name = random.choice(data.dwarven_clans)
            return self.clan_name

    def get_archetype(self):
        
        if self.archetype == "":
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
        
        for _ in range(self.number_char):

            self.getStats()
            self.get_race()
            self.get_name()
            self.get_clan_name()
            self.get_archetype()
            self.get_magic_spells()
            self.get_cleric_spells()
            self.clean_character_sheet()

    def get_magic_spells(self):
        if self.archetype == "Magic User":
            self.magic_spells = random.choice(data.first_level__magic_spells)

    def get_cleric_spells(self):
        if self.archetype == "Cleric":
            self.cleric_spells = random.choice(data.first_level__cleric_spells)

    def __str__(self):
        if self.archetype == "Cleric":
            return f"Character(Race: {self.race}, Name: {self.name} {self.clan_name}, Class: {self.archetype}, Cleric Spell: {self.cleric_spells})"
        if self.archetype == "Magic User":
            return f"Character(Race: {self.race}, Name: {self.name} {self.clan_name}, Class: {self.archetype}, Spells: Read Magic, {self.magic_spells})"
        if self.race == "Dwarf":
            return f"Character(Race: {self.race}, Name: {self.name} {self.clan_name}, Class: {self.archetype})"
        else:
            return f"Character(Race: {self.race}, Name: {self.name}, Class: {self.archetype})"
        

character1 = Character()
character1.generate_character()
print(character1)