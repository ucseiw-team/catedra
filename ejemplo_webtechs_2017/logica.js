function saludar() {
    alert('hola mundo');
}
function sumar_clicks() {
    var elemento_html = $('#contador');
    var cantidad_actual = elemento_html.text();
    cantidad_actual = Number(cantidad_actual);
    cantidad_actual += 1;
    elemento_html.text(cantidad_actual.toString());
}
