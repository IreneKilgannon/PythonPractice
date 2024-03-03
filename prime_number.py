num1 =  int(input("Please enter a number: "))

num2 = int(input("Please enter a second number: "))

prime_numbers = []

for num in range(num1, num2):
    isPrime = True
    for divisor in prime_numbers:
        if (num % divisor == 0):
            isPrime = False
            break

    if isPrime:
        prime_numbers.append(num)
print(prime_numbers)

