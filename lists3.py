# Extension of list2 showcasing many useful operations on lists

while True:
	line = input("Enter a list of numbers: ")

	try:
		# List comprehension
		numbers = [int(word) for word in line.split()]
	except ValueError:
		print(f"Invalid input, the list contains an invalid number")
		continue
	break

# Slicing
print("First three elements:", numbers[:3])
print("All elements from the fourth:", numbers[3:])
print("One element out of two:", numbers[::2])
print("Reversed list:", numbers[::-1])

numbers.extend([1, 2, 3, 4])
print("Updated numbers:", numbers)


# Mapping elements
def halve(elem):
	return elem / 2

print("Halved list", list(map(halve, numbers)))
print("Halved list", [number / 2 for number in numbers])

# Filtering elements
def big_enough(elem):
	return elem > 10

print("Filtered list", list(filter(big_enough, numbers)))
print("Filtered list", [number for number in numbers if number > 10])

	