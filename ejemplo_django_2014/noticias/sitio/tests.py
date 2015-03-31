from django.test import TestCase
from models import Categoria, Noticia
from api import crear_policial
from datetime import datetime
from django.core.urlresolvers import reverse
import mock


class TestCrearPolicial(TestCase):
    def setUp(self):
        self.policiales = Categoria(nombre='policiales')
        self.policiales.save()

    def test_noticia_se_crea_correctamente(self):
        self.assertEquals(Noticia.objects.count(), 0)

        nueva = crear_policial()
        cantidad = Noticia.objects.filter(pk=nueva.pk).count()

        self.assertEquals(cantidad, 1)

    def test_noticia_creada_tiene_categoria_policiales(self):
        nueva = crear_policial()
        self.assertEquals(nueva.categoria, self.policiales)

    def test_fecha_no_es_futura(self):
        nueva = crear_policial()
        self.assertGreaterEqual(datetime.now(), nueva.fecha)

    def test_datos_noticia_aparecen_en_html_resultante(self):
        response = self.client.get(reverse('crear_policial'))
        nueva = Noticia.objects.get()

        self.assertEquals(response.status_code, 200)
        self.assertIn(nueva.titulo, response.content)
        self.assertIn(nueva.texto, response.content)

    def test_la_vista_tiene_que_usar_la_api(self):
        from sitio.views import crear_policial as crear_policial_de_views
        self.assertEquals(crear_policial, crear_policial_de_views)

        with mock.patch('sitio.views.crear_policial') as mock_api_crear:
            self.client.get(reverse('crear_policial'))
            self.assertTrue(mock_api_crear.called)
