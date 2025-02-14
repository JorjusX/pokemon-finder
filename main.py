import tkinter as tk
import requests
import random
import matplotlib.pyplot as plt
import numpy as np
import os
from PIL import Image, ImageTk
from Excepciones import Excepciones
from PokeAleatorio import PokeAleatorio
from Detalles import Detalles
import pandas as pd
import time
size=(100,100)
class Main(tk.Frame):
    def __init__(self, master):
        self.bg = self.establecer_color("pikachu")
        super().__init__(master, bg=self.bg)
        self.pack()
        
        self.entrythingy = tk.Entry()
        self.entrythingy.pack()
        self.entrythingy.config(width=50, font=("Parisienne", 12))
        #holA
        self.image_label = tk.Label(self)
        self.image_label.pack()
        self.image_label.config(width=100, height=100)
        self.image_label.bind("<Button-1>", self.on_image_click)
        self.image_label.config(bg=self.bg)
        if not os.path.exists('sprites'):
            self.create_file()
            
        self.image = tk.PhotoImage(file="sprites/pikachu.png")
        self.image_label.config(image=self.image)
        
        self.text_box = tk.Text(self, height=10, width=50)
        self.text_box.pack()
        self.text_box.insert(tk.END, "Aquí aparecerán los resultados de la búsqueda.\n")
        self.text_box.config(state=tk.DISABLED, font=("Parisienne", 12))
        
        self.contents = tk.StringVar()
        self.contents.set("escribe aqui")
        self.entrythingy["textvariable"] = self.contents
        self.entrythingy.bind('<Key-Return>', self.contenido)
        self.entrythingy.pack(pady=10)
        
        self.contador = 0

    def contenido(self, event):
        self.bg = self.establecer_color("pikachu")
        self.shiny = False
        self.error = False
        self.no_existe = False
        print("\nEstas buscando el pokemon:", self.contents.get())
        if self.contents.get() == "exit":
            print("Saliendo de la aplicación")
            self.quit()
        try:
            pokemon = self.contents.get().split(" ",1)[0].lower()
            self.buscarPokemon(pokemon)
        except Exception as e:
            if "Expecting value: line 1 column 1 (char 0)" in str(e) and self.no_existe == True:
                self.delete_text()
                self.insert(f"Error: Has escrito un pokemon mal o inexistente\nEscribiste: {pokemon}\n")
            else:
                print("Error:", e)
        
    def buscarPokemon(self, pokemon):
        result = requests.get("https://pokeapi.co/api/v2/pokemon/"+pokemon)
        if pokemon is int:
            pokemon = result.json()['name']
        respuesta=self.contents.get().lower().replace("-", " ").split()[0]
        if respuesta == "random":
            pokemon = PokeAleatorio.pokeAleatorio(self, pokemon)
            self.entregarPokemon(pokemon)
        elif respuesta == "shiny":
            pokemon = self.contents.get().lower().replace("shiny-", "")
            self.shiny = True
            pokemon = Excepciones.excepciones(self, pokemon)
            self.entregarPokemon(pokemon)
        elif result.text == "Not Found":
            pokemon = Excepciones.excepciones(self, pokemon)
            print("El pokemon es:", pokemon)
            self.contents.set(pokemon)
            self.entregarPokemon(pokemon)
        else: self.entregarPokemon(pokemon)
        
    def entregarPokemon(self, pokemon):
        pokemon = Excepciones.variaciones(self, pokemon)
        #if self.image_label.cget("image") == str(self.image):
        print(f"Buscando pokemon {pokemon}")
        
        result = requests.get("https://pokeapi.co/api/v2/pokemon/"+str(pokemon))
        #image_url = result.json()['sprites']['front_default']
        image_url = self.establecer_genero(pokemon)
        image_url = self.calcular_shiny(pokemon, image_url=image_url)
        print(f"Se encontro el pokemon {pokemon}")
        img_data = requests.get(image_url).content
        if self.shiny:
            file_path = f"sprites/{pokemon} shiny.png"
        else:
            file_path = f"sprites/{pokemon}.png"
        with open(file_path, 'wb') as handler:
            handler.write(img_data)
        try:
            imagen = plt.imread(file_path)
            plt.imshow(imagen)
            self.image = tk.PhotoImage(file=file_path)
            self.image_label.config(image=self.image)   
            plt.show()
            self.text_box.config(state=tk.NORMAL)
            self.text_box.delete(1.0, tk.END)
            self.text_box.insert(tk.END, f"Se encontro el pokemon {pokemon}\n")
            self.text_box.insert(tk.END, f"Nombre: {result.json()['name']}\n")
            self.text_box.config(state=tk.DISABLED)
        except Exception as e:
            if "broken PNG file (bad header checksum in b'iCCP')" in str(e):
                self.error = True
                self.delete_text()
                self.insert(f"Error: El sprite {pokemon} pudo cargar, lo siento :-(\n")
                self.insert("Prueba con otro sprite\n")
                self.entregarPokemon(pokemon)
            else:
                print(f"Error al cargar la imagen: {e}")
        if self.error == False:
            self.establecer_color(pokemon)
            self.update_bg_color()
            print("Cambio el fondo")
            self.mostrar_variantes(pokemon)
    
    def mostrar_variantes(self, pokemon):
        result = requests.get("https://pokeapi.co/api/v2/pokemon-species/"+str(pokemon))
        if result.text == "Not Found":
            pokemon_request = pokemon.replace("-"," ").split()[0]
            #Hay algunos pokemons que son formas y me saltaba error ya que no pueden ser buscadas en "pokemon-species" (ej: mimikyu-disguised y mimikyu-busted)
            # pero todos los que llevan guion no tienen porque ser variantes (ej: mr-mime) asi que busco solo el nombre de la especie
            #No tendria que hacerlo de normal al buscar una forma especial pero tengo algunos que aunque busques una forma deberian salir las otras (ej: zygarde)
            result = requests.get("https://pokeapi.co/api/v2/pokemon-species/"+str(pokemon_request))#Debo hacer de nuevo la peticion con ahora el nombre de la especie y guardo el anterior porque debo mandarlo
        variantes = result.json()['varieties']
        print("Buscando variantes")
        lista = []
        variantes = Excepciones.sin_sprite(self, pokemon, variantes)
        for i in range(1, len(variantes)):
            lista.append(variantes[i]['pokemon']['name'])
        if len(variantes) == 2:
            self.insert(f"El pokemon {pokemon} tiene la variante {lista}\n")
        elif len(variantes) > 2:
            self.insert(f"El pokemon {pokemon} tiene las variantes {lista}\n")
        return variantes
    
    def establecer_color(self, pokemon):
        result = requests.get("https://pokeapi.co/api/v2/pokemon-species/"+str(pokemon))
        self.bg = result.json()['color']['name']
        return self.bg
    
    def establecer_genero(self, pokemon):
        print("Estableciendo genero")
        result = requests.get("https://pokeapi.co/api/v2/pokemon/"+str(pokemon))         
        rates_csv = pd.read_csv("pruebas/pokemon_app/Listas/d_rates.csv")
        id_poke = result.json()['id']
        name = result.json()['name']
        rate = rates_csv['gender_rate']
        if id_poke >= len(rate):
            print("especial")
            name2=name.replace("-"," ")
            name2=name2.split()[0]
            name=name.replace("-","")
            name=name.split()[0]
            id_poke = rates_csv[rates_csv['name'].str.contains(name2)].index[0]
            #Hay algunos que no estan en la lista porque son una forma especial y el id que utilizan es distinto, los asocio con la forma original
            #Luego esta el problema de que la forma de la lista por si es una forma especial (ej: mimikyu, aegislash) asi que hay que hacer esto
        gr = rate[id_poke]
        image_url = result.json()['sprites']['front_default']
        image_url_female = result.json()['sprites']['front_female']
        if gr != "Sin genero":
            gr = float(gr)
            n = random.randint(0,100)
            if n <= gr:
                print("Macho")
                return image_url
            else:
                if image_url_female == None: #Esto es porque los pokemon que siempre son hembra la imagen por defecto es 'font_default' y 'front_female' es None (ej: nidoqueen)
                    print("Hembra pero default")
                    return image_url
                print("Hembra")
                return image_url_female
            #Existen pokemons cuyo genero es en si una forma distinta (ej: Meowstic, Indeedee) que tienen distintas estadisticas, luego esta el caso de Nidoran que en realidad son distintos pokemons
        else:
            print("Desgenerao")
            return image_url

    def calcular_shiny(self, pokemon, image_url):
        print("Calculando shiny")
        result = requests.get("https://pokeapi.co/api/v2/pokemon/"+str(pokemon))
        shiny_url = result.json()['sprites']['front_shiny']
        shiny_url_female = result.json()['sprites']['front_shiny_female']
        shiny_inexistentes=["eternatus-eternamax", "10190", "pikachu-world-cap", "10160", "flapple-gmax", "10216", "appletun-gmax", "10217"]
        if pokemon in shiny_inexistentes:
            self.shiny = False
            self.insert(f"El pokemon {pokemon} no tiene forma shiny\n")
            return image_url
        if self.shiny:
            print("¡¡¡¡¡SHINY!!!!!")
            if "female" in image_url:
                return shiny_url_female
            else: return shiny_url
        shiny_n = 8192 #El shiny es 1 entre 8192 como en Pokemon Esmeralda
        cal_shiny = random.randint(1, shiny_n)
        print("Calculated Shiny:", cal_shiny)
        if cal_shiny == shiny_n:
            self.shiny = True
            print("¡¡¡¡¡SHINY!!!!!")
            if "female" in image_url:
                return shiny_url_female
            else: return shiny_url
        else: return image_url
        
    def create_file(self):
        print("Iniciando programa por primera vez")
        print("Creando carpeta sprites")
        os.makedirs('sprites')
        pikachu = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
        pikachu_img = requests.get(pikachu.json()['sprites']['front_default']).content
        with open(f"sprites/pikachu.png", 'wb') as handler:
            handler.write(pikachu_img)
            
    def insert(self, text):
        self.text_box.config(state=tk.NORMAL)
        self.text_box.insert(tk.END, text)
        self.text_box.config(state=tk.DISABLED)
    def delete_text(self):
        self.text_box.config(state=tk.NORMAL)
        self.text_box.delete(1.0, tk.END)
        self.text_box.config(state=tk.DISABLED)
        
    def on_image_click(self, event):
        Detalles.main(self, self.contents.get())
        
    def update_bg_color(self):
        self.config(bg=self.bg)
        self.image_label.config(bg=self.bg)
        self.master.config(bg=self.bg)
        
           

root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = int(screen_width * 0.5)
window_height = int(screen_height * 0.5)
root.geometry(f"{window_width}x{window_height}")
root.title("ThePokeFinder")
current_directory = os.path.dirname(os.path.abspath(__file__))
root.iconphoto(False, tk.PhotoImage(file=os.path.join(current_directory, 'images/mudkip.png')))
main_app = Main(root)
root.configure(bg=main_app.bg)
main_app.mainloop()