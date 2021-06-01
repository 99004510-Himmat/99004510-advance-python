#magic methods or dunders
class vector2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return vector2d(self.x + other.x, self.y + other.y)
    
first = vector2d(5, 7)
second = vector2d(3, 9)

result = first + second

print(result.x)
print(result.y)
print("------------------------\n")

#del method for garbage collection
a = 96
b = a
c = [a]

del a
b = 97
c[0] = 95
print("------------------------\n")

#data hiding
#weakly plrivate objects
class queue:
    def __init__(self, contents):
        self._hiddenlist = list(contents)
    
    def __push__(self, value):
        self._hiddenlist.insert(0, value)
        
    def __pop__(self):
        self._hiddenlist.pop(-1)
    
    def __repr__(self):
        return "Queue: {}".format(self._hiddenlist)

que = queue([1, 2, 4])
print(que)
que.__push__(0)
print(que)
que.__pop__()
print(que)
print("------------------------\n")

#strongly private objects
class spam:
    __egg = 5
    def print_egg(self):
        print(self.__egg)

s = spam()
s.print_egg()
print(s._spam__egg)
print(s.__egg)
print("------------------------\n")