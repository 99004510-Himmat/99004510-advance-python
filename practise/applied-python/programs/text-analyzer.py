#a program that analyzes a sample file to find what percentage of the text each character occupies.
def char_count(text, char):
    count = 0
    for c in text:
        if(c == char):
            count += 1
    return count

with open("applied-python/src/sample.txt") as f:
    text = f.read()

for char in "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    perc = 100 * char_count(text, char) / len(text)
    print("{0} - {1}".format(char, round(perc, 2)))  #round to 2 float 
