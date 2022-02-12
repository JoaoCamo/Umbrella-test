from email import message
from tkinter import *
from tkinter import messagebox
from tkinter import font
import requests

api = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=598068f18515daf478c319d1e0c59cac'

#Função para consultar a API com base na cidade que o usuário digitar
def getWeather(city):
    result = requests.get(api.format(city))
    if result:
        json = result.json()
        city = json['name']
        country = json['sys']['country']
        temp_kelvin = json['main']['temp']
        temp_celsius = temp_kelvin - 273.15
        humidity = json['main']['humidity']
        pressure = json['main']['pressure']
        weather = json['weather'][0]['main']
        final = (city, country, temp_celsius, humidity, weather, pressure)
        return final
    else:
        return None

#Função para preencher as labels do app
def clima():
    city = city_text.get()
    weather = getWeather(city)
    if weather:
        location_lbl['text'] = '{}, {}'.format(weather[0], weather[1])
        temp_lbl['text'] = 'Temperatura: {:.2f}°C'.format(weather[2])
        humidity_lbl['text'] = 'Umidade do ar: {}%'.format(weather[3])
        pressure_lbl['text'] = 'Pressão atmosferica: {} hPa'.format(weather[5])
        weather_lbl['text'] = 'Condição do tempo: {}'.format(weather[4])
        if weather_lbl['text'] == 'Rain' or weather_lbl['text'] == 'Thunderstorm' or weather_lbl['text'] == 'Drizzle':
            umbrella_lbl['text'] = 'Está chovendo por favor leve um guarda chuva'
        elif weather[3] >= 90 and weather[5] < 1015: #A probabilidade de chuva é feita com base em alta umidade e baixa pressão atmosferica
            umbrella_lbl['text'] = 'Provavelmente irá chover, por favor leve um guarda chuva'
        else:
            umbrella_lbl['text'] = 'Hoje você não precisa levar um guarda chuva'
    else:
        messagebox.showerror('Error', 'Não foi possivel encontrar a cidade: {}'.format(city))

app = Tk()
app.title("Desafio guarda chuva")
app.geometry('450x350')

city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.pack()

search_btn = Button(app, text='Procurar cidade', width=12, command=clima)
search_btn.pack()

location_lbl = Label(app, text='Digite sua cidade', font=('bolt', 12))
location_lbl.pack()

temp_lbl = Label(app, text='', font=('bolt', 12))
temp_lbl.pack()

humidity_lbl = Label(app, text='', font=('bolt', 12))
humidity_lbl.pack()

pressure_lbl = Label(app, text='', font=('bolt', 12))
pressure_lbl.pack()

weather_lbl = Label(app, text='', font=('bolt', 12))
weather_lbl.pack()

a = Label(app, text='-----------------------------------', font=('bolt', 12))
a.pack()

umbrella_lbl = Label(app, text='', font=('bolt', 12))
umbrella_lbl.pack()



app.mainloop()
