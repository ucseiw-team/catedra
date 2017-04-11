function click_actualizar_noticias() {
    $.ajax({url: '/lista_noticias_ajax/'}).done(actualizar_noticias).error(error_actualizar_noticias);
}


function actualizar_noticias(data, options) {
    $('#lista-noticias').html(data);
}


function error_actualizar_noticias() {
    $('#lista-noticias').html('Error al cargar las noticias');
}


function al_cargar_inicio() {
    $('#actualizar-noticias').on('click', click_actualizar_noticias);    
}


$(al_cargar_inicio)
