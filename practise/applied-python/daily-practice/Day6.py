print("------------------------\n")
#none type
print(None)
print("------------------------\n")

#dictionary
cell_phones = {"Samsung":"Galaxy", "Redmi":"Note", "OnePlus":"xt", "Apple":"iPhone"}
print(cell_phones)
print(cell_phones["Redmi"])
print("------------------------\n")

#assigning a value to non existing pair here
cell_phones["Microsoft"] = "Lumia"
print(cell_phones)
print("Redmi" in cell_phones)
print("Vivo" in cell_phones)
print("OnePlus" not in cell_phones)
print("------------------------\n")

#get method
print(cell_phones.get("Microsoft"))
print("------------------------\n")

fib = {1: 1, 2: 1, 3: 2, 4: 3}
print(fib.get(4, 0))
print(fib.get(7, 3))  #second argument is default value if not found at key
print("------------------------\n")


#tuples
tp = (1, 2, 4, (5, 6), 7)
print(tp[3])
print(tp[2:])
tpl = "a", "b", "d"
print(tpl)
print("------------------------\n")

#list slice
coach_carter = ["Diane", "Ernestine", "Hettie", "Jean", "Cookie", "Linda", "Deborah", "Grace"]
print(coach_carter[2:6]) #from 2 to 5, excl 6
print(coach_carter[:5])
print(coach_carter[::2]) #third argument is for steps
print("------------------------\n")

#list comprehensions 
square = [i*2 for i in range(6)]
print(square)
print("------------------------\n")

ek_ao = [i**2 for i in range(4) if i%2 == 0]
print(ek_ao)
print("------------------------\n")

#string formatting
num = [7, 6, 8]
msg = "Numbers: {0} {1} {2}".format(num[0], num[1], num[2])
print(msg)
print("------------------------\n")

print("{0}{1}{0}".format("abra", "cad"))
print("------------------------\n")

#string functions
#join function
print(",".join(["vikings","spartans","dothraki"]))

#split 
print("Vikings, Spartans, Dothrakis".split("."))

#replace 
print("Bjorn Lothbrok".replace("Lothbrok", "Ironside"))

#startwith and endswith
print("Ivar the Boneless was the youngest of sons of Ragnar".startswith("Ivar"))
print("Ivar the Boneless was the youngest of sons of Ragnar".endswith("Ragnar"))

#upper and lower case
print("Lagartha".upper())
print("InGRId".lower())

print("------------------------\n")