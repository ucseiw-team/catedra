function onLoad() {
    setTimeout(updateContador, 1000);
    setTimeout(updateTitulosNoticias, 1000);
}

function updateContador() {
    $.ajax({url: urlAjaxContador}).done(datosContador);
}

function datosContador(data, options) {
    $('#contador_noticias').text(data.contador);

    console.log('llegaron datos:');
    console.log(data);

    setTimeout(updateContador, 1000);
}

function updateTitulosNoticias() {
    $.ajax({url: urlAjaxTitulos}).done(datosTitulosNoticias);
}

function datosTitulosNoticias(data, options) {
    $('#titulos_noticias').html(data);
    setTimeout(updateTitulosNoticias, 1000);
}

$(onLoad);
