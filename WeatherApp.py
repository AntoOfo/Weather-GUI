from tkinter import *
from tkinter import font
from PIL import Image, ImageTk
import requests
from datetime import datetime
import pytz

def icons():
    global snow_icon, clear_icon, foggy_icon, thunder_icon, drizzle_icon, rain_icon, cloudy_icon
    snow = Image.open("snow.png")
    snow_resized = snow.resize((130,130), Image.LANCZOS)
    snow_icon = ImageTk.PhotoImage(snow_resized)
    
    clear = Image.open("clear-sky.png")
    clear_resized = clear.resize((130,130), Image.LANCZOS)
    clear_icon = ImageTk.PhotoImage(clear_resized)
    
    foggy = Image.open("foggy.png")
    foggy_resized = foggy.resize((130,130), Image.LANCZOS)
    foggy_icon = ImageTk.PhotoImage(foggy_resized)

    thunderstorm = Image.open("thunderstorm.png")
    thunderstorm_resized = thunderstorm.resize((130,130), Image.LANCZOS)
    thunder_icon = ImageTk.PhotoImage(thunderstorm_resized)
    
    drizzle = Image.open("drizzle.png")
    drizzle_resized = drizzle.resize((130,130), Image.LANCZOS)
    drizzle_icon = ImageTk.PhotoImage(drizzle_resized)
    
    rain = Image.open("rain.png")
    rain_resized = rain.resize((130,130), Image.LANCZOS)
    rain_icon = ImageTk.PhotoImage(rain_resized)
    
    cloudy = Image.open("cloudyicon.png")
    cloudy_resized = cloudy.resize((130,130), Image.LANCZOS)
    cloudy_icon = ImageTk.PhotoImage(cloudy_resized)
    
def get_weather():
    global weather, temp, windspeed, user_input, weather_icon, weather_win
    
    api_key = "dd983f4b06532bc0823252920cd8d1ec"
    
    user_input = city_entry.get().strip().title()

    response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&appid={api_key}"
        )
    data = response.json()
    
    weather = data["weather"][0]["main"]
    temp = round(data["main"]["temp"])
    windspeed = data["wind"]["speed"]
    
    
    weather_window()
    update_weather_icon()
    
def weather_window():
    global weather_icon, weather_win
    
    weather_win = Toplevel()
    weather_win.geometry("390x600")
    weather_win.resizable(False, False)
    weather_win.title("Weather")
    
    weather_win.config(background="#101010")
    
    city_header = Label(weather_win,
                        text=user_input,
                        font=(main_font),
                        fg="White",
                        bg="#101010")
    city_header.pack(pady=70)
    
    wind_desc = Label(weather_win,
                      text=f"Wind speed: {windspeed}mph",
                      font=(secondary_font, 12),
                      fg="Grey",
                      bg="#101010")
    wind_desc.place(x=117, y=140)
    
    weather_icon = Label(weather_win,
                         image=cloudy_icon,
                         bg="#101010")
    weather_icon.place(x=120, y=185)
    
    weather_desc = Label(weather_win,
                         text=weather,
                         font=(main_font, 15),
                         fg="Grey",
                         bg="#101010")
    weather_desc.place(x=150, y=335)
    degrees = Label(weather_win,
                    text=f"{temp}\u00B0",
                    font=(main_font),
                    fg="White",
                    bg="#101010")
    degrees.place(x=148, y=390)

   
    
def update_weather_icon():
    global weather_icon

    if weather == "Clear":
        weather_icon.config(image=clear_icon)
    elif weather == "Clouds":
        weather_icon.config(image=cloudy_icon)
    elif weather == "Rain":
        weather_icon.config(image=rain_icon)  
    elif weather == "Snow":
        weather_icon.config(image=snow_icon)
    elif weather == "Thunderstorm":
        weather_icon.config(image=thunder_icon)
    elif weather == "Drizzle":
        weather_icon.config(image=drizzle_icon)
    elif weather == "Atmosphere":
        weather_icon.config(image=foggy_icon)

def menu():
    global main_font, secondary_font, city_entry

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
                        command=get_weather)
    submitcity.place(x=150,y=360)
    
    icons()
    menu_window.mainloop()
    

menu()