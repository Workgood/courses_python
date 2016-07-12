print("Please enter two radii(R1>R2)")
r1 = int(input("R1: "))
r2 = int(input("R2: "))
if(r1<=r2):
	print("Please enter R1>R2")
else: 
	s1 = r1**2
	s2 = r2**2
	s3 = (s1-s2)
	print("Square of circle with R1 =",s1,"п, with R2 =",s2,"п")
	print("Square of ring =",s3,"п")
