// version de api que devuelve html
function pedir_actualizar_contador_html() {
    console.log("pidiendo contador html...");
    $.ajax({url: "/api/contador_noticias_html/"}).done(actualizar_contador_html);
    console.log("pedido lanzado");
}

function actualizar_contador_html(data) {
    console.log("recibido contador html");
    $("#contador-noticias-html").html(data);
}

// version de api que devuelve json
function pedir_actualizar_contador_json() {
    console.log("pidiendo contador json...");
    $.ajax({url: "/api/contador_noticias_json/"}).done(actualizar_contador_json);
    console.log("pedido lanzado");
}

function actualizar_contador_json(data) {
    console.log("recibido contador json");
    $("#contador-noticias-json").html("<p>Cantidad: " + data.cantidad_noticias.toString() + "</p>");
}



setInterval(pedir_actualizar_contador_html, 2000);
setInterval(pedir_actualizar_contador_json, 2000);

