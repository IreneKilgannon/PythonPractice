
# A for loop to carry out the required calculations.


# Ask the user to input a positive integer. 
def collatz():
    numbers = []
    numbers.append(number)
    for number in numbers:
    # Break out of the loop when the number is 1.
        if number == 1:
            break

    # Divide the number by two if it is greater that 1 and even. Append the result to the numbers list.
        elif number % 2 == 0:
            numbers.append(number//2)

    # For odd numbers append the result of number*3 + 1 to the list.
        else:
            numbers.append(number*3 + 1)
    for value in numbers:
    # use the end paramater to print the values in numbers list on the same line.
        print(f'{value} ', end = '')

'''

number = int(input("Please enter a positive integer: "))

global num

def check_number():
    if num < 0:
        print(f"You entered {number}, which is not a positive integer")
    elif type(number) != int:
        print(f"Number must be a positive integer")
    else:
        collatz()

check_number()
'''

try:
    number = int(input("Please enter a positive integer: "))
    if number <= 0:
        print(f"You entered {number}, which is not a positive integer")
    else:
        numbers = []
        numbers.append(number)
        for number in numbers:
    # Break out of the loop when the number is 1.
            if number == 1:
                break

    # Divide the number by two if it is greater that 1 and even. Append the result to the numbers list.
            elif number % 2 == 0:
                numbers.append(number//2)

    # For odd numbers append the result of number*3 + 1 to the list.
            else:
                numbers.append(number*3 + 1)
        for value in numbers:
    # use the end paramater to print the values in numbers list on the same line.
            print(f'{value} ', end = '')
except ValueError:
    print(f'Number must be an integer.')


