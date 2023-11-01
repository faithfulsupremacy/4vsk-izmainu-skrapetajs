import requests
import os
import calendar
import datetime
from datetime import date,datetime

#menesi = ["jan", "feb", "mar", "apr", "mai", "sep", "okt", "nov", "dec"]

def main():
    year = str(datetime.now().year)
    month = str(datetime.now().month)
    day = str(datetime.now().day)
    
    if month == "9":
        menesis = "sep"
    elif month == "10":
        menesis = "okt"
    elif month == "11":
        menesis = "nov"
    elif month == "12":
        menesis = "dec"
    elif month == "1":
        menesis = "jan"
    elif month == "2":
        menesis = "feb"
    elif month == "3":
        menesis = "mar"
    elif month == "4":
        menesis = "apr"
    elif month == "5":
        menesis = "mai"

    

    print(year)
    print(month + " | " + menesis)
    print(day)

    #requests.get(url="https://4vsk.jelgava.lv/images/2023_2024/izmainas/nov/Izm_01_11_23.pdf")
main()