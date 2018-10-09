import time
import random
from pathlib import Path
from datetime import datetime

path_datos = Path("/root/datos.txt")

if path_datos.exists():
    print("Existen datos anteriores:")
    with path_datos.open() as archivo_datos:
        print(archivo_datos.read())
else:
    print("No hay datos anteriores:")

nuevos_datos = random.randint(0, 100)
print("Escribiendo nuevos datos:")
print(nuevos_datos)
with path_datos.open("w") as archivo_datos:
    archivo_datos.write(str(nuevos_datos))

while True:
    time.sleep(3)
    print(datetime.now(), "Haciendo nada...")
