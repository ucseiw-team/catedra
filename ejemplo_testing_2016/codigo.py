from collections import namedtuple

Caja = namedtuple('Caja', 'x y z peso')

PESO_MAXIMO = 1000


def empaquetar(productos):
    z = 0

    if not productos:
        return Caja(0, 0, 0, 0)

    if sum(producto.peso for producto in productos) > PESO_MAXIMO:
        return None

    for producto in productos:
        z = z + producto.z

    caja_resultante = Caja(
        x=max(producto.x for producto in productos),
        y=max(producto.y for producto in productos),
        z=z,
        peso=sum(producto.peso for producto in productos),
    )

    return caja_resultante
