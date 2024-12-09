number = int(input("Enter the starting number: "))
print(number)

# def modulo(a, b):
# 	return a - a // b * b

while number != 1:
	if number % 2 == 0:
		number //= 2
	else:
		number = number * 3 + 1
	print(number)