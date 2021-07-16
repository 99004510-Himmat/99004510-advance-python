"""
 a function that takes multiple words as its argument and returns a concatenated version of those words separated by dashes (-).
The function should be able to take a varying number of words as the argument.
"""


def concatenate(*args):
    sep = "-"
    for i in range(len(args)):
        return sep.join(args)


print(concatenate("I", "love", "Python", "!"))