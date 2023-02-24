import random
def main():
	inventory = []
	print(f"You find yourself stuck in a cave that collapsed. Search the cave to find any resources that can help you escape. You've only ever heard rumors of monsters dwelling in these caves. So be careful while you're exploring who knows what's down there.")
	name = input("What will your adventurer's name be?\n")
	print(f"Welcome brave adventurer {name}.")
	print(f"You look at your surroundings. Convienently, you find a torch on the wall.")
	torch = input(f"Would you like to take the torch with you? y/n\n")
	if torch == "y":
		inventory.append(torch)
		print("*Torch was added to your inventory*")
	elif torch == "n":
		print("You decide to leave the torch behind.")
	else:
		print(f"That is not a wise decision {name}")
	print(f"Now that you can finally see the whole room, you see that there is a hole that you can fit through.")
	hole = input(f"Would you like to pass through the hole? y/n\n")
	if hole == "y":
		print