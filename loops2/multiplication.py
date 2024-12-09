while True:
	try:
		number = int(input("Enter a number: "))
		if number <= 0:
			raise ValueError()
	except ValueError:
		print("Error: please enter a positive integer.")
		continue

	print()
	print(f"{number}'s multiplication table")
	for i in range(1, 11):
		print(f"{number} x {i} = {number * i}")
	print()

	answer = input("Would you like to [retry] or [exit]? ")
	while answer not in ("retry", "exit"):
		print("Invalid option, chose either retry or exit.")
		answer = input("Would you like to [retry] or [exit]? ")
	if answer == "exit":
		break
