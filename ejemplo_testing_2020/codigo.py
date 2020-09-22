class Email:
    def __init__(self, asunto, texto):
        self.asunto = asunto
        self.texto = texto

    def medir_spam(self, modo_rapido=False):
        puntaje = self.asunto.lower().count("oferta") * 10

        if not modo_rapido:
            puntaje += self.texto.lower().count("oferta") * 2

        return puntaje

    def borrar(self):
        print("mensaje borrado!")


def limpiar_inbox(inbox):
    inbox_limpio = []

    for email in inbox:
        puntaje_spam = email.medir_spam(modo_rapido=True)
        if puntaje_spam > 5:
            email.borrar()
        else:
            inbox_limpio.append(email)

    return inbox_limpio
