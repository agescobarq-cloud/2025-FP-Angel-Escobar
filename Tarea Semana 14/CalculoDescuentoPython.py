def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento / 100)
    monto_final = monto_total - descuento
    return descuento, monto_final

# Llamada a la función con el porcentaje por defecto (10%)
monto1 = 1000
descuento1, final1 = calcular_descuento(monto1)
print(f"Compra 1: Monto total = ${monto1:.2f}, Descuento (10%) = ${descuento1:.2f}, Monto final = ${final1:.2f}")

# Llamada a la función con un porcentaje personalizado (20%)
monto2 = 2000
porcentaje2 = 20
descuento2, final2 = calcular_descuento(monto2, porcentaje2)
print(f"Compra 2: Monto total = ${monto2:.2f}, Descuento ({porcentaje2}%) = ${descuento2:.2f}, Monto final = ${final2:.2f}")