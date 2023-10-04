import api_gmail


class Email:
    def __init__(self, asunto, texto):
        self.asunto = asunto
        self.texto = texto
        self.enviado = False

    def medir_spam(self):
        puntaje = self.asunto.lower().count("oferta") * 10
        puntaje += self.texto.lower().count("oferta") * 2

        return puntaje

    def enviar(self):
        id_envio = api_gmail.conectar_y_enviar(self.asunto, self.texto)

        if id_envio is None:
            resultado = {"error": "No se pudo enviar el mail"}
        else:
            self.enviado = True
            resultado = {"id_envio": id_envio}

        return resultado
