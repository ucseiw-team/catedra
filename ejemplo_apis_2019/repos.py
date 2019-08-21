"""
Ejemplo de consumo de api sin usar lib específica para esa api, solamente haciendo requests http
y leyendo las respuestas a mano, y que no requiere OAuth.
"""
import requests


# hacemos una request para pedir datos
response = requests.get("https://api.github.com/users/fisadev/repos?sort=pushed")

# los datos vienen en el body como json. El método json() nos procesa eso y nos lo da como un
# diccionario de python.
if response.status_code == 200:
    data = response.json()
    print("10 most recently updated repos from fisadev:")
    print()
    for repo in data[0:10]:
        print(repo["name"], ":", repo["description"])
else:
    print("Response didn't return a normal result. HTTP response code:", response.status_code)
