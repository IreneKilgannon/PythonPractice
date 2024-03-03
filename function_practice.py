# https://www.w3resource.com/python-exercises/python-functions-exercises.php

# Question 1, write a function to find the max of three numbers

'''def maximum(a, b, c):
    return max(a, b, c)

print(maximum(10, 2, 4))

# Without using max()
def max_of_two(a, b):
    if a>b:
        return a
    else:
        return b

def max_of_three(a, b, c):
    return max_of_two(a, max_of_two(b, c))

print(max_of_three(10, 43, 2))

# Question 2 Write a function to sum all the numbers in a list

def sum_numbers_in_list(*numbers):
    total = 0
    for i in numbers:
        total += i
    return total

print(sum_numbers_in_list(12, 3, 4, 90))

def sum(numbers):
    # Initialize a variable 'total' to store the sum of numbers, starting at 0
    total = 0
    
    # Iterate through each element 'x' in the 'numbers' list
    for x in numbers:
        # Add the current element 'x' to the 'total'
        total += x
    
    # Return the final sum stored in the 'total' variable
    return total

# Print the result of calling the 'sum' function with a tuple of numbers (8, 2, 3, 0, 7)
print(sum((8, 2, 3, 0, 7)))

# Question 3 Muplitply all the numbers in a list

def multiply(*args):
    total = 1
    for i in args:
        total *= i
    return total
print(multiply(1,2,3,4,5))

# Question 4 Write a program to reverse a string

def reverse(string):
    rev_string = ''
    index = len(string)
    while index > 0:
        rev_string += string[index -1]
        index = index -1
    return rev_string
    
print(reverse("1234abcd"))

# Question 5, calculate the factorial of a number. Factorial 4 = 4 x 3 x 2 x 1

def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number-1)
    
print(factorial(5))

# Question 6 check to see if a number falls within a given range

def given_range(number, a, b):
    if b>a:
        if number >= a and number <= b:
            return f"{number} is in range of {a} and {b}"
        else:
            return f"{number} is not in range of {a} and {b}"
    else:
        return f"{b} should be greater than {a}"
    

print(given_range(1, 0, 5))

# Question 7 function that accepts a string and counts the number of upper and lower case letters

def counts_upper_lower(string):
    count_upper = 0
    count_lower = 0
    for i in string:
        if i.isupper():
            count_upper += 1
        else:
            count_lower += 1

    return f"No of upper case characters is {count_upper} /n No of lower case characters is {count_lower}"

print(counts_upper_lower("The Quick Brown Fox"))


# Q9 Write a function that takes a list and returns a new list with distinct elements fro the first list 

def unique_list(numbers):
    x = []
    for item in numbers:
        if item not in x:
            x.append(item)
    return x

print(unique_list([1,2,3,3,4,5,6,7,5 ,9,9,1, 7]))

# Q9 Takes in a number and checks if the number is prime or not

def check_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for x in range(2, n):
            if n % x == 0:
                return False
        return True

print(check_prime(9))

        


#Q10 Print the even numbers in a list
    
def check_even(number):
    even_lists = []
    for item in number:
        if item %2 == 0:
            even_lists.append(item)
    return even_lists
        
print(check_even([1, 2, 3, 4, 5, 6, 7, 8, 9]))

#Q11 Write a function to see if a number is 'Perfect' or not. 
#A perfect number is a positive integer that is equal to the sum of its proper positive devisors.
# eg 6 is perfect as it is the sum of 1, 2 and 3.

#Q12 Checks if a string is a pallindrome or not

def pallindrome(string):
    rev_string = ''
    index = len(string)
    while index > 0:
        rev_string += string[index -1]
        index = index -1
    if rev_string == string:
        return True
    else:
        return False
    
print(pallindrome("nlvan"))

#Q13 Write a function that prints out the first n row of Pascals triangle

def pascals_triangle():
    triangle = 


#Q14 write a function to check if a string is a pangram or not. A pangram is a sentence containing every letter of the alphabet
    
def pangram(abc):
    for x in abc:
        if x in '''

#Q15 Write a progam that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting

def hyphen_sorted(a-b-c):
    
