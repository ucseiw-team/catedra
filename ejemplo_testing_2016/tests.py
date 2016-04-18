from unittest import TestCase
from codigo import empaquetar, Caja


class TestsEmpaquetar(TestCase):
    def test_si_no_recibe_productos_devuelve_caja_vacia(self):
        self.assertEquals(empaquetar([]), Caja(0, 0, 0, 0))

    def test_un_solo_producto_devuelve_caja_igual_al_producto(self):
        producto = Caja(1, 2, 3, 4)
        self.assertEquals(empaquetar([producto]), producto)
