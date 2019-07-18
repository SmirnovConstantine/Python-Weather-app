import tkinter as tk
import requests

from PIL import Image, ImageTk

HEIGHT = 500
WIDTH = 600

def test(entry):
    print('Hello world!', entry)

#api.openweathermap.org/data/2.5/forecast?id={city ID}
#051dcf70d8e759971e0ee42d66275a59

def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = round((weather['main']['temp'] - 32)*5/9,1)
        final_str = 'City: %s \nConditions: %s \nTemperature(C) %s'  % (name, desc ,temp)
    except:
        final_str = 'There was a problem retrievung that information'

    return final_str

def get_weather(city):
    weather_key = '051dcf70d8e759971e0ee42d66275a59'
    url = 'https://api.openweathermap.org/data/2.5/weather/'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather)

    icon_name = weather['weather'][0]['icon']
    open_image(icon_name)

def open_image(icon):
    size = int(lower_frame.winfo_height()*0.2)
    img = ImageTk.PhotoImage(Image.open('./img/'+icon+'.png').resize((size, size)))
    weather_icon.delete("all")
    weather_icon.create_image(0,0, anchor='nw', image=img)
    weather_icon.image = img


root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)

background_image = tk.PhotoImage(file='5.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

canvas.pack()

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=('Courier', 10))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get weather", font=('Courier', 12), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 10), anchor='nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)

weather_icon = tk.Canvas(label, bd=0, highlightthickness=0)
weather_icon.place(relx=.75, rely=0, relwidth=1, relheight=0.5)

#icon = tk.PhotoImage(file='img/01d.png')
#icon.place(relwidth=1, relheight=1)

root.mainloop()