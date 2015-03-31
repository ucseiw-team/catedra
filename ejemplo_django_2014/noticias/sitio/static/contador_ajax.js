
function contador() {
  /* ajax usando un template como resultado */
  p_contador = $('#contador');
  p_contador.load(Urls.sumar_numero(p_contador.text()));

  /* ajax usando datos en json como resultado */
  p_contador_json = $('#contador_json');
  $.ajax({
      "url": Urls.sumar_numero_json(p_contador_json.text()),
      "dataType": "json"
  }).done(
    function (result) {
      p_contador_json.text(result.numero.toString());
      console.log(result);
      debugger;
  });
  
  setTimeout(contador, 1000);
}

setTimeout(contador, 1000);
