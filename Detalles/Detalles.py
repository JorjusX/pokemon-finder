import time
import tkinter as tk
import threading
import random
import requests
from PIL import Image, ImageTk

def main(self, pokemon):
    if pokemon == "morpeko-full-belly":
        hilo = threading.Thread(target=morpeko, args=(self, pokemon))
        hilo.start()
    elif pokemon == "lycanroc":
        pokemon = lycanroc(self, pokemon)
    elif "-meteor" in pokemon:
        minior(self, pokemon)        
    return pokemon

def morpeko(self, pokemon):
    try:
        valor = str(self.image)
        while valor == str(self.image):
            time.sleep(10)
            #Si el tiempo pasa y no ha cambiado el texto no se hara el cambio
            pokemon = self.contents.get().split(" ", 1)[0].lower()
            if pokemon == "morpeko-full-belly":
                pokemon = "morpeko-hangry"
                print("Morpeko tiene hambre")
                result = requests.get("https://pokeapi.co/api/v2/pokemon/morpeko-hangry")
                img = result.json()["sprites"]["front_default"]
                img_shiny = result.json()["sprites"]["front_shiny"]
                if self.shiny:
                    img_data = requests.get(img_shiny).content
                    file_path = f"sprites/{pokemon} shiny.png"
                else:
                    img_data = requests.get(img).content
                    file_path = f"sprites/{pokemon}.png"
                with open(file_path, 'wb') as handler:
                    handler.write(img_data)
                self.image = tk.PhotoImage(file=file_path)
                self.image_label.config(image=self.image)
                self.insert("A Morpeko le entro hambre de tanto esperar\n")
                self.contents.set("morpeko-hangry")
            else:
                break
    except Exception as e:
        print("Error:", e)

def lycanroc(self, pokemon):
    if time.localtime().tm_hour in range(8, 18):
        self.insert("De dia Lycanroc adquiere la forma diurna\n")
        pokemon = "lycanroc-midday"
    elif time.localtime().tm_hour in range(20, 6) or time.localtime().tm_hour == 0:
        self.insert("De noche Lycanroc adquiere la forma nocturna\n")
        pokemon = "lycanroc-midnight"
    else:
        self.insert("En el atardecer Lycanroc adquiere la forma crepuscular\n")
        pokemon = "lycanroc-dusk"
    self.contents.set(pokemon)
    return pokemon

def minior(self, pokemon):
    color = pokemon.split("-")[1]
    result = requests.get(f"https://pokeapi.co/api/v2/pokemon/minior-{color}")
    if self.shiny:
        img = result.json()["sprites"]["front_shiny"]
        file_path = f"sprites/minior-{color} shiny.png"
    else:
        img = result.json()["sprites"]["front_default"]
        file_path = f"sprites/minior-{color}.png"
    img_data = requests.get(img).content
    with open(file_path, 'wb') as handler:
        handler.write(img_data)
    self.image = tk.PhotoImage(file=file_path)
    self.image_label.config(image=self.image)
    self.contents.set(f"minior-{color}")
    pokemon = self.contents.get()
    self.insert(f"Has roto la coraza del minior\n")
    self.insert(f"Ahora es {pokemon}\n")

def palafin(self, pokemon):
    if self.contador == 0:
        pokemon = "palafin-zero"
        if self.shiny:
            self.contador = 2
        else:
            self.contador = 1
    elif self.contador == 1:
        pokemon = "palafin-hero"
        self.insert("Palafin se ha transformado en su forma heroica al entrar otra vez\n")
        self.contador = 0
    elif self.contador == 2:
        self.shiny = True
        pokemon = "palafin-hero"
        self.insert("El Palafin shiny de antes volvio en su forma heroica\n")
        self.contador = 0
    print("Contador:", self.contador)
    self.contents.set(pokemon)
    return pokemon