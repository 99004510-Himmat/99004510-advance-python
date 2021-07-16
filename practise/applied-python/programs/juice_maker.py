"""
 if you add an Orange juice with 1.0 capacity and an Apple juice with 2.5 capacity, the resulting juice should have:
name: Orange&Apple
capacity: 3.5
"""


class Juice:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def __str__(self):
        return self.name + ' (' + str(self.capacity) + 'L)'

    def __add__(self, other):
        self.name += "&" + str(other.name)
        self.capacity += other.capacity
        return self.__str__


a = Juice('Orange', 1.5)
b = Juice('Apple', 2.0)

result = (a.__add__(b)())
print(result)
