# write a list comphrension that gives x*y if x is greater than or equal to 5 but less that 10.
# and gives x/y when x = 10

x = 1, 3, 5, 6, 8, 10, 20
y = 2

my_list = [x*y if x >= 5 and x < 10 else x/y for x in x]
print(my_list)