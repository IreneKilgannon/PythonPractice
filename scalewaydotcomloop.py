#countries = {"France": "Paris", "Japan": "Tokyo", "USA": "Washington DC"}

#for key in countries:
#    print(key)

#for value in countries.values():
 #   print(value)

'''numbers = [1, 10, 9, 4] 

for number in numbers:
    if number < 3:
        print(f'{str(number)} is not greater than 3')
    else:
        print(f"{str(number)} is greater than 3")

countries = ["France", "Japan", "the USA"] 

for country in countries:
    if country == "the USA":
        print('This country is the USA')
    else:
        print('This country is not the USA')

positive = [-1, 2, 3, 0, -4]

for item in positive:
    if item > 0:
        print(f"{item} is a positive number")
    elif item <0:
        print(f"{item} is a negative number")
    else:
        print(f"{item} is neither a negative or positive number")

x = 5

for x in range(5, -1, -1):
    if x == 5:
        print("Counting down")
        x = x - 1
    elif x == 0:
        print("Go!")
    else: 
        print(x)

foods = [["apple", "orange"], ["carrot", "cabbage"], ["chicken", "beef"]]

for food in foods:
    for food2 in food:
        print(food2)'''

conjugations = [["go", "went", "gone"], ["see", "saw", "seen"], ["take", "took", "taken"]]

for group in conjugations:
        print(f'The conjugations of {group[0]} are')
        for conjugation in group:
             print(conjugation)

'''list_numbers = [["50", "48", "-40"], ["57", "99", "80"], ["49, 40, 45"]]

for list_number in list_numbers:
    for number in list_number:
        if number>= 50:
            print(number)

numbers=[[50, 48, -40], [57, 99, 80], [49, 40, 45]]
  
for group in numbers:
    for number in group:
        if number >=50:
            print(number)
  
numbers = [[1, 3, 9], [3, 2], [4, 2, 1, 3]]
  
for group in numbers:
    if len(group) != 2:
        continue
    elif sum(group) <= 5:
        print(group, "contains two items which have a sum no greater than 5")


greater_than_ten = [3, 5, 11, 12, 1]

for number in greater_than_ten:
    if number > 10:
        print("This list contains a number higher than 10")
        break

# use the += operator and a variable instantiated outside the loop
numbers = [1, 5, 2, 6]
totals = 0

for number in numbers:
    totals += number
print("The sum of numbers in the list is", totals)

numbers = [1, 5, 2, 6]
max_number = numbers[0]

for number in numbers:
    if number > max_number:
        max_number = number

print("The highest number in the list is", max_number)

numbers = [3, 6, 1, 2, 5]
doubled = []

for number in numbers:
    double_number = number *2
    doubled.append(double_number)
print(doubled)'''

price_list = {"bread": 1.5, "jam": 2.75, "butter": 0.99, "sugar": 0.75}
less_than_one_euro = []
more_than_one_euro = []

for key, values in price_list.items():
    if values < 1:
        less_than_one_euro.append(key)
    else:
        more_than_one_euro.append(key)
print(f'Items that cost less than 1 euro: {less_than_one_euro}')

print(f'Items that cost more than (or exactly) 1 euro: {more_than_one_euro}')