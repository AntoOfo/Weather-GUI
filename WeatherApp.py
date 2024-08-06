from tkinter import *
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
    
    menu_bg = Image.open("menugradient.png")
    menu_bg_resized = menu_bg.resize((390,600), Image.LANCZOS)
    menu_bg_photo = ImageTk.PhotoImage(menu_bg_resized)
    
    background = Label(menu_window,
                  image=menu_bg_photo)
    background.place(x=0,y=0)
    
    header = Label(menu_window,
                   text="Weatherly",
                   font=("Trebuchet MS",35),
                   fg="White",
                   bg=None)
    header.place(x=80, y=50)
    
    
    menu_window.mainloop()
    

menu()