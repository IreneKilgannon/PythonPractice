import math

'''radius = int(input("Enter radius of the circle: "))
area = math.pi * radius**2
print(round(area, 2))'''


input("1) Square  \n2) Triangle")
user = int(input("Please enter a number: "))

if user == 1:
    side = int(input("What is the length of the side?"))
    area = side *2
    print(area)
elif user == 2:
    base = int(input("What is the length of the base?"  ))
    height = int(input("What is the height?"  ))
    area_triangle = 0.5 * base * height
    print(area_triangle)
else:
    print("Error, only 1 or 2 please")