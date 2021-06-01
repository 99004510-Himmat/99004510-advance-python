#this is to check the applications of function only so no testing here
def sum(var1, var2):
    print("Sum: " + str(var1 + var2))

def difference(var1, var2):
    print("Diff: " + str(var1 - var2))

def product(var1, var2):
    print("Product: " + str(var1 * var2))

def quotient(var1, var2):
    print("Quotient: " + str(var1 / var2))

def remainder(var1, var2):
    print("Remainder: " + str(var1 % var2))

a = int(input("Enter first number "))
b = int(input("Enter second number "))

res_sum = sum(a, b)
res_diff = difference(a, b)
res_prod = product(a, b)
res_qt = quotient(a, b)
res_rem = remainder(a, b)