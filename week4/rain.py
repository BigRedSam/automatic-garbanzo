summer_months = ["June", "July", "August"]

rainfall = {}

for month in summer_months:
    rain = float(input(f"How much did it rain in {month}, in inches? "))
    rainfall[month] = rain
print()
print("Here's what you entered:")

for month , rain in rainfall.items():
    print(f"In {month} there was {rain} inches of rain. ")

total_rain = sum(rainfall.values())

months = len(rainfall)
average = total_rain / months

print()
print(f"The total amount of rain in {months} months is {total_rain} inches.")
print(f"The Average amount of rain per month is {average:.2f} inches")