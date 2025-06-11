"""
A list of tips and tricks to write better code.
"""

# 1. use a ternary operator to shorten code
condition = False

if condition:
    x = 1
else:
    x = 0

print(x)

# write the above in a single line using a ternary operator:
x = 1 if condition else 0
print(x)

# 2. add in underscores as separators to read large numbers

num1 = 10_000_000_000
num2 = 100_000_000

total = num1 + num2
print(f'{total:,}')  # prints 10,100,000,000

# 3. use context managers when working with files

# instead of opening and clossing the file...
f.open('test.txt', 'r')
file_contents = f.read()
f.close()

words = file_contents.split()
word_count = len(words)
print(word_count)

# ...use a context manager:
with open('test.txt', 'r') as f:
    file_contents = f.read()

# 4. use enumerate when you need a counter to loop over something
names = ['Corey', 'Chris', 'Dave', 'Travis']

for index, name in enumerate(names, start=1):
    print(index, name)

# 5. use zip when looping over two lists instead of enumerate
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']
universes = ['Marvel', 'DC', 'Marvel', 'DC']

# instead of writing this...
for index, name in enumerate(names):
    hero = heroes[index]
    print(f"{name} is actually {hero} from {universes}")

# use zip:
for name, hero in zip(names, heroes):
    print(f"{name} is actually {hero}")

# zip can also return tuples with all 3 values combined:
for value in zip(names, heroes, universes):
    print(value)

# 6. how to unpack values

# set an underscore for a variable you won't use
a, _ = (1, 2)
print(a)
# print(b)

# this won't work:
a, b, c = (1, 2, 3, 4, 5)
# this will work:
a, b, *c = (1, 2, 3, 4, 5)
# or:
a, b, *_ = (1, 2, 3, 4, 5)
# or:
a, b, *c, d = (1, 2, 3, 4, 5)

# 7. Getting and setting attributes on a certain object


class Person():
    pass


person = Person()

first_key = 'first'
first_val = 'Corey'

setattr(person, 'first', 'Corey')

print(person.first)
