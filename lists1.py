level_names = ["Forsaken City", "Old Site", "Celestial Resort", "Golden Ridge", "Mirror Temple", "Reflection", "The Summit", "Core", "Farewell"]

first_level = level_names[0]
print("First level:", first_level)
last_level = level_names[-1]
print("Last level:", last_level)

level_names.append("The Summit V2")
print("Updated levels:", level_names)

level_names.pop(2) # third element!
print("Updated levels:", level_names)

print("\nAll levels:")
for level in level_names:
	print("-", level)