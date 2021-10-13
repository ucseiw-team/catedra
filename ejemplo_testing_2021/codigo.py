class Email:
    def __init__(self, asunto, texto):
        self.asunto = asunto
        self.texto = texto

    def medir_spam(self, modo_rapido=False):
        puntaje = self.asunto.lower().count("oferta") * 10

        if not modo_rapido:
            puntaje += self.texto.lower().count("oferta") * 2

        return puntaje

    def __repr__(self):
        return f"<Email: {self.asunto}>"


def borrar(mail_a_borrar):
    # magia de db
    print("mensaje borrado!")

    return f"éxito! se borró el mail {mail_a_borrar.asunto}"


def limpiar_inbox(inbox):
    inbox_limpio = []
    resultados_borrados = []

    for email in inbox:
        puntaje_spam = email.medir_spam(modo_rapido=True)
        if puntaje_spam > 5:
            resultados_borrados.append(borrar(email))
        else:
            inbox_limpio.append(email)

    return inbox_limpio, resultados_borrados
