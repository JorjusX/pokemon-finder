import requests
import pandas as pd
import time

def sacar_variantes():
    for i in range(1, 1025):
        result = requests.get("https://pokeapi.co/api/v2/pokemon-species/"+str(i))
        variantes = result.json()['varieties']
        print(f"Buscando el pokemon numero {i}")
        if len(variantes) > 1:
            time.sleep(0.5)
            for j in range(0, len(variantes)):
                variante = variantes[j]['pokemon']['name']
                if "-" in variante:
                    print(variante)
                    v=pd.DataFrame([{'id': i, 'variante': variante}])
                    v.to_csv("pruebas/pokemon_app/listas/variantes.csv", mode='a', header=False, index=False)
                    # Eliminar duplicados si existen
                    df = pd.read_csv("pruebas/pokemon_app/listas/variantes.csv", header=None, names=['id', 'variante'])
                    df.drop_duplicates(inplace=True)
                    df.to_csv("pruebas/pokemon_app/listas/variantes.csv", mode='w', header=False, index=False)
                    print(f"{i},{variante}")
                    print(v)
            

sacar_variantes()
    
#print(lista).to_csv(csv_variantes, index=False)

"""def sacar_variantes2(lista):
    for i in range(1, 1025):
        result = requests.get("https://pokeapi.co/api/v2/pokemon-species/"+str(i))
        variantes = result.json()['varieties']
        print(f"Buscando el pokemon numero {i}")
        time.sleep(0.5)
        for j in range(1, len(variantes)):
            variante = variantes[j]['pokemon']['name']
            v=pd.DataFrame([{'id': i, 'variante': variante}])
            with open("pruebas/pokemon_app/variantes.json", 'a') as f:
                v.to_json(f, orient='records', lines=True)
            print(f"{i},{variante}")
            print(v)
            
            
    print(sorted(lista))

sacar_variantes2(lista)"""

