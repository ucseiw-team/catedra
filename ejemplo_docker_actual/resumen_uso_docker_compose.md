Necesitamos instalar docker compose con pip antes (recomendado usar un virtualenv):

```
pip install docker-compose
```

Y luego, se usa casi igual a docker: tenemos comandos para crear todos los contenedores, levantar todo, detener todo, borrar todos los contenedores, etc:

```
docker-compose up --no-start
docker-compose start
docker-compose stop
docker-compose down
```

Y también podemos correr el up y el start al mismo tiempo, y que se vean los logs en vivo en nuestra consola (lo detenemos con control-c y luego un down):

```
docker-compose up
```

Y podemos hacer super magia: escalar los servicios a la cantidad que necesitemos! (con o sin `--no-start`)

```
docker-compose up --scale web=50
```
