
function contador() {
  p_contador = $('p#contador');
  var valor_actual = parseInt(p_contador.text());
  valor_actual = valor_actual + 1;
  p_contador.text(valor_actual.toString());
  setTimeout(contador, 1000);

  console.log(valor_actual);
}

setTimeout(contador, 1000);
