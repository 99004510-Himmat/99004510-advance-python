#a program to take N (variable num in code template) positive numbers as input, and recursively calculate and output the first N numbers of the Fibonacci sequence (starting from 0).

num = int(input("Enter a number: "))


def fibonacci(n):
	n1 = 0
	n2 = 1
	count = 1
	temp = 0
	while(count <= n):
		print(temp)
		count += 1
		n1 = n2
		n2 = temp
		temp = n1 + n2
		

fibonacci(num)