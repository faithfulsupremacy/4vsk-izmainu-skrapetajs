import requests
import datetime
from datetime import date,datetime,timedelta
import os
import pytz
import time

#menesi = ["jan", "feb", "mar", "apr", "mai", "sep", "okt", "nov", "dec"]
attempt = 0

def main():

    nowtime = datetime.now(pytz.timezone('Europe/Riga'))
    if nowtime.hour < 8:
        datevar = nowtime
    else:
        datevar = nowtime + timedelta(days=1)

    day = str(datevar.day)
    month = str(datevar.month)
    year = str(datevar.year)
    syear = datevar.strftime("%y")


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
    todaylink = "https://4vsk.jelgava.lv/images/2023_2024/izmainas/" + izmf
    segments = todaylink.split('/')
    filename = segments[-1]

    print(year)
    print(month + " | " + menesis)
    print(day)
    print(todaylink)
    print(filename)
    print("\n\n\n")

    #try:
    #    responsecheck = requests.get(url + (menesis + "/Izm_" + day + "_" + month + "_" + syear + "_5.pdf"))
    #except:
    #    print("5. revīzija neeksistē.")
    #    foundRev = False
   # 
   # if foundRev == True:
   #     print("Revīzija atrasta. ")
   # else:
   #     try:
   #         responsecheck = requests.get(url + (menesis + "/Izm_" + day + "_" + month + "_" + syear + "_4.pdf"))
   #     except:
   #         print("4. revīzija neeksistē.")
   #         foundRev = False
   #     if foundRev == True:
   #         print("Revīzija atrasta. ")
   #     else:
   #         try:
   #             responsecheck = requests.get(url + (menesis + "/Izm_" + day + "_" + month + "_" + syear + "_3.pdf"))
   #         except:
   #             print("3. revīzija neeksistē.")
   #             foundRev = False

    #url = "https://4vsk.jelgava.lv/images/" + year + "_2024/izmainas/" + menesis + "/Izm_" + day + "_" + month + "_" + syear + "_4.pdf"
    #url = "https://4vsk.jelgava.lv/images/2023_2024/izmainas/nov/Izm_22_11_23.pdf"
    #response = requests.get(url)
    #file = open("faili/" + izmD, "wb")
    #ile.write(response.content)

    responses = requests.get(url=todaylink)
    files = open("faili/" + filename, "wb")
    files.write(responses.content)
    files.close()

    try:
        fline=open("faili/" + filename, encoding="utf8").readline().rstrip()    
    except:
        print("Fails ir pareizs.")
    else:
        print("Fails ir nepareizs.")
        os.remove("faili/" + filename)

    #print("start")
    #time.sleep(315)

while True:
    main()
    attempt =+ 1
    print(attempt)
    time.sleep(300)