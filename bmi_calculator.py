#bmi_calculator
print("***BMI CALCULATOR***")
height = input("Enter your height(cm)")
weight = input("Enter your weight(kg)")
BMI = int(weight)/int(height)/int(height)*10000
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

