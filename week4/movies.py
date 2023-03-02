import random

favorites = ["Fight Club", "Clerks", "The Matrix", "Jaws"]

random.shuffle(favorites)

for index, movie in enumerate(favorites):
    print(f'{index + 1}. {movie}')

favorites.sort()
favorites.reverse()
print(favorites)

# for movie in favorites:
#     print(movie)

# favorites.append("The Rock")
# print(favorites)

# last_movie = favorites.pop()
# print(favorites)
# favorites.remove("Jaws")
# print(favorites)

