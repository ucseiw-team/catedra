function saludar() {
    alert('hola!');
}

function actualizarContador(e) {
    e.preventDefault();

    var valorActual = parseInt($('.contador:first').text());
    valorActual += 1;
    $('.contador').text(valorActual);
}

function alInicio() {
    $('#link-inicio').on('click', saludar);
    $('#link-contador').on('click', actualizarContador);
    // setTimeout(saludar, 3000);
}

// ejecutar al terminar de cargar la pagina
$(alInicio);


// esto seria lo mismo:
/*
$(function () {
    $('#link-inicio').on('click', function() {
        alert('hola!');
    });

    $('#link-contador').on('click', function(e) {
        e.preventDefault();

        var valorActual = parseInt($('.contador:first').text());
        valorActual += 1;
        $('.contador').text(valorActual);
    });
});
*/
