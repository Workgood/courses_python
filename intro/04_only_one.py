a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
print("Only one of the numbers a and b is even")
if(a%2 == 0 and b%2 != 0):
	print("This statement is true")
elif(a%2 !=0 and b%2 ==0):
	print("This statement is true")
else:
	print("This statement is false")
	

