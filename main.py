import requests
import os
import datetime
from datetime import date,datetime
import time
import subprocess as sub

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

    izmD = "Izm_" + day + "_" + month + "_" + syear + ".pdf"
    izmf = menesis + "/Izm_" + day + "_" + month + "_" + syear + ".pdf"
    todaylink = "https://4vsk.jelgava.lv/images/" + year + "_2024/izmainas/" + izmf

    print(year)
    print(month + " | " + menesis)
    print(day)
    print(todaylink)
    print(izmD + "\n\n\n")




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

    responses = requests.get(url="https://4vsk.jelgava.lv/images/2023_2024/izmainas/nov/Izm_22_11_24.pdf")
    files = open("faili/" + "htmlPDF.txt", "wb")
    files.write(responses.content)

    #with open('faili/htmlPDF.txt') as f:
    #    first_line = f.readline()
    #    print(first_line)

    try:
        fline=open("faili/Izm_22_11_23.txt", encoding="utf8").readline().rstrip()    
        print(fline)
    except:
        print("Fails ir pareizs.")
    else:
        print("Fails ir nepareizs.")
    
    fline=open("htmlPDF.txt", encoding="utf8").readline().rstrip()    
    print(fline)

    #print("start")
    #time.sleep(315)

main()
input("")