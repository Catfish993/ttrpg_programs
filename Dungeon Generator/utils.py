import random

def roll_2d6():
    dice_one = random.randint(1,6)
    dice_two = random.randint(1,6)

    total_dice = dice_one + dice_two
    return total_dice

def roll_d100():
    d100 = random.randint(1,100)
    return d100

