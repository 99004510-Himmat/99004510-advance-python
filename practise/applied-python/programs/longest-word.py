# Given a text as input, find and output the longest word.

txt = input("Enter some sentence")
#example- this is a sentence
size = []
new_ls = []

for s in txt.split(" "):
    size.append( len(s))
    new_ls.append(s)

ind = size.index(max(size))

print(new_ls[ind])