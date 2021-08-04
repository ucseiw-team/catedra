from flask import Flask

app = Flask(__name__)

@app.route("/policiales")
def policiales():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>Página de ejemplo</title>
    <meta charset="utf-8"/>
    <style>
        h1 {
            color: red;
        }

        p {
            color: yellow;
            font-size: 9px;
        }

        #el_parrafo_de_bienvenida {
            color: blue;
            font-weight: 800;
        }

        p.parrafo_resaltado {
            background-color: green;
        }

        #pie_de_pagina p {
            background-color: #999999
        }

    </style>

    <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=" crossorigin="anonymous"></script>
</head>

<body>
    <h1>Noticias.com</h1>

    <p id="el_parrafo_de_bienvenida" class="parrafo_resaltado">Bienvenidos a el mejor sitio de noticias</p>

    <p>Noticia: fisa se robó otra espada más, van 100</p>

    <p class="parrafo_resaltado">Noticia de último momento: Nicolas se robó los videos de la materia</p>

    <img src="https://pbs.twimg.com/media/E71_E1vWUAI0RtM?format=jpg&name=small"/>

    <div id="pie_de_pagina">
        <p>Gracias, vuelva prontos</p>
        <p>Sitio hecho en vivo con mil problemas</p>

        <a href="/acerca_de">Acerca de</a>
    </div>

    <script>
        function bienvenir() {
            console.log("mostrando mensaje");
            //alert("hola, gracias por entrar!");
            $("#el_parrafo_de_bienvenida").html("Gracias por visitarnos");
            console.log("mensaje aceptado");

        }

        setTimeout(bienvenir, 3000);

    </script>

</body>
</html>
"""


@app.route("/acerca_de")
def acerca_de():
    return """
<!DOCTYPE html>
<html>
<body>
    Hecho por fisa renegando en vivo. Quién me manda.
</body>

</html>
"""

