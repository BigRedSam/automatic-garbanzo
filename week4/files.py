import os

try:
    os.makedirs('quotes')
except FileExistsError:
    pass


quote = """
"Every great developer you know got there by
by solving porblems they were unqualified to solve until
they actually did it."
- Patrick McKenzie
"""

path = os.path.join('quotes', 'mckenzie.txt')

f = open(path, 'w')
f.write(quote)
f.close()

newquote = """
"No one in the brief history of computing has ever written a piece
of perfect software. It's unlikely that you'll be the first." - Andy Hunt
"""

newpath = os.path.join('quotes', 'hunt.txt')

c = open(newpath, 'w')
c.write(newquote)
c.close