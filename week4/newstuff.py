class_code = input("Enter an ITEC class code: ")

if 'ITEC' in class_code.upper():
    if len(class_code) == 9:
        print (class_code.upper())
    else:
        print("Error in input")
else:
    print("Error in input")