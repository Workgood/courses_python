#!/usr/bin/env python3

from datetime import datetime, date

zodiacs = {
    datetime.strptime("20.1", "%d.%m"): "Aquarius",
    datetime.strptime("19.2", "%d.%m"): "Pisces",
    datetime.strptime("21.3", "%d.%m"): "Aries",
    datetime.strptime("20.4", "%d.%m"): "Taurus",
    datetime.strptime("21.5", "%d.%m"): "Gemini",
    datetime.strptime("22.6", "%d.%m"): "Cancer",
    datetime.strptime("23.8", "%d.%m"): "Leo",
    datetime.strptime("23.9", "%d.%m"): "Virgo",
    datetime.strptime("23.10", "%d.%m"): "Libra", #doesn't find this month
    datetime.strptime("23.11", "%d.%m"): "Scorpio",
    datetime.strptime("22.12", "%d.%m"): "Sagittarius"
}


def get_zodiac(zodiacs, date):
    zodiac_dates = sorted(list(zodiacs.keys()))   
    for i in zodiac_dates:
        if i == date:
            return zodiacs.get(i)
                


try:
    input_date = datetime.strptime(str(input("Enter date (): ")), "%d.%m")
    print(get_zodiac(zodiacs, input_date))
except ValueError:
    print("Invalid date!")
