import requests
import pandas as pd
import time

csv_generos="pruebas/pokemon_app/Listas/d_generos.csv"
csv=open(csv_generos)
csv_generos2="pruebas/pokemon_app/Listas/d_generos.csv"
csv2=open(csv_generos2)
def sacar_variantes():
    for i in range(1, 1025):
        result = requests.get("https://pokeapi.co/api/v2/pokemon-species/"+str(i))
        dg = result.json()["has_gender_differences"]
        rate= result.json()["gender_rate"]
        print(f"Buscando el pokemon numero {i}")
        time.sleep(0.5)
        if dg == True:
            print(f" El pokemon numero {i} tiene diferencias de genero")
            v=pd.DataFrame([{'id': i, 'dg': dg, 'gender_rate': rate}])
            v.to_csv(csv_generos, mode='a', header=False, index=False)
            # Eliminar duplicados si existen
            df = pd.read_csv(csv_generos, header=None, names=['id', 'dg', 'gender_rate'])
            df.drop_duplicates(inplace=True)
            df.to_csv(csv_generos, mode='w', header=False, index=False)
            
def sacar_porcentajes():
    for i in range(1, 1025):
        result = requests.get("https://pokeapi.co/api/v2/pokemon-species/"+str(i))
        rate = result.json()["gender_rate"]
        name = result.json()["name"]
        if rate == -1:
            rate = "Sin genero"
        elif rate == 0:
            rate == "100% Machos"
        elif rate == 1:
            rate = "87.5% Machos"
        elif rate == 2:
            rate = "75% Machos"
        elif rate == 3:
            rate = ""
        elif rate == 4:
            rate = "50% Machos"
        elif rate == 5:
            rate = ""
        elif rate == 6:
            rate = "25% Machos"
        elif rate == 7:
            rate = "12.5% Machos"
        elif rate == 8:
            rate = "0% Machos"
        print(f"Buscando el pokemon numero {i}")
        v=pd.DataFrame([{'id': i, 'name': name, 'gender_rate': rate}])
        v.to_csv(csv_generos2, mode='a', header=False, index=False)
        # Eliminar duplicados si existen
        df = pd.read_csv(csv_generos2, header=None, names=['id', 'name', 'gender_rate'])
        df.drop_duplicates(inplace=True)
        df.to_csv(csv_generos2, mode='w', header=False, index=False)
            
#sacar_porcentajes()

lista=[]
def contar_diferencias(lista):
    
    for i in range(1, 1025):
        time.sleep(0.5)
        print(f"Buscando el pokemon numero {i}")
        result = requests.get("https://pokeapi.co/api/v2/pokemon-species/"+str(i))
        gr=result.json()["gender_rate"]
        lista = lista + gr
    
    return sorted(set(lista))


#print(contar_diferencias(lista))

def listar_porcentajes():
    rates_csv="pruebas/pokemon_app/Listas/d_rates.csv"
    csv_rates=open(rates_csv)
    for i in range(1, 1026):
            result = requests.get("https://pokeapi.co/api/v2/pokemon-species/"+str(i))
            dg = result.json()["has_gender_differences"]
            rate= result.json()["gender_rate"]
            pv = result.json()["varieties"][0]["pokemon"]["name"]
            if rate == -1:
                rate = "Sin genero"
            elif rate == 0:
                rate = 100
            elif rate == 1:
                rate = 87.5
            elif rate == 2:
                rate = 75
            elif rate == 3:
                rate = ""
            elif rate == 4:
                rate = 50
            elif rate == 5:
                rate = ""
            elif rate == 6:
                rate = 25
            elif rate == 7:
                rate = 12.5
            elif rate == 8:
                rate = 0
            print(pv)
            if "-male" in pv:
                for j in range(2):
                    if j == 0:
                        rate = 100
                    else:
                        rate = 0
                    pv = result.json()["varieties"][j]["pokemon"]["name"]
                    v=pd.DataFrame([{'id': i, 'name':pv, 'dg': dg, 'gender_rate': rate}])
                    v.to_csv(rates_csv, mode='a', index=False)

            else:
                v=pd.DataFrame([{'id': i, 'name':pv, 'dg': dg, 'gender_rate': rate}])
                v.to_csv(rates_csv, mode='a', index=False)
            # Eliminar duplicados si existen
            df = pd.read_csv(rates_csv, names=['id', 'name', 'dg', 'gender_rate'])
            df.drop_duplicates(inplace=True)
            df.to_csv(rates_csv, mode='w', index=False)
listar_porcentajes()