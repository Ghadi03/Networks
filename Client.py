import tkinter as tk
import requests
from tkinter import messagebox

def format_weather_data(weather_data):
    temp = weather_data['main']['temp'] -273.15
    print(temp)
    weather = weather_data['weather'][0]['description']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']

    formatted_data = (
        f"Temperature: {temp:.2f}°C\n"
        f"Weather: {weather}\n"
        f"Humidity: {humidity}%\n"
        f"Wind Speed: {wind_speed} m/s\n"
    )
    return formatted_data


def fetch_weather():
    city = city_entry.get()
    if city:
        try:
            response = requests.get(f'http://localhost:5000/weather/{city}')
            weather = response.json()
            formatted_weather = format_weather_data(weather)
            result_label.config(text=formatted_weather)
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", e)
    else:
        messagebox.showinfo("Info", "Please enter a city name")


def clear_data():
    city_entry.delete(0, tk.END)  
    result_label.config(text="") 

app = tk.Tk()
app.title("Weather App")

city_entry = tk.Entry(app)
city_entry.pack()

fetch_button = tk.Button(app, text="Get Weather", command=fetch_weather)
fetch_button.pack()

result_label = tk.Label(app, text="")
result_label.pack()

clear_button = tk.Button(app, text="Clear", command=clear_data)
clear_button.pack()

app.mainloop()



