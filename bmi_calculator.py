#bmi_calculator
print("***BMI CALCULATOR***")
height = input("Enter your height(cm)")
weight = input("Enter your weight(kg)")
BMI = int(weight)/int(height)/int(height)*10000
print("Your BMI is ",BMI)
if(int(BMI)<15):
	print("Acute underweight!")
elif(int(BMI)<20):
	print("Underweight.")
elif(int(BMI)<25):
	print("Normal weight.")
elif(int(BMI)<30):
	print("Overweight.")
else:
	print("Obesity!")
