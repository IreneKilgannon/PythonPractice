'''user = input("Please enter your name: ")
num = int(input("Enter a number: "))


for x in range(0, num):
    for i in name:
        print(i)


user2 = int(input("Enter a number between 1 and 12: "))
for i in range(1,13):
    print(f'{i} times {user2} is {i*user2}')

num = int(input("Enter a number <50: "))
for i in range(50, num-1, -1):
    print(i)

user = input("Please enter your name: ")
num = int(input("Enter a number: "))

if num < 10:
    for x in range(0, num):
        print(user)
else:
    for x in range(0,3):
        print("Too high")'''

total = 0

for x in range(0,5):
    num = int(input("Enter a number: "))
    inc = input("Do you want the number included: ")
    if inc == "yes":
        new_total = total + 1
print(new_total)