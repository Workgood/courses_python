#bmi_calculator
print("***BMI CALCULATOR***")
height =int(input("Enter your height(cm)"))
weight =int(input("Enter your weight(kg)"))
BMI = (weight*10000)/(height**2)
print("Your BMI is ",BMI)
if(BMI<15):
	print("Acute underweight!")
elif(BMI<20):
	print("Underweight.")
elif(BMI<25):
	print("Normal weight.")
elif(BMI<30):
	print("Overweight.")
else:
	print("Obesity!")

