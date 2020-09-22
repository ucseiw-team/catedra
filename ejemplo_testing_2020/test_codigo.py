from codigo import Email, limpiar_inbox


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


def test_limpieza_de_inbox_saca_mails_spamosos(mocker):
    mail_normal = Email("", "")
    mail_normal2 = Email("", "")
    mail_spam = Email("", "")

    fake_medir_normal = mocker.patch.object(mail_normal, "medir_spam", return_value=0)
    fake_medir_normal2 =mocker.patch.object(mail_normal2, "medir_spam", return_value=3)
    fake_medir_spam = mocker.patch.object(mail_spam, "medir_spam", return_value=999)

    inbox = [mail_normal, mail_normal2, mail_spam]

    nuevo_inbox = limpiar_inbox(inbox)

    assert nuevo_inbox == [mail_normal, mail_normal2]

    fake_medir_normal.assert_called_once_with(modo_rapido=True)
    fake_medir_normal2.assert_called_once_with(modo_rapido=True)
    fake_medir_spam.assert_called_once_with(modo_rapido=True)

