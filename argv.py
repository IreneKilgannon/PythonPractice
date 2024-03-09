import sys

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
