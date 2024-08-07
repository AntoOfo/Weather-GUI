from tkinter import *
from tkinter import font
from PIL import Image, ImageTk
import requests
from datetime import datetime
import pytz

def icons():
    global snow_icon, clear_icon, foggy_icon, thunder_icon, drizzle_icon, rain_icon, cloudy_icon
    snow = Image.open("snow.png")
    snow_resized = snow.resize((100,100), Image.LANCZOS)
    snow_icon = ImageTk.PhotoImage(snow_resized)
    
    clear = Image.open("clear-sky.png")
    clear_resized = clear.resize((100,100), Image.LANCZOS)
    clear_icon = ImageTk.PhotoImage(clear_resized)
    
    foggy = Image.open("foggy.png")
    foggy_resized = foggy.resize((100,100), Image.LANCZOS)
    foggy_icon = ImageTk.PhotoImage(foggy_resized)

    thunderstorm = Image.open("thunderstorm.png")
    thunderstorm_resized = thunderstorm.resize((100,100), Image.LANCZOS)
    thunder_icon = ImageTk.PhotoImage(thunderstorm_resized)
    
    drizzle = Image.open("drizzle.png")
    drizzle_resized = drizzle.resize((100,100), Image.LANCZOS)
    drizzle_icon = ImageTk.PhotoImage(drizzle_resized)
    
    rain = Image.open("rain.png")
    rain_resized = rain.resize((100,100), Image.LANCZOS)
    rain_icon = ImageTk.PhotoImage(rain_resized)
    
    cloudy = Image.open("cloudyicon.png")
    cloudy_resized = cloudy.resize((100,100), Image.LANCZOS)
    cloudy_icon = ImageTk.PhotoImage(cloudy_resized)
def weather_window():
    
    weather_window = Toplevel()
    weather_window.geometry("390x600")
    weather_window.resizable(False, False)
    weather_window.title("Weather")
    
    weather_window.config(background="#101010")
    
    city_header = Label(weather_window,
                        text="Testing",
                        font=(main_font),
                        fg="White",
                        bg="#101010")
    city_header.pack(pady=70)
    
    wind_desc = Label(weather_window,
                      text="Wind speed: 0%",
                      font=(secondary_font, 12),
                      fg="Grey",
                      bg="#101010")
    wind_desc.place(x=130, y=140)
    
    weather_icon = Label(weather_window,
                         image=cloudy_icon,
                         bg="#101010")
    weather_icon.place(x=130, y=210)

    weather_window.mainloop()



def menu():
    global main_font, secondary_font

    menu_window = Tk()
    menu_window.geometry("390x600")
    menu_window.resizable(False, False)
    menu_window.title("Home Screen")
    
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
                        relief=FLAT,
                        command=weather_window)
    submitcity.place(x=150,y=360)
    
    icons()
    menu_window.mainloop()
    

menu()