sec = int(input("Enter a number of seconds: "))
hour = sec//3600
minute =(sec%3600)//60
second = sec%60
print(hour,"h",minute,"m",second,"s","in",sec,"seconds")
