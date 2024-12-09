while True:
	line = input("Enter a list of numbers: ")

	numbers = []
	try: 
		for word in line.split():
			numbers.append(int(word))
	except ValueError:
		print(f"Invalid input, {word} is not a number")
		continue
	break

print(numbers)
print("Sum of all numbers:", sum(numbers))
print("Average of all numbers:", sum(numbers) / len(numbers))
print("Smallest of all numbers:", min(numbers))
print("Greatest of all numbers:", max(numbers))
print("Sorted list:", sorted(numbers))

print("First three elements:", numbers[:3])
print("All elements from the fourth:", numbers[3:])
print("One element out of two:", numbers[::2])

numbers.extend([1, 2, 3, 4])
print("Updated numbers:", numbers)

def halve(elem):
	return elem / 2

print("Halved list", list(map(halve, numbers)))
print("Halved list", [number / 2 for number in numbers])


def big_enough(elem):
	return elem > 10

print("Filtered list", list(filter(big_enough, numbers)))
print("Filtered list", [number for number in numbers if number > 10])

# def add_two(a: int):
# 	a += 2

# def add_elem_two(a: List[int]):
# 	a.append(2)

# number = 60
# add_two(number)
# print(number)



# numbers = [60]
# add_elem_two(numbers)
# print(numbers)
	