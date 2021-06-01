#  a function to take the Celsius value as an argument and return the corresponding Fahrenheit value.

celsius = int(input("Enter temperature in Celsius: "))

def conv(c):
    #your code goes here
    return (9/5 * c + 32)
    

fahrenheit = conv(celsius)
print(fahrenheit)