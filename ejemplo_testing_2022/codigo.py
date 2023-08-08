class Email:
    def __init__(self, asunto, texto):
        self.asunto = asunto
        self.texto = texto

    def medir_spam(self, modo_rapido=False):
        puntaje = self.asunto.count("oferta") * 10

        if not modo_rapido:
            puntaje += self.texto.count("oferta") * 2

        return puntaje

    def __repr__(self):
        return f"<Email: {self.asunto}>"


def borrar(email_a_borrar):
    # código que haga cosas en la db
    print("borrando mail...")

    return f"mail borrado: {email_a_borrar.asunto}"


def limpiar_inbox(inbox):
    inbox_limpio = []
    emails_borrados = []
    resultados_borrados = []

    for email in inbox:
        puntaje_spam = email.medir_spam(modo_rapido=True)
        if puntaje_spam > 5:
            emails_borrados.append(email)
            resultado = borrar(email)
            resultados_borrados.append(resultado)
        else:
            inbox_limpio.append(email)

    return inbox_limpio, emails_borrados, resultados_borrados
