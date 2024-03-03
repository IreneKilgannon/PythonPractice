'''name = input("Please enter your first name:  ")
if len(name) < 5:
    surname = input("What is your surname: ")
    print(name.upper() + surname)
else:
    print(name.lower())'''



word = input("Please enter a word: ")
first = word[0]
rest = word[1:]
if first != "a" and first != "e" and first != "i" and first != "o" and first != "u":
    print(rest + first +"ay")
else:
    print(word + "way")



