function cuando_este_cargada() {
    //saludar();
    //window.setTimeout(saludar, 10000);
    $('p strong').on('click', saludar);
    $('#sumador').on('click', sumar_clicks);
}

$(cuando_este_cargada)
