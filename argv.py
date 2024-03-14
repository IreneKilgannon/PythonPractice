#import sys
'''
print('Script name:', sys.argv[0])
for i, arg in enumerate(sys.argv[1:], start=1):
    print(f'Argument {i}:', arg)

# Output when running: python3 your_script.py arg1 arg2
# Script name: your_script.py
# Argument 1: arg1
# Argument 2: arg2

#argv returns a list of the arguments passed to a python script where argv[0] contains the name of the python script.

# All items in sys.argv are strings, so may need to convert them to the appropriate type.
    
#https://ioflood.com/blog/python-args/#:~:text=argv%20is%20a%20list%20in,count%20the%20number%20of%20arguments.
    
import sys

if len(sys.argv) < 2:
    print('Error: missing argument')
    sys.exit(1)

# Output when running: python3 your_script.py
# Error: missing argument
    

# https://realpython.com/python-counter/

# Creating a dictionary to count several objects at once. The dictionary keys will store the objects you want to count. 
# The Dictionary values will hold the number of repetitions of an object

word = "mississippi"
counter = {}

for letter in word:
    if letter not in counter:
        counter[letter] = 0
    counter[letter] += 1


counter'

from collections import Counter

letters = Counter("mississippi")
letters["p"]

letters["s"]


for letter in letters:
    print(letter, letters[letter])

for letter in letters.keys():
    print(letter, letters[letter])

for count in letters.values():
    print(count)

for letter, count in letters.items():
    print(letter, count)


from collections import Counter

letters = Counter("mississippi")
print(letters["m"])


# letters.py

from collections import Counter

def count_letters(filename):
    letter_counter = Counter()
    with open(filename) as file:
        for line in file:
            line_letters = [
                char for char in line.lower() if char.isalpha()
            ]
            letter_counter.update(Counter(line_letters))
    return letter_counter

from letters import count_letters
letter_counter = count_letters("pyzen.txt")

for letter, count in letter_counter.items():
    print(letter, "->", count)

for letter, count in letter_counter.most_common(5):
    print(letter, "->", count)'''
  
#Python - Command Line Arguments https://www.youtube.com/watch?v=ZQ9JO0e9468

import sys

my_txt_file = sys.argv[1]

with open(my_txt_file, 'r') as f:
    f_cont = f.read().count('e')

print(f_cont)


'''count = 0 taken from es.py

n = len(sys.argv)

for i in range(1, n):
    if i == 'e':
        count +=1
print(count)
    

for arg in sys.argv:
    with open(arg[1], 'r') as f:
       data = f.read()
       print(counting(data))
'''