def byte_converter(megabyte):
    return megabyte * 1000000


def main():
    converted_number = float(input("How many megabytes do you have? "))
    print(f"You have {byte_converter(converted_number)} bytes!")


main()