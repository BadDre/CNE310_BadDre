num_sides = int(input("Enter number of sides per dice: 4, 6, 8, 10, 12, or 20: "))
num_dice = int(input("How many dice? "))
damage_request = str(input("Is this a damage roll? "))

total_rolls = []
for die in range(num_dice):
    dice_roll = random.randint(1, num_sides)
    total_rolls.append(dice_roll)

total_damage = sum(total_rolls)



if damage_request == 'no' or damage_request == 'n':
    print("Your rolls were: " + str(total_rolls))
elif damage_request == 'yes' or damage_request =='y':
    print("You deal",total_damage,"damage!")
