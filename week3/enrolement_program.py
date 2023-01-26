credits = int(input("How many credits are you taking this semester: "))

if credits >= 12:
    print("You are a full time student this semeseter!")
elif credits >= 6:
    print("You are a half time student.")
else:
    print("You are less than a half time student.")