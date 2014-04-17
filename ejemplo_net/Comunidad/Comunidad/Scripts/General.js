$(function () {
    $('#updateTime').click(function () {
        $.ajax({
            url: '/Home/GiveMeDate',
            data: {
                complete: true
            }
        }).done(function (result) {
            $('#datetime').html(result);
        });

        //$('#datetime').load('/Home/GiveMeDate', { complete: true }, function () {
        //    Mi código una vez cargado el contenido
        //});

        //$.get('/Home/GiveMeDate', { complete: true })
        //.done(function (result) {
        //    $('#datetime').html(result);
        //});
    });

    //setInterval(update, 1000);
});

//function update() {
//    $.get('/Home/GiveMeDate', { complete: true })
//        .done(function (result) {
//            $('#datetime').html(result);
//        });
//};