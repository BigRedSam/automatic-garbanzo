try:
    f = open('does_not_exist.txt', 'r')
    lines = f.readlines()
    f.close()
    print(lines)
except FileNotFoundError:
    print('Error - files does not exist')