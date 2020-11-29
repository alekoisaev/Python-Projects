from tkinter import *
import requests


def resp(weather):
    try:
        name = weather['name']
        description = weather['weather'][0]['description']
        temperature = weather['main']['temp']
        final_str = 'ქალაქი:', name, '\n', 'აღწერა:', description, '\n', 'ტემპერატურა: ', temperature
    except:
        final_str = 'Connection failed'

    return final_str


def get_weather(city):
    weather_key = "dc3f3e1b9c3b5c0dff8651e702eda735"
    url = 'https://api.openweathermap.org/data/2.5/weather'
    parameters = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, parameters)
    weather = response.json()
    resp(weather)

    label['text'] = resp(weather)


root = Tk()

canvas = Canvas(root, height=300, width=350)
canvas.pack()

frame = Frame(root)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = Entry(frame, font=20)
entry.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = Button(frame, text="Check weather", command=lambda: get_weather(entry.get()))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = Frame(root)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = Label(lower_frame, font=32)
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()
