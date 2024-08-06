from tkinter import *
from tkinter import font
from PIL import Image, ImageTk
import requests
from datetime import datetime
import pytz

def menu():
    
    menu_window = Tk()
    menu_window.geometry("390x600")
    menu_window.resizable(False, False)
    menu_window.title("Weather App")
    
    icon = PhotoImage(file="sunicon.png")
    menu_window.iconphoto(True, icon) 
    menu_window.config(background="#101010")
    
    main_font = font.Font(family="Aileron Bold", size=35)
    secondary_font = font.Font(family="Aileron Light", size=10)
    header = Label(menu_window,
                   text="Weatherly",
                   font=(main_font),
                   fg="White",
                   bg="#101010")
    header.place(x=75, y=50)
    
    desc = Label(menu_window,
                 text="Your Personalised Weather Companion",
                 font=(secondary_font),
                 fg="Grey",
                 bg="#101010")
    desc.place(x=77, y=140)
    
    city_entry = Entry(menu_window)
    city_entry.config(width=35)
    city_entry.place(x=83, y=280 )
    
    entry_desc = Label(menu_window,
                       text="City:",
                       font=(secondary_font),
                       fg="Grey",
                       bg="#101010")
    entry_desc.place(x=80, y=255)
    
    submitcity = Button(menu_window,
                        text=">",
                        font=(main_font,25),
                        fg="White",
                        bg="#101010",
                        relief=FLAT)
    submitcity.place(x=150,y=360)
    
    
    menu_window.mainloop()
    

menu()