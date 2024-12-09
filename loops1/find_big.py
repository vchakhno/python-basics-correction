array = [18, 36, 14, 78, 39]

i = 0
while i < len(array):
	if array[i] > 100:
		print(i)
		break
	i+=1
else:
	print("Aucun element au dessus de 100")
print()

for i in range(len(array)):
	if array[i] > 100:
		print(i)
		break
else:
	print("Aucun element au dessus de 100")

print()

for i, elem in enumerate(array):
	if elem > 100:
		print(i)
		break
else:
	print("Aucun element au dessus de 100")

print()

i = 0
while i < len(array) and array[i] <= 100:
	i+=1
if i == len(array):
	print("Aucun element au dessus de 100")

print("78 is at index", array.index(78))