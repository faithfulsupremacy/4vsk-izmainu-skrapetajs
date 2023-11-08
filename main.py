import requests
import os
import calendar
import datetime
from datetime import date,datetime
import urllib.request 

#menesi = ["jan", "feb", "mar", "apr", "mai", "sep", "okt", "nov", "dec"]

def main():
    year = str(datetime.now().year)
    month = str(datetime.now().month)
    day = str(datetime.now().day)
    syear = "23"
    

    if len(month) == 1:
        month = "0" + month
    if len(month) == 2:
        print("D: m2")

    if len(day) == 1:
        day = "0" + day
    if len(day) == 2:
        print("D: d2")


    if month == "9":
        menesis = "sep"
        nulmonth = "09"
    elif month == "10":
        menesis = "okt"
        nulmonth = "10"
    elif month == "11":
        menesis = "nov"
        nulmonth = "11"
    elif month == "12":
        menesis = "dec"
        nulmonth = "12"
    elif month == "1":
        menesis = "jan"
        nulmonth = "01"
    elif month == "2":
        menesis = "feb"
        nulmonth = "02"
    elif month == "3":
        menesis = "mar"
        nulmonth = "03"
    elif month == "4":
        menesis = "apr"
        nulmonth = "04"
    elif month == "5":
        menesis = "mai"
        nulmonth = "05"


    izmf = menesis + "/Izm_" + day + "_" + month + "_" + syear + ".pdf"
    todaylink = "https://4vsk.jelgava.lv/images/" + year + "_2024/izmainas/" + izmf

    print(year)
    print(month + " | " + menesis)
    print(day)
    print(todaylink)

    #requests.get(url="https://4vsk.jelgava.lv/images/2023_2024/izmainas/nov/Izm_01_11_23.pdf")

main()