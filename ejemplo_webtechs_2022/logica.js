function actualizarNoticias() {
    console.log("actualizando las noticias...");
    console.log("listo!");
}

actualizarNoticias();

setInterval(actualizarNoticias, 3000);

function noSePuedeBajar() {
    alert("No se pueden bajar las imagenes");
}

$("div.noticia img").on("click", noSePuedeBajar);
