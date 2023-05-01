from random import choice
with open("text.txt", "r") as file:
	a = file.readlines()
print(choice(a[0:5]))
