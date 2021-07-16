"""
using user defined packages
"""
import calculator

var1 = int(input("Enter first operand"))
var2 = int(input("Enter second operand"))

print("add \t sub \t mul \t div ")
opr = input("Enter operation to be performed")

if opr == "add":
    result = calculator.addition(var1, var2)
    print(result)
elif opr == "sub":
    result = calculator.diff(var1, var2)
    print(result)
elif opr == "mul":
    result = calculator.prod(var1, var2)
    print(result)
elif opr == "div":
    result = calculator.division(var1, var2)
    print(result)
else:
    print("Invalid operation")
