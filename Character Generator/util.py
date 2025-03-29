import random

# collection of utility methods that dont fit into classes

def dice_4d6():
    dice_one = random.randint(1,6)
    dice_two = random.randint(1,6)
    dice_three = random.randint(1,6)
    dice_four = random.randint(1,6)

    dice_array = [dice_one, dice_two, dice_three, dice_four]
    dice_array.remove(min(dice_array))
    stat_total = dice_array[0] + dice_array[1] + dice_array[2]
    return stat_total

def roll_1d4():
    d4 = random.randint(1,4)
    return d4

def roll_1d6():
    d6 = random.randint(1,6)
    return d6

def roll_1d8():
    d8 = random.randint(1,8)
    return d8

def starter_gold():
    dice_one = random.randint(1,6)
    dice_two = random.randint(1,6)
    dice_three = random.randint(1,6)

    total_dice = dice_one + dice_two + dice_three
    total_gold = total_dice * 10
    print(total_gold)
    return total_gold
