#!/usr/bin/env python3
from tkinter import *
import pyttsx3
from covid import Covid
root = Tk()
root.geometry("350x350")
root.title("Get Country Wise Covid-19 Data")
engine = pyttsx3.init()
def speakdata():
    covid=Covid()
    cases = []
    confirmed = []
    active = []
    deaths = []
    recovered = []
    try:
        root.update()
        countries = data.get()
        country_names = countries.strip()
        country_names = country_names.replace(" ", ",")
        country_names = country_names.split(",")
        for x in country_names:
            cases.append(covid.get_status_by_country_name(x))
            root.update()
        for y in cases:
            act="\nActive Cases in {} : {} ".format(y['country'],y['active'])
            con="\nTotal Cases in {} : {}".format(y['country'],y['confirmed'])
            dead="\nTotal Deaths in {} : {} ".format(y['country'],y['deaths'])
            rec="\nRecovered Cases in {} : {}".format(y['country'],y['recovered'])
            print(act)
            engine.say(act)
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
        data.set("Please Enter Correct Details")
        
Label(root, text="Enter all Countries Names\nFor whom you want to get\nCovid-19 data").pack()
Label(root, text="Enter Country name:").pack()
data = StringVar()
data.set("Enter Country Name")
entry = Entry(root, textvariable=data, width=50).pack()
Button(root, text="Speak Data", command=speakdata).pack()
root.mainloop()
