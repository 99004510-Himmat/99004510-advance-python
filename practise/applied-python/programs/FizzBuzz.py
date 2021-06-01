# It takes an input n and outputs the numbers from 1 to n.
# For each multiple of 3, print "Solo" instead of the number.
# For each multiple of 5, prints "Learn" instead of the number.
# For numbers which are multiples of both 3 and 5, output "SoloLearn".

n = int(input("enter a number1"))

for x in range(1, n):
    if(x % 2 == 0):
        print(x)
        continue
    if x % 3 == 0 and x % 5 == 0:
        print("SoloLearn")
    elif x % 3 == 0:
        print("Solo")
    elif x % 5 == 0:
        print("Learn")
    else:
        print(x)
    