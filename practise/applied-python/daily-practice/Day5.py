#reading from file
file = open("applied-python/src/sample.txt", "r")
for i in range(21):
    print(file.read(4)) #each line will print 4 bytes
file.close()
print("------------------------\n")

#readlines() method 
fp = open("applied-python/src/sample.txt")
print(fp.readlines())
fp.close()
print("------------------------\n")

#writing into files
#w mode will overwrite the file's content 
file_me_likhte_he = open("applied-python/src/otherSample.txt", "w")
file_me_likhte_he.write("This is new text written in this file using 'w' mode in open.")
file_me_likhte_he.close()
#to read that
to_read_from = open("applied-python/src/otherSample.txt", "r")
print(to_read_from.readlines())
to_read_from.close()
print("------------------------\n")

#a mode will append and not delete the existing content
adding_this = open("applied-python/src/sample.txt", "a")
adding_this.write("In the series he is the eldest son of the great Ragnar Lothbrok.")
adding_this.close

#using with will always close the file even if exception occur
with open("applied-python/src/sample.txt") as f:
    print(f.read())
    #no need to close the file as with does it automatically
print("------------------------\n")