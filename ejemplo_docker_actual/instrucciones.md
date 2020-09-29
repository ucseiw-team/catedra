Compilar la imagen a partir del Dockerfile:

```
docker build -t my_web . 
```

Crear y correr un contenedor descartable con esa imagen (se muere y se borra cuando detengamos el proceso con ctrl-c):

```
docker run --rm -t -i my_web
```

Pero necesitamos mapear puertos para poder usar la web: que nuestramaquina:5000 vaya a elcontenedor:5000 (con la sintaxis `-p puerto_de_nuestra_maquina:puerto_del_contenedor`)

```
docker run --rm -t -i -p 5000:5000 my_web
```

Crear un contenedor con la imagen pero que no se borre solo (para poder iniciarlo y detenerlo muchas veces), y luego iniciarlo:

```
docker create --name web1 -p 5001:5000 my_web
docker start web1
```

Detener ese contenedor:

```
docker stop web1
```

Podemos crear varios, y levantar y matar de a varios juntos:

```
docker create --name web2 -p 5002:5000 my_web
docker create --name web3 -p 5003:5000 my_web

docker start web1 web2 web3
docker stop web1 web2 web3
```

También podemos borrarlos si no los vamos a usar más:

```
docker rm web1 web2 web3
```

Recordar que la data es efímera y no es compartida! Vive lo que viva el contenedor, no se comparte entre contenedores, y los contenedores son descartables! 
Así que la idea es NO tener datos adentro de los contenedores, los datos van afuera.

Si queremos que usen datos compartidos y persistentes, necesitamos definirles un volumen: les decimos que tal carpeta del contenedor, sea en realidad tal carpeta de nuestra máquina (dicho con la sintaxis `-v directorio_persistente_de_nuestra_maquina:directorio_del_contenedor`)

```
docker create --name web1 -p 5001:5000 -v /home/fisa/devel/ucse/seia/data_docker/:/myweb/data my_web
docker create --name web2 -p 5002:5000 -v /home/fisa/devel/ucse/seia/data_docker/:/myweb/data my_web

docker start web1 web2
```

Si usamos la web, podemos ver que los datos que guardan son compartidos, y podemos entrar a la carpeta /home/fisa/devel/ucse/seia/data_docker/ y ver los datos también.
Si detenemos o incluso borramos los contenedores, la data igualmente queda guardada en ese directorio.

También podemos meternos con una consola a un contenedor que está andando, para probar cosas:

```
docker exec -i -t web1 /bin/bash
```

También podemos borrar la imagen, si no la vamos a usar más y queremos liberar espacio. Pero no nos va a dejar si hay contenedores creados (corriendo o no) que usen esa imagen.

```
docker stop web1 web2
docker rm web1 web2
docker rmi my_web  # finalmente podemos borrar la imagen
```
