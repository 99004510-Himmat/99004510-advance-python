#numeric functions
lis = [2, 63, -9, 0, 99]
#sum
print(sum(lis))

#max and min
print(max(lis))
print(min(lis))

#absolute (distance from zero)
print(abs(-3))
print(abs(4))

#round
print(round(63.63))

print("------------------------\n")

#list functions
#enumerate function on lists
for v in enumerate(lis):
    print(v)
print("------------------------\n")

#higher order functions - means either taking functions as argumnets or returning them as results
def test(func, arg):
  return func(func(arg))

def mult(x):
  return x * x

print(test(mult, 2))
print("------------------------\n")

#pure functions - returns value which depend only on their argument
def sum(x, y):
    return (x + y)

print(sum(6, -2))
print("------------------------\n")

#anonymous functions using lambda
#function to return sqaure of a number
print((lambda x: x*x )(6))
#or can be assigned to a variable as
sqr = lambda x: x*x
print(sqr(6))
print("------------------------\n")

#map function
def add_four(x):
    return x+4

result = list(map(add_four, lis))
print(result)

#above function can be shortned using lambda as
res = list(map(lambda x: x+4, lis))
print(res)
print("------------------------\n")

#filter function
rest = list(filter(lambda x: x%2 == 0, lis))
print(rest)
print("------------------------\n")

#generators
def make_word():
  word = ""
  for ch in "spam":
    word +=ch
    yield word

print(list(make_word()))
print("------------------------\n")

#decorators
def decor(func):
    def wrap():
        print("====================")
        func()
        print("====================")
    return wrap

def print_tes():
    print("Hello Decor!")

decorated = decor(print_tes)
decorated()
print("------------------------\n")

#also decor
@decor 
def print_test():
    print("Hello Decor!")

print_test()