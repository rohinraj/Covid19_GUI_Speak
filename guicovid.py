#!/usr/bin/env python3
from tkinter import *           # initializing tkinter
import pyttsx3                  # pyttsx3 to speak
from covid import Covid         # Covid to get the data
root = Tk()
root.geometry("350x250")        # setting geometry
root.title("Get Country Wise Covid-19 Data")        # setting title
engine = pyttsx3.init()
def speakdata():
    covid=Covid()
    cases = []                  # To store datas in lists
    confirmed = []
    active = []
    deaths = []
    recovered = []
    try:
        root.update()           # updating root
        countries = data.get()          # getting countries names entered by the user
        country_names = countries.strip()
        country_names = country_names.replace(" ", ",")
        country_names = country_names.split(",")    # seperates the countries
        for x in country_names:
            cases.append(covid.get_status_by_country_name(x))       # getting required country data
            root.update()
        for y in cases:
            act="\nActive Cases in {} : {} ".format(y['country'],y['active'])       # string to print and speak
            con="\nTotal Cases in {} : {}".format(y['country'],y['confirmed'])
            dead="\nTotal Deaths in {} : {} ".format(y['country'],y['deaths'])
            rec="\nRecovered Cases in {} : {}".format(y['country'],y['recovered'])
            print(act)          # just printe it to know wheere the code reached 
            engine.say(act)     # Speaks th string
            engine.runAndWait()
            print(con)
            engine.say(con)
            engine.runAndWait()
            print(dead)
            engine.say(dead)
            engine.runAndWait()
            print(rec)
            engine.say(rec)
            engine.runAndWait()
    except Exception as e:
        data.set("Please Enter Correct Details")        # Error message for invalid Country names
        
Label(root, text="Enter all Countries Names\nFor whom you want to get\nCovid-19 data",font="Helvetica 15 bold").pack()
Label(root, text="Enter Country name:").pack()
data = StringVar()
data.set("India")
entry = Entry(root, textvariable=data, width=50).pack()
Button(root, text="Speak Data", command=speakdata).pack()
root.mainloop()
