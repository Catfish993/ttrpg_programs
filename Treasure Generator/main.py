# Generate treasure 
# GP (and lesser currency)
# Gems
# Generate magical weapons
import random

class treasure_generator:

    def __init__(self):
        self.weapon = {}

    def magic_weapon(self):

        r = random.randint(1,100)
        match r:

            case r if 1 <= r <= 2:
                self.weapon["Weapon Type"] = "Great Axe"
                self.weapon["Tag"] = "Melee"
            case r if 3 <= r <= 9:
                self.weapon["Weapon Type"] = "Battle Axe"
                self.weapon["Tag"] = "Melee"
            case r if 10 <= r <= 11:
                self.weapon["Weapon Type"] = "Hand Axe"
                self.weapon["Tag"] = "Melee"
            case r if 12 <= r <= 19:
                self.weapon["Weapon Type"] = "Shortbow"
                self.weapon["Tag"] = "Missle"
            case r if 20 <= r <= 27:
                self.weapon["Item Type"] = "Shortbow Arrow"
                self.weapon["Tag"] = "Missle"
            case r if 28 <= r <= 31:
                self.weapon["Weapon Type"] = "Longbow"
                self.weapon["Tag"] = "Missle"
            case r if 32 <= r <= 35:
                self.weapon["Weapon Type"] = "Longbow Arrow"
                self.weapon["Tag"] = "Missle"
            case r if 36 <= r <= 43:
                self.weapon["Weapon Type"] = "Light Quarrel"
                self.weapon["Tag"] = "Missle"
            case r if 44 <= r <= 47:
                self.weapon["Weapon Type"] = "Heavy Quarrel"
                self.weapon["Tag"] = "Missle"
            case r if 48 <= r <= 59:
                self.weapon["Weapon Type"] = "Dagger"
                self.weapon["Tag"] = "Melee"
            case r if 60 <= r <= 65:
                self.weapon["Weapon Type"] = "Shortsword"
                self.weapon["Tag"] = "Melee"
            case r if 66 <= r <= 79:
                self.weapon["Weapon Type"] = "Longsword"
                self.weapon["Tag"] = "Melee"
            case r if 80 <= r <= 81:
                self.weapon["Weapon Type"] = "Scimitar"
                self.weapon["Tag"] = "Melee"
            case r if 82 <= r <= 83:
                self.weapon["Weapon Type"] = "Two Handed-Sword"
                self.weapon["Tag"] = "Melee"
            case r if 84 <= r <= 86:
                self.weapon["Weapon Type"] = "Warhammer"
                self.weapon["Tag"] = "Melee"
            case r if 87 <= r <= 94:
                self.weapon["Weapon Type"] = "Mace"
                self.weapon["Tag"] = "Melee"
            case 95:
                self.weapon["Weapon Type"] = "Maul"
                self.weapon["Tag"] = "Melee"
            case 96:
                self.weapon["Weapon Type"] = "Pole Arm"
                self.weapon["Tag"] = "Melee"
            case 97:
                self.weapon["Weapon Item"] = "Sling Bullet"
            case r if 98 <= r <= 100:
                self.weapon["Weapon Type"] = "Spear"
                self.weapon["Tag"] = "Melee"

    def weapon_bonus_melee(self):

        r = random.randint(1,100)
        match r:
            case r if 1 <= r <= 40:
                self.weapon["Bonus"] = 1
            case r if 41<= r <= 50:
                self.weapon["Bonus"] = 2
            case r if 51<= r <= 55:
                self.weapon["Bonus"] = 3
            case r if 56<= r <= 57:
                self.weapon["Bonus"] = 4
            case 58:
                self.weapon["Bonus"] = 5
            case r if 59 <= r <= 75:
                self.weapon["Bonus"] = 1
                self.weapon["Special Enemy Damage Mod"] = 2
                self.weapon["Special Enemy"] = ""
            case r if 76 <= r <= 85:
                self.weapon["Bonus"] = 1
                self.weapon["Special Enemy Damage Mod"] = 3
                self.weapon["Special Enemy"] = ""
            case r if 86 <= r <= 95:
                self.weapon["Special Ability"] = ""
            case r if 96 <= r <= 98:
                self.weapon["Cursed"] = "-1"
            case r if 99 <= r <= 100:
                self.weapon["Cursed"] = "-2"

    def special_enemy(self):

        r = random.randint(1,6)
        if r == 1:
            self.weapon["Special Enemy"] = "Dragon"
        if r == 2:
            self.weapon["Special Enemy"] = "Enchanted"
        if r == 3:
            self.weapon["Special Enemy"] = "Lycanthropes"
        if r == 4:
            self.weapon["Special Enemy"] = "Regenerators"
        if r == 5:
            self.weapon["Special Enemy"] = "Spell Users"
        if r == 6:
            self.weapon["Special Enemy"] = "Undead"

    def special_ability(self):
        
        r = random.randint(1,20)
        match r:
            case r if 1 <= r <= 9:
                self.weapon["Special Ability"] = "Cast Light on command"
            case r if 10<= r <= 11:
                self.weapon["Special Ability"] = "Charm Person"
            case 12:
                self.weapon["Special Ability"] = "Drain Energy"
            case r if 13<= r <= 16:
                self.weapon["Special Ability"] = "Flames On Command"
            case r if 17<= r <= 19:
                self.weapon["Special Ability"] = "Locate Objects"
            case 20:
                self.weapon["Special Ability"] = "Wishes"

    def main(self):

        self.magic_weapon()
        self.weapon_bonus_melee()
        
        if "Special Enemy" in self.weapon:
            self.special_enemy()
        if "Special Ability" in self.weapon:
            self.special_ability()
            self.weapon_bonus_melee()
        if "Cursed" in self.weapon and "Special Ability" in self.weapon:
            del self.weapon["Special Ability"]

        print(self.weapon)

test = treasure_generator()
test.main()
