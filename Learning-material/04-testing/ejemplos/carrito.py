def subtotal(items):
    """items: lista de (precio, cantidad). Devuelve el subtotal."""
    return sum(precio * cant for precio, cant in items)

def aplicar_descuento(monto, porcentaje):
    if not 0 <= porcentaje <= 100:
        raise ValueError("porcentaje debe estar entre 0 y 100")
    return monto * (1 - porcentaje / 100)
