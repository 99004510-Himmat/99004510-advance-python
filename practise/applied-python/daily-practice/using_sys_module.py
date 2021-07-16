"""
This program is to apply learnings of sys module
"""

import sys

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
opr = sys.argv[3]

if opr == "add":
    result = num1 + num2
    print(result)
elif opr == "sub":
    result = num1 - num2
    print(result)
elif opr == "mul":
    result = num1 * num2
    print(result)
elif opr == "div":
    result = num1 / num2
    print(result)
else:
    sys.exit("Invalid operation")
