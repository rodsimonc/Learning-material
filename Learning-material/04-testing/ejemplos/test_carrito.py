import pytest
from carrito import subtotal, aplicar_descuento

def test_subtotal_suma_bien():
    assert subtotal([(100, 2), (50, 1)]) == 250

def test_subtotal_carrito_vacio():
    assert subtotal([]) == 0

@pytest.mark.parametrize("monto,pct,esperado", [
    (100, 0, 100),
    (100, 10, 90),
    (100, 100, 0),
])
def test_descuento(monto, pct, esperado):
    assert aplicar_descuento(monto, pct) == esperado

def test_descuento_invalido_lanza_error():
    with pytest.raises(ValueError):
        aplicar_descuento(100, 150)
