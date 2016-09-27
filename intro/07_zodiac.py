from datetime import datetime, date
usr_enter = input("Enter date (): ")
try:
    date = datetime.strptime(usr_enter, "%d.%m")
except ValueError:
    print("Invalid date!")


dates = {1:"Aquarius",2:"Pisces",3:"Aries",4:"Taurus",5:"Gemini",6:"Cancer",
         7:"Leo",8:"Virgo",9:"Libra",10:"Scorpio",11:"Sagittarius"}
try:
    if (date >= datetime.strptime("20.1", "%d.%m")) and (date <= datetime.strptime("18.2", "%d.%m")):
        print(dates[1])
    elif (date >= datetime.strptime("19.2", "%d.%m")) and (date <= datetime.strptime("20.3", "%d.%m")):
        print(dates[2])
    elif (date >= datetime.strptime("21.3", "%d.%m")) and (date <= datetime.strptime("19.4", "%d.%m")):
        print(dates[3])
    elif (date >= datetime.strptime("20.4", "%d.%m")) and (date <= datetime.strptime("20.5", "%d.%m")):
        print(dates[4])
    elif (date >= datetime.strptime("21.5", "%d.%m")) and (date <= datetime.strptime("21.6", "%d.%m")):
        print(dates[5])
    elif (date >= datetime.strptime("22.6", "%d.%m")) and (date <= datetime.strptime("22.7", "%d.%m")):
        print(dates[6])
    elif (date >= datetime.strptime("23.8", "%d.%m")) and (date <= datetime.strptime("22.9", "%d.%m")):
        print(dates[7])
    elif (date >= datetime.strptime("23.9", "%d.%m")) and (date <= datetime.strptime("22.10", "%d.%m")):
        print(dates[8])
    elif (date >= datetime.strptime("23.10", "%d.%m")) and (date <= datetime.strptime("22.11", "%d.%m")):
        print(dates[9])
    elif (date >= datetime.strptime("23.11", "%d.%m")) and (date <= datetime.strptime("21.12", "%d.%m")):
        print(dates[10])
    elif (date >= datetime.strptime("22.12", "%d.%m")) and (date <= datetime.strptime("19.1", "%d.%m")):
        print(dates[11])
except:
    print("Error!")
