import requests


lista=[]
"""for i in range(1, 1026):
    result = requests.get("https://pokeapi.co/api/v2/pokemon/"+str(i))
    shiny = result.json()["sprites"]["front_shiny"]
    shiny_female = result.json()["sprites"]["front_shiny_female"]
    if shiny == None:
        if shiny_female == None:
            print("No shiny")
            lista.append(i)
print(lista)
print("se analizo todo lo basico")"""
#De estas todas son shinys, no hay ninguna que no tenga shiny

"""rg = range(10001 10279)
for i in (rg):#No entiendo porque aunque de error y no tenga sentido al ejecutarlo espera y cuando cambio el nombre de "rg" funciona
    result = requests.get("https://pokeapi.co/api/v2/pokemon/"+str(i))
    shiny = result.json()["sprites"]["front_shiny"]
    shiny_female = result.json()["sprites"]["front_shiny_female"]
    if shiny is None and shiny_female is None:
        print("No shiny")
        lista.append(i)
print(f"Sin shiny: {lista} tiene {len(lista)} elementos")
print("se analizaron todas las formas")"""

for i in range(10001, 10280):
    result = requests.get("https://pokeapi.co/api/v2/pokemon/"+str(i))
    shiny = result.json()["sprites"]["front_shiny"]
    shiny_female = result.json()["sprites"]["front_shiny_female"]
    if shiny is None and shiny_female is None:
        print("No shiny")
        lista.append(i)
print(f"Sin shiny: {lista} tiene {len(lista)} elementos")
print("se analizaron todas las formas")

for elemento in lista:
    result = requests.get("https://pokeapi.co/api/v2/pokemon/"+str(elemento))
    print(result.json()["name"])
#Para cuando necesite volver a mirarlo:
#[10128, 10129, 10146, 10153, 10154, 10158, 10159, 10160, 10182, 10183, 10190,
# 10216, 10217, 10264, 10265, 10266, 10267, 10268, 10269, 10270, 10271, 10278, 10279]
#Esto es todo lo que hay, son las 22 formas sin Shiny aparente
#10128, 10129, 10146, 10153 y 1015 son lurantis-totem, salazzle-totem, kommo-o-totem, araquanid-totem y togedemaru-totem
#10158 y 10159 son pikachu-starter y eevee-starter
#10160 es pikachu-world-cap
#10182 y 10183 son cramorant-gulping y cramorant-gorging
#10190 es eternatus-etermax que solo tiene front_default
#10216 y 10217 son flapple-gmax y appletun-gmax
#10264, 10265, 10266 y 10267 son koraidon-limited-build, koraidon-sprinting-build, koraidon-swimming-build y koraidon-gliding-build
#10268, 10269, 10270 y 10271 son miraidon-low-power-mode, miraidon-drive-mode, miraidon-aquatic-mode y miraidon-glide-mode
#10278 y 10279 son frisllish-female y jellicent-female, al parecer serian formas a parte pero decidieron retirarlas