# list operations
alpha = ["a", "b", "c", "d",]
# in to check if item is in list
print("b" in alpha)
print("e" in alpha)
print(not "e" in alpha)
print("------------------------\n")

# list functions
# append function
alpha.append("e")
print("e" in alpha)
# length of list
print(len(alpha))
print("------------------------\n")

num = [1, 2, 3, 5, 2]
# insert
num.insert(3, 4)
print(num)
# index to find location of item
print(num.index(3))
# other list functions
print(max(num))
print(min(num))
print(num.count(2))
num.remove(2)
print(num)
num.reverse()
print(num)
print("------------------------\n")

# loops
# while
a = 5
while a >= 3:
    print(a)
    a -= 1
print("------------------------\n")

# break in loops
b = 7 
while b >= 2:
    print(b)
    b -= 1
    if b == 3:
        print("Chinna Thala is here ")
        break
    
print("------------------------\n")

# continue
c = 7 
while c >= 2:
    print(c)
    c -= 1
    if c == 3:
        print("Chinna Thala is here so skip it ")
        continue
    
print("------------------------\n")

# for loop
st = "Thor has lost his hammer, but it will come back by it self."
count = 0
for var in st:
    if var == "t":
        count += 1
print("Number of times 't' in st: " + str(count))
print("------------------------\n")

# range
# one argument
print(list(range(5)))   # starts from 0 to 5
# two argument
print(list(range(2, 5)))    # starts from 2 to 4, 5 excluded
# three argument
print(list(range(1, 10, 2)))    # starts from 1 to 10 but only with addition of 2, thus odd numbers here
print("------------------------\n")

# functions
def display_skipper():
    print("Thala")

display_skipper()
print("------------------------\n")

# comments
# single line Commnets using #
print("this line is not commented \n")
# this is single line comment

# multi line comment using """
"""
this is 
a multi line
comment 
in 
pyhton
"""
print("------------------------\n")

# using modules
from math import sqrt as root
num = 36
print(root(num))
print("------------------------\n")

# excemption handlig
try:
    num1 = 5
    num2 = 0
    print(num1 / num2)
    print("line after excemption \n")
except ZeroDivisionError:
    print("Error found\n Zero Division error \n")
finally:
    print("this is finall print\n")
print("------------------------\n")

# assertion
abc = 15
# assert abc == 14, "they are not same"
print("------------------------\n")

# file handling
# to open a file
file_ptr = open("applied-python/src/sample.txt", "w")
file_ptr.close()