En versiones actuales, docker trae directamente adentro docker compose (antes se instalaba aparte con pip).

Se usa casi igual a docker: tenemos comandos para crear todos los contenedores, levantar todo, detener todo, borrar todos los contenedores, etc:

```
docker compose up --no-start  # esto crea los contenedores si no existen
docker compose start
docker compose stop
docker compose down  # esto borra los contenedores
```

Podemos consultar las cosas que tenemos corriendo referidas a nuestro proyecto con:

```
docker compose ps
```

Y también podemos correr el up y el start al mismo tiempo, y que se vean los logs en vivo en nuestra consola (lo detenemos con control-c y luego un down):

```
docker compose up
```

Y podemos hacer super magia: escalar los servicios a la cantidad que necesitemos! (con o sin `--no-start`)

```
docker compose up --no-start --scale web=25
```
