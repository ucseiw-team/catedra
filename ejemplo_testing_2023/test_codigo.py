from codigo import Email


def test_spamitud_es_cero_para_mails_normales():
    mail = Email("fisa fue a nerdearla", "estuvo genial!")
    nivel_spam = mail.medir_spam()

    assert nivel_spam == 0


def test_asunto_spamoso_es_detectado():
    mail = Email("oferta oferta! compre", "estuvo genial!")
    nivel_spam = mail.medir_spam()

    assert nivel_spam == 20


def test_texto_spamoso_es_detectado():
    mail = Email("buenas!", "ayer me pasaron esta oferta. Te parece buena Oferta?")
    nivel_spam = mail.medir_spam()

    assert nivel_spam == 4


def test_spamitud_considera_ambos_campos():
    mail = Email("Oferta genial!", "no te pierdas esta oferta")
    nivel_spam = mail.medir_spam()

    assert nivel_spam == 12


def test_al_enviar_un_mail_se_marca_y_devolvemos_el_id(mocker):
    fake_api = mocker.patch("codigo.api_gmail", autospec=True)
    fake_api.conectar_y_enviar.return_value = 42

    mail = Email("fisa fue a nerdearla", "estuvo genial!")
    resultado = mail.enviar()

    assert mail.enviado
    assert resultado["id_envio"] == 42


def test_al_enviar_un_mail_se_usa_correctamente_la_api_de_gmail(mocker):
    fake_api = mocker.patch("codigo.api_gmail", autospec=True)

    mail = Email("fisa fue a nerdearla", "estuvo genial!")
    mail.enviar()

    fake_api.conectar_y_enviar.assert_called_once_with(mail.asunto, mail.texto)


def test_al_fallar_un_envio_no_se_marca_e_informamos_el_error(mocker):
    fake_api = mocker.patch("codigo.api_gmail", autospec=True)
    fake_api.conectar_y_enviar.return_value = None

    mail = Email("fisa fue a nerdearla", "estuvo genial!")
    resultado = mail.enviar()

    assert not mail.enviado
    assert resultado["error"] == "No se pudo enviar el mail"
