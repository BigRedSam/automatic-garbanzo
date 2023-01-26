jedi_count = input("How many Jedi? ")
sith_count = input("How many Sith? ")
if jedi_count > sith_count:
    print("Jedi Win!")
elif sith_count > jedi_count:
    print("Sith Win!")
else:
    print("Tie!")
    print(f"Jedi had {jedi_count} and Sith had {sith_count}!")