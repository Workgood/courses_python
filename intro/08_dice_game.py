import random
print("***Dice game***")
balance = 100
while True:
	bet = int(input("Your bet:"))
	if balance<bet:
		print("Bet is too big!")
		continue
	elif bet<0:
		print("Enter only positive bet")
		continue
	num = int(input("Your dice:"))
	numc = random.randint(2,12)
	if num == numc:
		balance += 6*bet
		print("You guessed!")
	elif num > 12:
		print("Enter number between 2 and 12")
		continue
	else:
		balance -=bet
		print("You lose")
		print("Dice was",numc)
	print("Your balance: ",balance)
	if balance == 0:
		input("You lose all money! Press anything to exit")
		break
	choice = input("Would you like to continue (Y/N):")
	if choice == "Y":
		continue
	elif choice == "N":
		break
	else:
		print("Error!")
		break	
