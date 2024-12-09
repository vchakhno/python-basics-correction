from typing import List

# Ints are passed by value
# which means they are copied when passed as an argument,
# and changing one inside the function won't affect the real one
def add_two(a: int):
	a += 2

number = 60
add_two(number)
print(number)

# Lists are passed by reference
# which means they are the same in and out of the function,
# and changing one inside the funcition *WILL* affect the real one

def add_elem_two(a: List[int]):
	a.append(2)

numbers = [60]
add_elem_two(numbers)
print(numbers)