function pedir_contadores() {
    $.ajax({url: '/contador_noticias_ajax/'}).done(actualizar_contadores).error(error_actualizar_contadores);
}


function actualizar_contadores(data, options) {
    $('#cantidad-noticias').text(data.cantidad_noticias);
    $('#cantidad-noticias-archivadas').text(data.cantidad_noticias_archivadas);
}


function error_actualizar_contadores() {

}


function al_cargar_base() {
    setInterval(pedir_contadores, 3000);
}


$(al_cargar_base)
