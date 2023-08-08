from codigo import Email, borrar, limpiar_inbox


def test_los_atributos_se_guardan_correctamente():
    m = Email("espada nueva!", "hay una espada nueva")

    assert m.asunto == "espada nueva!"
    assert m.texto == "hay una espada nueva"


def test_mail_sano_no_genera_valor_de_spam():
    m = Email("espada nueva!", "hay una espada nueva")

    assert m.medir_spam() == 0


def test_mail_con_asunto_spamoso_es_detectado():
    m = Email("espada en oferta!", "hay una espada nueva")

    assert m.medir_spam() == 10


def test_mail_con_texto_spamoso_es_detectado():
    m = Email("espada nueva!", "hay una espada nueva en oferta")

    assert m.medir_spam() == 2


def test_modo_rapido_deja_pasar_textos_spamosos():
    m = Email("espada nueva!", "hay una espada nueva en oferta")

    assert m.medir_spam(modo_rapido=True) == 0


def test_spamosidad_final_es_resultado_de_spamosidad_de_texto_y_asunto():
    m = Email("espada nueva oferta oferta!", "hay una espada nueva en oferta oferta")

    assert m.medir_spam() == 24


def test_limpiar_inbox_borra_mails_spamosos(mocker):
    fake_borrar = mocker.patch("codigo.borrar", return_value="borrado!")

    m_spam1 = Email("espada nueva oferta!", "hay una espada nueva")
    m_spam2 = Email("espada nueva oferta!", "hay una espada nueva")
    m_bien1 = Email("espada nueva!", "hay una espada nueva")
    m_bien2 = Email("espada nueva!", "hay una espada nueva")

    inbox = [m_spam1, m_bien1, m_spam2, m_bien2]

    inbox_limpio, emails_borrados, resultados_borrados = limpiar_inbox(inbox)

    assert inbox_limpio == [m_bien1, m_bien2]
    assert emails_borrados == [m_spam1, m_spam2]
    assert resultados_borrados == ["borrado!", "borrado!"]

    # fake_borrar.assert_called_once_with(m_spam1)
    fake_borrar.assert_has_calls([
        mocker.call(m_spam1),
        mocker.call(m_spam2),
    ])
    assert fake_borrar.call_count == 2
