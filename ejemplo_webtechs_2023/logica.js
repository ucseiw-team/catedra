function actualizarNoticias() {
    console.log("actualizando las noticias...");
    console.log("listo!");
}

setInterval(actualizarNoticias, 3000);

function noAnda() {
    $("div#resultado").html("Anduvo!");
}

$("div.noticia h1").on("click", noAnda);

