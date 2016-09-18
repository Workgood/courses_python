while True:
	print("Options:")
	print("Enter 'add' to add two numbers")
	print("Enter 'sub' to subtract two numbers")
	print("Enter 'mul' to multiply two numbers")
	print("Enter 'div' to divide two numbers")
	print("Enter 'q' to end the program")
	user_input = input(": ")
	if user_input == "q":
		break
	elif user_input == "add":
		a = float(input("Enter first number:"))
		b = float(input("Enter second number:"))
		s =a+b 
		print("{} + {} = {}".format(a,b,s))
	elif user_input == "sub":
                a = float(input("Enter first number:"))
                b = float(input("Enter second number:"))
                s =a-b
                print("{} - {} = {}".format(a,b,s))
	elif user_input == "mul":
                a = float(input("Enter first number:"))
                b = float(input("Enter second number:"))
                s =a*b
                print("{} * {} = {}".format(a,b,s))
	elif user_input == "div":
		a = float(input("Enter first number:"))
		b = float(input("Enter second number:"))
		if b == 0:
			print("You can not divide by zero!")
		else:
                	s =a/b
                	print("{} / {} = {}".format(a,b,s))

	else:
		print("Unknow input!")

