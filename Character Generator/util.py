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