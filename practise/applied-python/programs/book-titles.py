#  a books.txt file, which includes the book titles, each one written on a separate line.
# Read the title one by one and output the code for each book on a separate line.

# For example, if the books.txt file contains:
# Some book
# Another book

# Your program should output:
# S9
# A12

file = open("applied-python/src/books.txt", "r")

lines = file.readlines()
for line in lines:
    line = line.strip("\n")
    char_sz = len(line)
    print(line[0] + str(char_sz))


file.close()