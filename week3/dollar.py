pennies_count = int(input("How many pennies do you have on you?: "))
dollar = pennies_count % 100
dollar_count = pennies_count // 100
if dollar != 0:
    if pennies_count > 100:
        print("You have more than a dollar!")
    else:
        print("You have less than a dollar!")
else:
    if pennies_count == 0:
        print("You're penniless dude!")
    else:
        print(f"You have {dollar_count} dollars!")
