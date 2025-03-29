import random
import data
import util

class Character:

    def __init__(self, name="", clan_name = "", gender="", race="", archetype ="", magic_spells="", cleric_spells=""):
        
        self.characters = []
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

    def get_stats(self):

        stat_block = {}

        for ability in self.abilities:
            stat_value = util.dice_4d6()
            stat_block[ability] = stat_value

        self.current_character["Stats"] = stat_block

    def get_modifiers(self):
        
        for stat, value in self.current_character["Stats"].items():

            self.modifier = 0
            
            if value ==18:
                self.modifier = 3
                self.current_character["Stats"][stat] = {
                    "Score": value,
                    "Mod": self.modifier
                }
            if 16 <= value <= 17:
                self.modifier = 2
                self.current_character["Stats"][stat] = {
                    "Score": value,
                    "Mod": self.modifier
                }
            if 13 <= value <= 15:
                self.modifier = 1
                self.current_character["Stats"][stat] = {
                    "Score": value,
                    "Mod": self.modifier
                }
            if 9 <= value <= 12:
                self.modifier = 0
                self.current_character["Stats"][stat] = {
                    "Score": value,
                    "Mod": self.modifier
                }
            if 6 <= value <= 8:
                self.modifier = -1
                self.current_character["Stats"][stat] = {
                    "Score": value,
                    "Mod": self.modifier
                }
            if 4 <= value <= 5:
                self.modifier = -2
                self.current_character["Stats"][stat] = {
                    "Score": value,
                    "Mod": self.modifier
                }
            if value == 3:
                self.modifier = -3
                self.current_character["Stats"][stat] = {
                    "Score": value,
                    "Mod": self.modifier
                }
            
    def roll_hp(self):

        if self.current_character['Class'] == "Fighter":
            con_mod = self.current_character["Stats"]["Constitution"]["Mod"]
            hp = util.roll_1d8()
            self.current_character["HP"] = hp + con_mod
        if self.current_character['Class'] == "Cleric":
            con_mod = self.current_character["Stats"]["Constitution"]["Mod"]
            hp = util.roll_1d6()
            self.current_character["HP"] = hp + con_mod
        if self.current_character['Class'] == "Magic User" or "Thief":
            con_mod = self.current_character["Stats"]["Constitution"]["Mod"]
            hp = util.roll_1d4()
            self.current_character["HP"] = hp + con_mod

    def get_race(self):

        valid_races = ["Human"]
        if self.current_character['Stats']["Constitution"] >= 9:
            valid_races.append("Dwarf")
        if self.current_character['Stats']["Intelligence"] >=9:
            valid_races.append("Elf")
        if self.current_character['Stats']["Dexterity"] >=9:
            valid_races.append("Halfling")
        
        self.current_character["Race"] = random.choice(valid_races)

    def get_name(self):
        if self.name == "":
            if self.current_character['Race'] == "Dwarf":
                self.current_character['Name'] = random.choice(data.dwarven_names)
            if self.current_character['Race'] == "Human":
                self.current_character['Name'] = random.choice(data.human_names)
            if self.current_character['Race'] == "Elf":
                self.current_character['Name'] = random.choice(data.elven_names)
            if self.current_character['Race'] == "Halfling":
                self.current_character['Name'] = random.choice(data.halfling_names)
        else:
            self.current_character['Name'] = "Test"
        
    def get_clan_name(self):
        if self.current_character['Race'] == "Dwarf":
            self.current_character['Clan Name'] = random.choice(data.dwarven_clans)

    def get_archetype(self):
        
        if self.archetype == "":
            valid_archetype = ["Fighter"]

            if self.current_character['Stats']["Wisdom"] >=9:
                valid_archetype.append("Cleric")
            if self.current_character['Stats']["Intelligence"] >=9 and self.current_character['Race'] != "Dwarf" and self.current_character['Race'] != "Halfling":
                valid_archetype.append("Magic User")
            if self.current_character['Stats']["Dexterity"] >=9 and self.current_character['Race'] != "Dwarf":
                valid_archetype.append("Thief")

            self.current_character['Class'] = random.choice(valid_archetype)

    def get_magic_spells(self):
        if self.current_character["Class"] == "Magic User":
            self.current_character["1st Spell"] = "Read Magic"
            self.current_character["2nd Spell"] = random.choice(data.first_level__magic_spells)

    def get_cleric_spells(self):
        if self.current_character["Class"] == "Cleric":
            self.current_character["Spells"] = random.choice(data.first_level__cleric_spells)

    def clean_character_sheet(self):
        # modifies stats if they are too high
        if self.current_character['Race'] == "Dwarf" and self.current_character["Stats"]["Charisma"]["Score"] >17:
            self.current_character["Stats"]["Charisma"]["Score"] = 17
        if self.current_character['Race'] == "Elf" and self.current_character["Stats"]["Charisma"]["Score"] >17:
            self.current_character["Stats"]["Charisma"]["Score"] = 17
        if self.current_character['Race'] == "Halfling" and self.current_character["Stats"]["Charisma"]["Score"] >17:
            self.current_character["Stats"]["Charisma"]["Score"] = 17
        if self.current_character["HP"] == 0:
            self.current_character["HP"] = 1

    def generate_character(self, num=1):
        
        for _ in range(num):

            self.current_character = {}

            self.get_stats()
            self.get_race()
            self.get_name()
            self.get_clan_name()
            self.get_archetype()
            self.get_magic_spells()
            self.get_cleric_spells()
            self.get_modifiers()
            self.roll_hp()
            self.clean_character_sheet()

            self.characters.append(self.current_character)
            print(self.current_character)

characters = Character()
characters.generate_character()
