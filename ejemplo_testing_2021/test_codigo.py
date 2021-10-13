from codigo import Email, limpiar_inbox


def test_creacion_de_email_guarda_datos_correctamente():
    asunto = "hola!"
    texto = "cómo estás?"
    mail = Email(asunto, texto)

    assert mail.asunto == asunto
    assert mail.texto == texto


def test_un_mail_sano_no_tiene_puntaje_de_spam():
    email = Email("evento espadas!", "mañana venite a espadear")

    assert email.medir_spam() == 0


def test_un_mail_con_asunto_spamoso_es_bien_detectado():
    email = Email("oferta oferta espadas!", "muchas baratas")

    assert email.medir_spam() == 20


def test_un_mail_con_texto_spamoso_es_bien_detectado():
    email = Email("espadas copadas!", "muchas ofertas ofertas de espadas baratas")

    assert email.medir_spam() == 4


def test_un_mail_con_texto_spamoso_es_ignorado_en_modo_rapido():
    email = Email("espadas copadas!", "muchas ofertas ofertas de espadas baratas")

    assert email.medir_spam(modo_rapido=True) == 0


def test_un_mail_muy_spamoso_suma_todo_el_puntaje():
    email = Email("espadas en oferta!", "muchas ofertas ofertas de espadas baratas")

    assert email.medir_spam() == 14


def test_la_spamitud_no_depende_de_mayusculas_o_minusculas():
    email = Email("espadas en OFERTA!", "muchas ofertas OFERTAS de espadas baratas")

    assert email.medir_spam() == 14


def test_limpiar_inbox_borra_mails_spamosos_y_devuelve_el_resto(mocker):
    # este tiene puntaje 10, se va a borrar
    email1 = Email("espadas en oferta!", "")
    # estos tienen puntaje 0, no se borran
    email2 = Email("espadas!", "")
    email3 = Email("más espadas!", "")

    inbox = [email1, email2, email3]

    fake_borrar = mocker.patch("codigo.borrar", return_value="borrado!")

    clean_inbox, resultados = limpiar_inbox(inbox)

    # aseguramos que nos devuelve los que no son spam
    assert clean_inbox == [email2, email3]

    # aseguramos que se borraron los de spam
    fake_borrar.assert_called_once_with(email1)

    # aseguramos que devuelve los resultados de los borrados
    assert resultados == ["borrado!"]
