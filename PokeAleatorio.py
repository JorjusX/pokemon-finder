import tkinter as tk
import random
import pandas as pd
import requests
class PokeAleatorio:
    def __init__(self):
        self.contents.set("")
        
    def pokeAleatorio(self, pokemon):
        if "shiny" in self.contents.get():
            self.shiny = True
            self.contents.set(self.contents.get().replace("shiny-", ""))
        if self.contents.get() == "random":
            pokemon = random.randint(1,1025)
        elif self.contents.get() == "random-gen1":
            pokemon = random.randint(1,151)
        elif self.contents.get() == "random-gen2":
            pokemon = random.randint(152,251)
        elif self.contents.get() == "random-gen3":
            pokemon = random.randint(252,386)
        elif self.contents.get() == "random-gen4":
            pokemon = random.randint(387,493)
        elif self.contents.get() == "random-gen5":
            pokemon = random.randint(494,649)
        elif self.contents.get() == "random-gen6":
            pokemon = random.randint(650,721)
        elif self.contents.get() == "random-gen7":
            pokemon = random.randint(722,809)
        elif self.contents.get() == "random-gen8":
            pokemon = random.randint(810,905)
        elif self.contents.get() == "random-gen9":
            pokemon = random.randint(906,1025)
        elif self.contents.get() == "random-mega":
            megas = ["venusaur-mega", "charizard-mega-x", "charizard-mega-y", "blastoise-mega", "alakazam-mega", "gengar-mega", "kangaskhan-mega", "pinsir-mega", "gyarados-mega", "aerodactyl-mega", "mewtwo-mega-x", "mewtwo-mega-y", "ampharos-mega", "scizor-mega", "heracross-mega", "houndoom-mega", "tyranitar-mega", "blaziken-mega", "gardevoir-mega", "mawile-mega", "aggron-mega", "medicham-mega", "manectric-mega", "banette-mega", "absol-mega", "garchomp-mega", "lucario-mega", "abomasnow-mega", "beedrill-mega", "pidgeot-mega", "slowbro-mega", "steelix-mega", "sceptile-mega", "swampert-mega", "sableye-mega", "sharpedo-mega", "camerupt-mega", "altaria-mega", "glalie-mega", "salamence-mega", "metagross-mega", "latias-mega", "latios-mega", "rayquaza-mega", "lopunny-mega", "gallade-mega", "audino-mega", "diancie-mega"]
            pokemon = random.choice(megas)
        elif self.contents.get() == "random-alola":                
            formas_alola = ["rattata-alola", "raticate-alola", "raichu-alola", "sandshrew-alola", "sandslash-alola", "vulpix-alola", "ninetales-alola", "diglett-alola", "dugtrio-alola", "meowth-alola", "persian-alola", "geodude-alola", "graveler-alola", "golem-alola", "grimer-alola", "muk-alola", "exeggutor-alola", "marowak-alola"]
            pokemon = random.choice(formas_alola)
        elif self.contents.get() == "random-galar":
            formas_galar = ["meowth-galar", "ponyta-galar", "rapidash-galar", "slowpoke-galar", "slowbro-galar", "farfetchd-galar", "weezing-galar", "mr-mime-galar", "corsola-galar", "zigzagoon-galar", "linoone-galar", "darumaka-galar", "darmanitan-galar", "yamask-galar", "stunfisk-galar"]
            pokemon = random.choice(formas_galar)
        elif self.contents.get() == "random-hisui":
            formas_hisui = ["deiciduieye-hisui", "typhlosion-hisui", "samurott-hisui", "qwilfish-hisui", "lilligant-hisui", "sliggoo-hisui", "goodra-hisui", "growlithe-hisui", "arcanine-hisui", "voltorb-hisui", "electroce-hisui", "avalugg-hisui", "zorua-hisui", "zoroark-hisui", "braviary-hisui"]
        elif self.contents.get() == "random-gmax":
            gigamax = ["charizard-gmax", "butterfree-gmax", "pikachu-gmax", "meowth-gmax", "machamp-gmax", "gengar-gmax", "kingler-gmax", "lapras-gmax", "eevee-gmax", "snorlax-gmax", "garbodor-gmax", "melmetal-gmax", "rillaboom-gmax", "cinderace-gmax", "inteleon-gmax", "corviknight-gmax", "orbeetle-gmax", "drednaw-gmax", "coalossal-gmax", "flapple-gmax", "appletun-gmax", "sandaconda-gmax", "centiskorch-gmax", "hatterene-gmax", "grimmsnarl-gmax", "alcremie-gmax", "copperajah-gmax", "duraludon-gmax", "eternatur-eternamax", "urshifu-rapid-strike-gmax", "urshifu-single-strike-gmax", "toxtricity-low-key-gmax", "toxtricity-amped-gmax", "venusaur-gmax", "blastoise-gmax"]
            pokemon = random.choice(gigamax)
        elif self.contents.get() == "random-legendario":
            legendarios = ["articuno", "articuno-galar", "zapdos", "zapdos-galar", "moltres", "moltres-galar", "mewtwo", "raikou", "entei", "suicune", "lugia", "ho-oh", "regirock", "regice", "registeel", "latias", "latios", "kyogre", "kyogre-primal", "groudon", "groudon-primal", "rayquaza", "uxie", "mesprit", "azelf", "dialga", "dialga-origin", "palkia", "palkia-origin", "heatran", "regigigas", "giratina", "giratina-origin", "cresselia", "cobalion", "terrakion", "virizion", "tornadus-incarnate", "tornadus-therian", "thundurus-incarnate", "thundurus-therian", "reshiram", "zekrom", "landorus-incarnate", "landorus-therian", "kyurem", "kyurem-black", "kyurem-white", "xerneas", "yveltal", "zygarde-10-power-construct", "zygarde-50-power-construct", "zygarde-complete", "tapu-koko", "tapu-lele", "tapu-bulu", "tapu-fini", "cosmog", "cosmoem", "solgaleo", "lunala", "necrozma", "necrozma-dusk", "necrozma-dawn", "necrozma-ultra", "zacian", "zacian-crowned", "zamazenta", "zamazenta-crowned", "eternatus", "kubfu", "urshifu-rapid-strike", "urshifu-single-strike", "regieleki", "regidrago", "glastrier", "spectrier", "calyrex", "calyrex-ice", "calyrex-shadow", "enamorus-incarnate", "enamorus-therian", "wo-chien", "chien-pao", "ting-lu", "chi-yu", "koraidon", "miraidon", "okidogi", "munkidori", "fezandipiti", "ogerpon", "ogerpon-wellspring-mask", "ogerpon-hearthflame-mask", "ogerpon-cornerstone-mask", "terapagos", "terapagos-terastal", "terapagos-stellar"]
            pokemon = random.choice(legendarios)
        elif self.contents.get() == "random-mythical":
            miticos = ["mew", "celebi", "jirachi", "deoxys-normal", "deoxys-attack", "deoxys-defense", "deoxys-speed", "phione", "manaphy", "darkrai", "shaymin-land", "shaymin-sky", "arceus", "victini", "keldeo-ordinary", "keldeo-resolute", "meloetta-aria","meloetta-pirouette", "genesect", "diancie", "hoopa", "hoopa-unbound", "volcanion", "magearna", "magearna-original", "marshadow", "zeraora", "meltan", "melmetal", "zarude", "zarude-dada", "pecharunt"]
            pokemon = random.choice(miticos)
        elif self.contents.get() == "random-ultraente":
            ultraentes = ["nihilego", "buzzwole", "pheromosa", "xurkitree", "celesteela", "kartana", "guzzlord", "poipole", "naganadel", "stakataka", "blacephalon"]
            pokemon = random.choice(ultraentes)
        elif self.contents.get() == "random-shiny":
            self.shiny = True
            pokemon = random.randint(1,1025)
        elif self.contents.get() == "random-type":
            tipos = ["normal", "fire", "water", "electric", "grass", "ice", "fighting", "poison", "ground", "flying", "psychic", "bug", "rock", "ghost", "dragon", "dark", "steel", "fairy"]
            self.insert(f"Se eligio un tipo aletorio: {random.choice(tipos)}")
        elif self.contents.get() == "random-type-normal":
            pokemon = random.randint(1,1025)
            while not requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}").json()["types"][0]["type"]["name"] == "normal":
                pokemon = random.randint(1,1025)
        elif self.contents.get() == "random-type-fire":
            pokemon = random.randint(1,1025)
            while not requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}").json()["types"][0]["type"]["name"] == "fire":
                pokemon = random.randint(1,1025)
        elif self.contents.get() == "random-type-water":
            pokemon = random.randint(1,1025)
            while not requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}").json()["types"][0]["type"]["name"] == "water":
                pokemon = random.randint(1,1025)
        elif self.contents.get() == "random-type-electric":
            pokemon = random.randint(1,1025)
            while not requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}").json()["types"][0]["type"]["name"] == "electric":
                pokemon = random.randint(1,1025)
        elif self.contents.get() == "random-type-grass":
            pokemon = random.randint(1,1025)
            while not requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}").json()["types"][0]["type"]["name"] == "grass":
                pokemon = random.randint(1,1025)
        elif self.contents.get() == "random-type-ice":
            pokemon = random.randint(1,1025)
            while not requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}").json()["types"][0]["type"]["name"] == "ice":
                pokemon = random.randint(1,1025)
        elif self.contents.get() == "random-type-fighting":
            pokemon = random.randint(1,1025)
            while not requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}").json()["types"][0]["type"]["name"] == "fighting":
                pokemon = random.randint(1,1025)
        elif self.contents.get() == "random-type-poison":
            pokemon = random.randint(1,1025)
            while not requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}").json()["types"][0]["type"]["name"] == "poison":
                pokemon = random.randint(1,1025)
        elif self.contents.get() == "random-type-ground":
            pokemon = random.randint(1,1025)
            while not requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}").json()["types"][0]["type"]["name"] == "ground":
                pokemon = random.randint(1,1025)
        elif self.contents.get() == "random-type-flying":
            pokemon = random.randint(1,1025)
            while not requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}").json()["types"][0]["type"]["name"] == "flying":
                pokemon = random.randint(1,1025)
        elif self.contents.get() == "random-type-psychic":
            pokemon = random.randint(1,1025)
            while not requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}").json()["types"][0]["type"]["name"] == "psychic":
                pokemon = random.randint(1,1025)
        elif self.contents.get() == "random-type-bug":
            pokemon = random.randint(1,1025)
            while not requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}").json()["types"][0]["type"]["name"] == "bug":
                pokemon = random.randint(1,1025)
        elif self.contents.get() == "random-type-rock":
            pokemon = random.randint(1,1025)
            while not requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}").json()["types"][0]["type"]["name"] == "rock":
                pokemon = random.randint(1,1025)
        elif self.contents.get() == "random-type-ghost":
            pokemon = random.randint(1,1025)
            while not requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}").json()["types"][0]["type"]["name"] == "ghost":
                pokemon = random.randint(1,1025)
        elif self.contents.get() == "random-type-dragon":
            pokemon = random.randint(1,1025)
            while not requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}").json()["types"][0]["type"]["name"] == "dragon":
                pokemon = random.randint(1,1025)
        elif self.contents.get() == "random-type-dark":
            pokemon = random.randint(1,1025)
            while not requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}").json()["types"][0]["type"]["name"] == "dark":
                pokemon = random.randint(1,1025)
        elif self.contents.get() == "random-type-steel":
            pokemon = random.randint(1,1025)
            while not requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}").json()["types"][0]["type"]["name"] == "steel":
                pokemon = random.randint(1,1025)
        elif self.contents.get() == "random-type-fairy":
            pokemon = random.randint(1,1025)
            while not requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}").json()["types"][0]["type"]["name"] == "fairy":
                pokemon = random.randint(1,1025)
        elif self.contents.get() == "random-color":
            colores = ["red", "blue", "yellow", "green", "black", "brown", "purple", "gray", "white", "pink"]
            self.insert(f"Se eligio un color aletorio: {random.choice(colores)}")
        elif self.contents.get() == "random-color-red":
            pokemon = random.randint(1,1025)
            while not requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}").json()["color"]["name"] == "red":
                pokemon = random.randint(1,1025)
        elif self.contents.get() == "random-color-blue":
            pokemon = random.randint(1,1025)
            while not requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}").json()["color"]["name"] == "blue":
                pokemon = random.randint(1,1025)
        elif self.contents.get() == "random-color-yellow":
            pokemon = random.randint(1,1025)
            while not requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}").json()["color"]["name"] == "yellow":
                pokemon = random.randint(1,1025)
        elif self.contents.get() == "random-color-green":
            pokemon = random.randint(1,1025)
            while not requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}").json()["color"]["name"] == "green":
                pokemon = random.randint(1,1025)
        elif self.contents.get() == "random-color-black":
            pokemon = random.randint(1,1025)
            while not requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}").json()["color"]["name"] == "black":
                pokemon = random.randint(1,1025)
        elif self.contents.get() == "random-color-brown":
            pokemon = random.randint(1,1025)
            while not requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}").json()["color"]["name"] == "brown":
                pokemon = random.randint(1,1025)
        elif self.contents.get() == "random-color-purple":
            pokemon = random.randint(1,1025)
            while not requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}").json()["color"]["name"] == "purple":
                pokemon = random.randint(1,1025)
        elif self.contents.get() == "random-color-gray":
            pokemon = random.randint(1,1025)
            while not requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}").json()["color"]["name"] == "gray":
                pokemon = random.randint(1,1025)
        elif self.contents.get() == "random-color-white":
            pokemon = random.randint(1,1025)
            while not requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}").json()["color"]["name"] == "white":
                pokemon = random.randint(1,1025)
        elif self.contents.get() == "random-color-pink":
            pokemon = random.randint(1,1025)
            while not requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}").json()["color"]["name"] == "pink":
                pokemon = random.randint(1,1025)
        elif self.contents.get() == "random-egg":
            huevos = ["monster", "water1", "bug", "flying", "field", "fairy", "grass", "human-like", "water3", "mineral", "amorphous", "water2", "ditto", "dragon", "undiscovered"]
            self.insert(f"Se eligio un grupo huevo aletorio: {random.choice(huevos)}")
        elif self.contents.get() == "random-egg-monster":
            pokemon = random.randint(1,1025)
            while not requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}").json()["egg_groups"][0]["name"] == "monster":
                pokemon = random.randint(1,1025)
        elif self.contents.get() == "random-egg-water1":
            pokemon = random.randint(1,1025)
            while not requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}").json()["egg_groups"][0]["name"] == "water1":
                pokemon = random.randint(1,1025)
        elif self.contents.get() == "random-egg-bug":
            pokemon = random.randint(1,1025)
            while not requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}").json()["egg_groups"][0]["name"] == "bug":
                pokemon = random.randint(1,1025)
        elif self.contents.get() == "random-egg-flying":
            pokemon = random.randint(1,1025)
            while not requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}").json()["egg_groups"][0]["name"] == "flying":
                pokemon = random.randint(1,1025)
        elif self.contents.get() == "random-egg-field":
            pokemon = random.randint(1,1025)
            while not requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}").json()["egg_groups"][0]["name"] == "field":
                pokemon = random.randint(1,1025)
        elif self.contents.get() == "random-egg-fairy":
            pokemon = random.randint(1,1025)
            while not requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}").json()["egg_groups"][0]["name"] == "fairy":
                pokemon = random.randint(1,1025)
        elif self.contents.get() == "random-egg-grass":
            pokemon = random.randint(1,1025)
            while not requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}").json()["egg_groups"][0]["name"] == "grass":
                pokemon = random.randint(1,1025)
        elif self.contents.get() == "random-egg-human-like":
            pokemon = random.randint(1,1025)
            while not requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}").json()["egg_groups"][0]["name"] == "human-like":
                pokemon = random.randint(1,1025)
        elif self.contents.get() == "random-egg-water3":
            pokemon = random.randint(1,1025)
            while not requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}").json()["egg_groups"][0]["name"] == "water3":
                pokemon = random.randint(1,1025)
        elif self.contents.get() == "random-egg-mineral":
            pokemon = random.randint(1,1025)
            while not requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}").json()["egg_groups"][0]["name"] == "mineral":
                pokemon = random.randint(1,1025)
        elif self.contents.get() == "random-egg-amorphous":
            pokemon = random.randint(1,1025)
            while not requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}").json()["egg_groups"][0]["name"] == "amorphous":
                pokemon = random.randint(1,1025)
        elif self.contents.get() == "random-egg-water2":
            pokemon = random.randint(1,1025)
            while not requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}").json()["egg_groups"][0]["name"] == "water2":
                pokemon = random.randint(1,1025)
        elif self.contents.get() == "random-egg-ditto":
            pokemon = random.randint(1,1025)
            while not requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}").json()["egg_groups"][0]["name"] == "ditto":
                pokemon = random.randint(1,1025)
        elif self.contents.get() == "random-egg-dragon":
            pokemon = random.randint(1,1025)
            while not requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}").json()["egg_groups"][0]["name"] == "dragon":
                pokemon = random.randint(1,1025)
        elif self.contents.get() == "random-egg-undiscovered":
            pokemon = random.randint(1,1025)
            while not requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}").json()["egg_groups"][0]["name"] == "undiscovered":
                pokemon = random.randint(1,1025)
        elif self.contents.get() == "random-shape":
            shapes = ["ball", "squiggle", "fish", "arms", "blob", "upright", "legs", "quadruped", "wings", "tentacles", "heads", "humanoid", "bug-wings", "armor"]
            self.insert(f"Se eligio una forma aletoria: {random.choice(shapes)}")
        elif self.contents.get() == "random-shape-ball":
            pokemon = random.randint(1,1025)
            while not requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}").json()["shape"]["name"] == "ball":
                pokemon = random.randint(1,1025)
        elif self.contents.get() == "random-shape-squiggle":
            pokemon = random.randint(1,1025)
            while not requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}").json()["shape"]["name"] == "squiggle":
                pokemon = random.randint(1,1025)
        elif self.contents.get() == "random-shape-fish":
            pokemon = random.randint(1,1025)
            while not requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}").json()["shape"]["name"] == "fish":
                pokemon = random.randint(1,1025)
        elif self.contents.get() == "random-shape-arms":
            pokemon = random.randint(1,1025)
            while not requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}").json()["shape"]["name"] == "arms":
                pokemon = random.randint(1,1025)
        elif self.contents.get() == "random-shape-blob":
            pokemon = random.randint(1,1025)
            while not requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}").json()["shape"]["name"] == "blob":
                pokemon = random.randint(1,1025)
        elif self.contents.get() == "random-shape-upright":
            pokemon = random.randint(1,1025)
            while not requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}").json()["shape"]["name"] == "upright":
                pokemon = random.randint(1,1025)
        elif self.contents.get() == "random-shape-legs":
            pokemon = random.randint(1,1025)
            while not requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}").json()["shape"]["name"] == "legs":
                pokemon = random.randint(1,1025)
        elif self.contents.get() == "random-shape-quadruped":
            pokemon = random.randint(1,1025)
            while not requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}").json()["shape"]["name"] == "quadruped":
                pokemon = random.randint(1,1025)
        elif self.contents.get() == "random-shape-wings":
            pokemon = random.randint(1,1025)
            while not requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}").json()["shape"]["name"] == "wings":
                pokemon = random.randint(1,1025)
        elif self.contents.get() == "random-shape-tentacles":
            pokemon = random.randint(1,1025)
            while not requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}").json()["shape"]["name"] == "tentacles":
                pokemon = random.randint(1,1025)
        elif self.contents.get() == "random-shape-heads":
            pokemon = random.randint(1,1025)
            while not requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}").json()["shape"]["name"] == "heads":
                pokemon = random.randint(1,1025)
        elif self.contents.get() == "random-shape-humanoid":
            pokemon = random.randint(1,1025)
            while not requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}").json()["shape"]["name"] == "humanoid":
                pokemon = random.randint(1,1025)
        elif self.contents.get() == "random-shape-bug-wings":
            pokemon = random.randint(1,1025)
            while not requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}").json()["shape"]["name"] == "bug-wings":
                pokemon = random.randint(1,1025)
        elif self.contents.get() == "random-shape-armor":
            pokemon = random.randint(1,1025)
            while not requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}").json()["shape"]["name"] == "armor":
                pokemon = random.randint(1,1025)
        elif self.contents.get() == "random-habitat":
            habitats = ["cave", "forest", "grassland", "mountain", "rare", "rough-terrain", "sea", "urban", "waters-edge"]
            self.insert(f"Se eligio un habitat aletorio: {random.choice(habitats)}")
            
        pokemon = str(pokemon)
        print("Poke random:", pokemon)
        return pokemon
