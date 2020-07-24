#!/usr/bin/env python3
from tkinter import *           # initializing tkinter
import pyttsx3                  # pyttsx3 to speak
from covid import Covid         # Covid to get the data
root = Tk()
root.geometry("350x250")        # setting geometry
root.title("Get Country Wise Covid-19 Data")        # setting title
engine = pyttsx3.init()
rate = engine.getProperty('rate')
r=150
engine.setProperty('rate',r)
covid=Covid()
def speakdata():
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
def showdata():
    # importing matplotlib to show data graphically
    from matplotlib import pyplot as plt
    import matplotlib.patches as mpatches       # to scale the data we are importing patches
    cases = []      # Emoty lists for datas
    confirmed = []
    active = []
    deaths = []
    recovered = []
    try:
        root.update()       # updating root
        countries = data.get()
        country_names = countries.strip()
        country_names = country_names.replace(" ", ",")
        country_names = country_names.split(",")
        for x in country_names:
            cases.append(covid.get_status_by_country_name(x))
            # updating the root
            root.update()
        for y in cases:
            confirmed.append(y["confirmed"])            # appending list with each country data
            active.append(y["active"])
            deaths.append(y["deaths"])
            recovered.append(y["recovered"])
        confirmed_patch = mpatches.Patch(color='blue', label='confirmed')               # marking the color information on scaleusing patches
        recovered_patch = mpatches.Patch(color='green', label='recovered')
        active_patch = mpatches.Patch(color='red', label='active')
        deaths_patch = mpatches.Patch(color='black', label='deaths')
        plt.legend(handles=[confirmed_patch, recovered_patch, active_patch, deaths_patch])                  # using legend() to plot scale on graph
        for x in range(len(country_names)):                 # showing the data using graphs
            plt.bar(country_names[x], confirmed[x], color='blue')
            if recovered[x] > active[x]:
                plt.bar(country_names[x], recovered[x], color='green')
                plt.bar(country_names[x], active[x], color='red')
            else:
                plt.bar(country_names[x], active[x], color='red')
                plt.bar(country_names[x], recovered[x], color='green')
            plt.bar(country_names[x], deaths[x], color='black')
        plt.title('Current Covid Cases')            # setting the title of the graph
        plt.xlabel('Country Name')                  # giving label to x direction
        plt.ylabel('Cases(in millions)')            # giving label to y direction
        plt.show()                                  # showing the full graph
    except Exception as e:
        data.set("Please Enter Correct Details")        # Error message for invalid Country names
        
Label(root, text="Enter all Countries Names\nFor whom you want to get\nCovid-19 data",font="Helvetica 15 bold").pack()
Label(root, text="Enter Country names:").pack()
data = StringVar()
data.set("India")
entry = Entry(root, textvariable=data, width=40).pack()
Button(root, text="Speak Data", command=speakdata).pack()
Button(root, text="Show Data", command=showdata).pack()
root.mainloop()
