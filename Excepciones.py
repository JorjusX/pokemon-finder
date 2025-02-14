import tkinter as tk
import random
import pandas as pd
import requests
import time
import threading
from Detalles import Detalles

class Excepciones:
    def __init__(self):
        self.contents.set("")

    def sin_sprite(self, pokemon, variantes):
        variantes = [variante for variante in variantes if "-starter" not in variante['pokemon']['name'] and "-totem" not in variante['pokemon']['name']]
        # Elimina los dominantes y los iniciales de let's go
        result = requests.get("https://pokeapi.co/api/v2/pokemon-species/"+str(pokemon))

        if "miraidon" in pokemon:
            self.insert("Solo existe sprite estatico para la forma de defensa de Miraidon\n")
            variantes = []
        elif "koraidon" in pokemon:
            self.insert("Solo existe sprite estatico para la forma de combate de Koraidon\n")
            variantes = []
        elif "frillish" in pokemon:
            variantes = []
        elif "jellicent" in pokemon:
            variantes = []
        elif "zygarde" in pokemon:
            variantes = [variante for variante in variantes if "zygarde" not in variante['pokemon']['name']]
        elif "mimikyu" in pokemon:
            if pokemon == "mimikyu-busted":
                variantes[1]['pokemon']['name'] = variantes[0]['pokemon']['name']
        elif "cramorant" in pokemon:
            variantes = [variante for variante in variantes if "cramorant" not in variante['pokemon']['name']]
            self.insert("Solo existe sprite para la forma normal de Cramorant\n")

        elif result.text == "Not Found":
            pokemon = pokemon.replace("-", " ").split()[0]
            result = requests.get("https://pokeapi.co/api/v2/pokemon-species/"+str(pokemon))
            for i in range(len(variantes)):
                if variantes[i]['pokemon']['name'] == self.contents.get():
                    variantes[i]['pokemon']['name'] = variantes[0]['pokemon']['name']
        return variantes

    def excepciones(self, pokemon):
        if pokemon == "nidoran":
            self.insert("Elije nidoran-m, nidoran-f o nidoran-random\n")
        elif pokemon == "farfetch'd":
            pokemon = "farfetchd"
        elif pokemon == "farfetch'd-galar":
            pokemon = "farfetchd-galar"
        elif pokemon == "sirfetch'd":
            pokemon = "sirfetchd"    
        elif pokemon == "mr. mime":
            pokemon = "mr-mime"
        elif pokemon == "mr. mime-galar":
            pokemon = "mr-mime-galar"
        elif pokemon == "mr. rime":
            pokemon = "mr-rime"
        elif pokemon == "mime jr.":
            pokemon = "mime-jr"
        elif pokemon == "wormadam":
            self.insert("Elije wormadam-plant, wormadam-sandy, wormadam-trash o wormadam-random\n")
        elif pokemon == "giratina":
            self.insert("Elije giratina-altered, giratina-origin o random\n")
        elif pokemon == "deoxys":
            self.insert("Elije deoxys-normal, deoxys-attack, deoxys-defense, deoxys-speed o random\n")
        elif pokemon == "shaymin":
            self.insert("Elije shaymin-land, shaymin-sky o random\n")
        elif pokemon == "basculin":
            self.insert("Elije basculin-red-striped, basculin-blue-striped, basculin-white-striped o random\n")
        elif pokemon == "darmanitan":
            self.insert("Elije darmanitan-standard, darmanitan-zen o random\n")
        elif pokemon == "darmanitan-galar":
            self.insert("Elije darmanitan-standard-galar, darmanitan-zen-galar o random\n")
        elif pokemon == "landorus":
            self.insert("Elije landorus-incarnate, landorus-therian o random\n")
        elif pokemon == "tornadus":
            self.insert("Elije tornadus-incarnate, tornadus-therian o random\n")
        elif pokemon == "thundurus":
            self.insert("Elije thundurus-incarnate, thundurus-therian o random\n")
        elif pokemon == "enamorus":
            self.insert("Elije enamorus-incarnate, enamorus-therian o random\n")
        elif pokemon == "keldeo":
            self.insert("Elije keldeo-ordinary, keldeo-resolute o random\n")
        elif pokemon == "meloetta":
            self.insert("Elije meloetta-aria, meloetta-pirouette o random\n")
        elif pokemon == "flabébé":
            pokemon = "flabebe"
        elif pokemon == "meowstic":
            self.insert("Elije meowstic-male, meowstic-female o random\n")
        elif pokemon == "indeedee":
            self.insert("Elije indeedee-male, indeedee-female o random\n")
        elif pokemon == "basculegion":
            self.insert("Elije basculegion-male, basculegion-female o random\n")
        elif pokemon == "oinkologne":
            self.insert("Elije oinkologne-male, oinkologne-female o random\n")
        elif pokemon == "aegislash":
            self.insert("Elije aegislash-blade, aegislash-shield o random\n")
        elif pokemon == "pumpkaboo":
            self.insert("Elije pumpkaboo-average, pumpkaboo-small, pumpkaboo-large, pumpkaboo-super o random\n")
        elif pokemon == "gourgeist":
            self.insert("Elije gourgeist-average, gourgeist-small, gourgeist-large, gourgeist-super o random\n")
        elif pokemon == "zygarde":
            self.insert("Elije zygarde-50, zygarde-10-power-construct, zygarde-50-power-construct, zygarde-complete o random\n")
        elif pokemon == "oricorio":
            self.insert("Elije oricorio-baile, oricorio-pom-pom, oricorio-pau, oricorio-sensu o random\n")
        elif pokemon == "lycanroc":
            pokemon = Detalles.lycanroc(self, pokemon)
        elif pokemon == "wishiwashi":
            self.insert("Elije wishiwashi-solo, wishiwashi-school o random\n")
        elif pokemon == "codigo-cero":
            pokemon = "type-null"
            self.insert("El nombre de este pokemon es type-null\n")
        elif pokemon == "minior":
            self.insert("Elije minior-red-meteor, minior-orange-meteor, minior-yellow-meteor, minior-green-meteor, minior-blue-meteor, minior-indigo-meteor, minior-violet-meteor, minior-red, minior-orange, minior-yellow, minior-green, minior-blue, minior-indigo, minior-violet o random(meteor, core o ambos)\n")
        elif pokemon == "mimikyu":
            pokemon = "mimikyu-disguised"
        elif pokemon == "toxtricity":
            self.insert("Elije toxtricity-amped, toxtricity-low-key o random\n")
        elif pokemon == "eiscue":
            pokemon = "eiscue-ice"
        elif pokemon == "morpeko":
            pokemon = "morpeko-full-belly"
        elif pokemon == "urshifu":
            self.insert("Elije urshifu-rapid-strike, urshifu-single-strike o random\n")
        elif pokemon == "maushold":
            n = random.randint(1, 100)
            if n == 1:
                pokemon = "maushold-family-of-three"
            else: pokemon = "maushold-family-of-four"
        elif pokemon == "squawkabilly":
            self.insert("Las cuatro formas de Squawkabilly son squawkabilly-green-plumage, squawkabilly-blue-plumage, squawkabilly-yellow-plumage y squawkabilly-white-plumage\n")
        elif pokemon == "palafin":
            pokemon = Detalles.palafin(self, pokemon)
        elif pokemon == "tatsugiri":
            self.insert("Las tres formas son tatsugiri-curly, tatsugiri-droopy, tatsugiri-stretchy\n")
        elif pokemon == "dudunsparce":
            n = random.randint(1, 100)
            if n == 1:
                pokemon = "dudunsparce-three-segment"
            else: pokemon = "dudunsparce-two-segment"
            
        else:
            self.no_existe = True
        self.contents.set(pokemon)
        return pokemon

    def variaciones(self, pokemon):
        # Randoms
        if pokemon == "nidoran-random":
            pokemon = random.choice(["nidoran-f", "nidoran-m"])
        elif pokemon == "pikachu-random":
            pokemon = random.choice(["pikachu", "pikachu-cosplay", "pikachu-rock-star", "pikachu-belle", "pikachu-pop-star", "pikachu-phd", "pikachu-libre", "pikachu-original-cap", "pikachu-hoenn-cap", "pikachu-sinnoh-cap", "pikachu-unova-cap", "pikachu-kalos-cap", "pikachu-alola-cap", "pikachu-partner-cap", "pikachu-world-cap"])
        elif pokemon == "tauros-random":
            pokemon = random.choice(["tauros-paldea-combat-breed", "tauros-paldea-blaze-breed", "tauros-paldea-aqua-breed", "tauros"])
        elif pokemon == "castform-random":
            pokemon = random.choice(["castform", "castform-sunny", "castform-rainy", "castform-snowy"])
        elif pokemon == "deoxys-random":
            pokemon = random.choice(["deoxys-normal", "deoxys-attack", "deoxys-defense", "deoxys-speed"])
        elif pokemon == "wormadam-random":
            pokemon = random.choice(["wormadam-plant", "wormadam-sandy", "wormadam-trash"])
        elif pokemon == "rotom-random":
            pokemon = random.choice(["rotom", "rotom-heat", "rotom-wash", "rotom-frost", "rotom-fan", "rotom-mow"])
        elif pokemon == "dialga-random":
            pokemon = random.choice(["dialga", "dialga-origin"])
        elif pokemon == "palkia-random":
            pokemon = random.choice(["palkia", "palkia-origin"])
        elif pokemon == "giratina-random":
            pokemon = random.choice(["giratina-altered", "giratina-origin"])
        elif pokemon == "shaymin-random":
            pokemon = random.choice(["shaymin-land", "shaymin-sky"])
        elif pokemon == "basculin-random":
            pokemon = random.choice(["basculin-red-striped", "basculin-blue-striped", "basculin-white-striped"])
        elif pokemon == "darmanitan-random":
            pokemon = random.choice(["darmanitan-standard", "darmanitan-zen"])
        elif pokemon == "darmanitan-galar-random":
            pokemon = random.choice(["darmanitan-galar-standard", "darmanitan-galar-zen"])
        elif pokemon == "tornadus-random":
            pokemon = random.choice(["tornadus-incarnate", "tornadus-therian"])
        elif pokemon == "thundurus-random":
            pokemon = random.choice(["thundurus-incarnate", "thundurus-therian"])
        elif pokemon == "landorus-random":
            pokemon = random.choice(["landorus-incarnate", "landorus-therian"])
        elif pokemon == "enamorus-random":
            pokemon = random.choice(["enamorus-incarnate", "enamorus-therian"])
        elif pokemon == "kyurem-random":
            pokemon = random.choice(["kyurem", "kyurem-black", "kyurem-white"])
        elif pokemon == "keldeo-random":
            pokemon = random.choice(["keldeo-ordinary", "keldeo-resolute"])
        elif pokemon == "meloetta-random":
            pokemon = random.choice(["meloetta-aria", "meloetta-pirouette"])
        elif pokemon == "meowstic-random":
            pokemon = random.choice(["meowstic-male", "meowstic-female"])
        elif pokemon == "indeedee-random":
            pokemon = random.choice(["indeedee-male", "indeedee-female"])
        elif pokemon == "basculegion-random":
            pokemon = random.choice(["basculegion-male", "basculegion-female"])
        elif pokemon == "oinkologne-random":
            pokemon = random.choice(["oinkologne-male", "oinkologne-female"])
        elif pokemon == "aegislash-random":
            pokemon = random.choice(["aegislash-blade", "aegislash-shield"])
        elif pokemon == "pumpkaboo-random":
            pokemon = random.choice(["pumpkaboo-average", "pumpkaboo-small", "pumpkaboo-large", "pumpkaboo-super"])
        elif pokemon == "gourgeist-random":
            pokemon = random.choice(["gourgeist-average", "gourgeist-small", "gourgeist-large", "gourgeist-super"])
        elif pokemon == "zygarde-random":
            pokemon = random.choice(["zygarde-50", "zygarde-10-power-construct", "zygarde-50-power-construct", "zygarde-complete"])
        elif pokemon == "hoopa-random":
            pokemon = random.choice(["hoopa", "hoopa-unbound"])
        elif pokemon == "oricorio-random":
            pokemon = random.choice(["oricorio-baile", "oricorio-pom-pom", "oricorio-pau", "oricorio-sensu"])
        elif pokemon == "lycanroc-random":
            pokemon = random.choice(["lycanroc-midday", "lycanroc-midnight", "lycanroc-dusk"])
        elif pokemon == "wishiwashi-random":
            pokemon = random.choice(["wishiwashi-solo", "wishiwashi-school"])
        elif pokemon == "minior-random":
            pokemon = random.choice(["minior-red-meteor", "minior-orange-meteor", "minior-yellow-meteor", "minior-green-meteor", "minior-blue-meteor", "minior-indigo-meteor", "minior-violet-meteor", "minior-red", "minior-orange", "minior-yellow", "minior-green", "minior-blue", "minior-indigo", "minior-violet"])
        elif pokemon == "minior-meteor-random":
            pokemon = random.choice(["minior-red-meteor", "minior-orange-meteor", "minior-yellow-meteor", "minior-green-meteor", "minior-blue-meteor", "minior-indigo-meteor", "minior-violet-meteor"])
        elif pokemon == "minior-core-random":
            pokemon = random.choice(["minior-red", "minior-orange", "minior-yellow", "minior-green", "minior-blue", "minior-indigo", "minior-violet"])
        elif pokemon == "mimikyu-random":
            pokemon = random.choice(["mimikyu-disguised", "mimikyu-busted"])
        elif pokemon == "necrozma-random":
            pokemon = random.choice(["necrozma", "necrozma-dusk", "necrozma-dawn", "necrozma-ultra"])
        elif pokemon == "magearna-random":
            pokemon = random.choice(["magearna", "magearna-original"])
        elif pokemon == "toxtricity-random":
            pokemon = random.choice(["toxtricity-amped", "toxtricity-low-key"])
        elif pokemon == "eiscue-random":
            pokemon = random.choice(["eiscue-ice", "eiscue-noice"])
        elif pokemon == "morpeko-random":
            pokemon = random.choice(["morpeko-full-belly", "morpeko-hangry"])
        elif pokemon == "zacian-random":
            pokemon = random.choice(["zacian", "zacian-crowned"])
        elif pokemon == "zamazenta-random":
            pokemon = random.choice(["zamazenta", "zamazenta-crowned"])
        elif pokemon == "urshifu-random":
            pokemon = random.choice(["urshifu-rapid-strike", "urshifu-single-strike"])
        elif pokemon == "zarude-random":
            pokemon = random.choice(["zarude", "zarude-dada"])
        elif pokemon == "calyrex-random":
            pokemon = random.choice(["calyrex", "calyrex-ice", "calyrex-shadow"])
        elif pokemon == "calyrex-jinete-random":
            pokemon = random.choice(["calyrex-ice", "calyrex-shadow"])
        elif pokemon == "squawkabilly-random":
            pokemon = random.choice(["squawkabilly-green-plumage", "squawkabilly-blue-plumage", "squawkabilly-yellow-plumage", "squawkabilly-white-plumage"])
        elif pokemon == "palafin-random":
            pokemon == random.choice(["palafin-zero", "palafin-hero"])
        elif pokemon == "tatsugiri-random":
            pokemon = random.choice(["tatsugiri-curly", "tatsugiri-droopy", "tatsugiri-stretchy"])
        elif pokemon == "ogerpon-random":
            pokemon = random.choice(["ogerpon", "ogerpon-wellspring-mask", "ogerpon-hearthflame-mask", "ogerpon-cornerstone-mask"])

        # Variantes sin sprite
        elif pokemon == "pikachu-world-cap":
            self.insert("El sprite Pikachu-world-cap no puede cargarse, lo siento :-(\n")
            pokemon="pikachu"
        elif "koraidon" in pokemon:
            pokemon = "koraidon"
        elif "miraidon" in pokemon:
            pokemon = "miraidon"
        elif "-starter" in pokemon:
            self.insert("No existe sprite estatico para Eevee o Pikachu de let's go\n")
            pokemon = pokemon.replace("-starter", "")
        elif "-totem" in pokemon:
            self.insert("No existe sprite estatico para los pokemons dominantes\n")
            pokemon = pokemon.replace("-totem", "")
        elif pokemon == "frillish-female":
            self.insert("El sexo de este pokemon es aleatorio\n")
            pokemon = "frillish"
        elif pokemon == "jellicent-female":
            self.insert("El sexo de este pokemon es aleatorio\n")
            pokemon = "jellicent"
        elif pokemon == "zygarde-10":
            pokemon = "zygarde-10-power-construct"
        elif pokemon == "zygarde":
            pokemon = "zygarde-50"
        elif "cramorant" in pokemon:
            pokemon = "cramorant"

        Detalles.main(self, pokemon)
        self.contents.set(pokemon)
        return pokemon