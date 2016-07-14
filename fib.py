N =int(input("Enter index of requested Fibonacci number: "))
f1 =0
f2 =1
if N == 0:
	f2 = 0
n =1
while n<N:
	f1,f2 = f2,f2+f1
	n+=1
print(f2)
