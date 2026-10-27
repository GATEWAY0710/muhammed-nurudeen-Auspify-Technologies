import tkinter as tk
from tkinter import messagebox
import requests
import json
from datetime import datetime

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather Information App")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#87CEEB")
        
        # API Key - Using OpenWeatherMap API
        # Get your free API key from: https://openweathermap.org/api
        self.api_key = "YOUR_API_KEY_HERE"
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
        
        # Title
        title_label = tk.Label(
            root,
            text="Weather Information",
            font=("Arial", 20, "bold"),
            bg="#87CEEB",
            fg="#000000"
        )
        title_label.pack(pady=20)
        
        # City search frame
        search_frame = tk.Frame(root, bg="#87CEEB")
        search_frame.pack(pady=10)
        
        self.city_entry = tk.Entry(
            search_frame,
            font=("Arial", 14),
            width=20,
            justify="center"
        )
        self.city_entry.pack(side=tk.LEFT, padx=5)
        self.city_entry.insert(0, "Enter city name")
        self.city_entry.bind("<FocusIn>", self.clear_placeholder)
        self.city_entry.bind("<Return>", lambda event: self.get_weather())
        
        search_btn = tk.Button(
            search_frame,
            text="Search",
            font=("Arial", 12),
            bg="#4CAF50",
            fg="white",
            command=self.get_weather,
            cursor="hand2"
        )
        search_btn.pack(side=tk.LEFT, padx=5)
        
        # Weather info frame
        self.info_frame = tk.Frame(root, bg="#ffffff", relief=tk.RIDGE, bd=2)
        self.info_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        
        # City name
        self.city_label = tk.Label(
            self.info_frame,
            text="",
            font=("Arial", 18, "bold"),
            bg="#ffffff"
        )
        self.city_label.pack(pady=10)
        
        # Temperature
        self.temp_label = tk.Label(
            self.info_frame,
            text="",
            font=("Arial", 48, "bold"),
            bg="#ffffff"
        )
        self.temp_label.pack(pady=10)
        
        # Description
        self.desc_label = tk.Label(
            self.info_frame,
            text="",
            font=("Arial", 14),
            bg="#ffffff"
        )
        self.desc_label.pack(pady=5)
        
        # Details frame
        details_frame = tk.Frame(self.info_frame, bg="#ffffff")
        details_frame.pack(pady=20)
        
        self.humidity_label = tk.Label(
            details_frame,
            text="",
            font=("Arial", 12),
            bg="#ffffff"
        )
        self.humidity_label.grid(row=0, column=0, padx=20)
        
        self.wind_label = tk.Label(
            details_frame,
            text="",
            font=("Arial", 12),
            bg="#ffffff"
        )
        self.wind_label.grid(row=0, column=1, padx=20)
        
        # Note
        note_label = tk.Label(
            root,
            text="Note: Add your API key in the code",
            font=("Arial", 8),
            bg="#87CEEB",
            fg="#666666"
        )
        note_label.pack(side=tk.BOTTOM, pady=5)
    
    def clear_placeholder(self, event):
        if self.city_entry.get() == "Enter city name":
            self.city_entry.delete(0, tk.END)
    
    def get_weather(self):
        city = self.city_entry.get().strip()
        
        if not city or city == "Enter city name":
            messagebox.showwarning("Warning", "Please enter a city name")
            return
        
        if self.api_key == "YOUR_API_KEY_HERE":
            messagebox.showwarning(
                "API Key Required",
                "Please add your OpenWeatherMap API key.\n\nGet it for free at:\nhttps://openweathermap.org/api"
            )
            return
        
        try:
            params = {
                'q': city,
                'appid': self.api_key,
                'units': 'metric'
            }
            response = requests.get(self.base_url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            # Update display
            self.city_label.config(text=f"{data['name']}, {data['sys']['country']}")
            self.temp_label.config(text=f"{round(data['main']['temp'])}°C")
            self.desc_label.config(text=data['weather'][0]['description'].title())
            self.humidity_label.config(text=f"Humidity: {data['main']['humidity']}%")
            self.wind_label.config(text=f"Wind: {data['wind']['speed']} m/s")
            
        except requests.exceptions.HTTPError:
            messagebox.showerror("Error", "City not found. Please check the city name.")
        except requests.exceptions.ConnectionError:
            messagebox.showerror("Error", "Network error. Please check your internet connection.")
        except requests.exceptions.Timeout:
            messagebox.showerror("Error", "Request timed out. Please try again.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
