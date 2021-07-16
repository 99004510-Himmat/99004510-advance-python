# class methods
class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    @classmethod
    def perimeter(cls, side):
        return cls(4 * side)


border_len = Square.perimeter(6)
print("\n")
print(border_len.area())


# static method
# properties
class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @staticmethod
    def validate_toppings(toppings):
        if toppings == "pineapple":
            raise ValueError("No pineapples!")
        else:
            return True

    @property
    def pineapple_allowed(self):
        return False


ingredients = ["cheese", "onions", "meat"]
if all(Pizza.validate_toppings(i) for i in ingredients):
    pizza = Pizza(ingredients)
print(Pizza.pineapple_allowed())
