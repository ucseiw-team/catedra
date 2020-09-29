Necesitamos instalar docker compose con pip antes (recomendado usar un virtualenv):

```
pip install docker-compose
```

Y luego, se usa casi igual a docker: tenemos comandos para levantar todo, bajar todo, borrar todos los contenedores, etc:

```
docker-compose start
docker-compose stop
docker-compose rm
```

Y también podemos levantar todo y ver en vivo los logs, con colores para cada servicio, y que si frenamos con control-c se detenga todo también:

```
docker-compose up
```

Y podemos hacer super magia: escalar los servicios a la cantidad que necesitemos!

```
docker-compose up --scale web=50
```
