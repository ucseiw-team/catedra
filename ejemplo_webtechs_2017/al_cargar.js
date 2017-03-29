function cuando_este_cargada() {
    // saludar();
    // window.setTimeout(saludar, 10000);
    $('p strong').on('click', saludar);
    $('#sumador').on('click', sumar_clicks);
    window.setTimeout(function() {
      $('#sumador').addClass('btn btn-success');
    }, 10000);
}

$(cuando_este_cargada)
