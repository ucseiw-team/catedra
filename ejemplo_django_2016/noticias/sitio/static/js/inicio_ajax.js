function pedir_lista_noticias() {
    console.log('pdiendo lista');

    $.ajax({url: url_lista_ajax}).done(actualizar_lista_noticias).error(setear_actualizacion_lista_noticias);
}

function actualizar_lista_noticias(data, options) {
    console.log('llego la lista de noticias');
    $('#lista-noticias').html(data);
    setear_actualizacion_lista_noticias();
}

function setear_actualizacion_lista_noticias() {
    window.setTimeout(pedir_lista_noticias, 5000);
}


function pedir_contador_noticias() {
    console.log('pidiendo contador');
    $.ajax({url: url_contador_ajax}).done(actualizar_contador_noticias).error(setear_actualizacion_contador_noticias);
}

function actualizar_contador_noticias(data, options) {
    console.log('llego la contador de noticias');
    $('#contador-noticias').html(data.cantidad);
    setear_actualizacion_contador_noticias();
}

function setear_actualizacion_contador_noticias() {
    window.setTimeout(pedir_contador_noticias, 5000);
}

function cuando_este_cargada() {
    pedir_lista_noticias();
    pedir_contador_noticias();
}

$(cuando_este_cargada)
