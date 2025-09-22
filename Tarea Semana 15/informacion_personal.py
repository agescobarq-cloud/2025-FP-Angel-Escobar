# 1. Crear un diccionario con información personal ficticia
informacion_personal = {
    "nombre": "Ana García",
    "edad": 30,
    "ciudad": "Madrid",
    "profesion": "Ingeniera de Software"
}
# Imprimir diccionario inicial para verificación
print("Diccionario inicial:", informacion_personal)

# 2. Acceder y modificar el valor de "ciudad"
# Accedemos al valor de la clave "ciudad"
print("\nCiudad actual:", informacion_personal["ciudad"])
# Modificamos el valor de la clave "ciudad"
informacion_personal["ciudad"] = "Barcelona"
print("Ciudad modificada:", informacion_personal["ciudad"])

# Agregar una nueva clave-valor (aunque "profesion" ya existe, para este ejemplo
# asumimos que se pide agregar otra profesión o una clave diferente)
informacion_personal["hobby"] = "Fotografía"
print("Diccionario tras agregar hobby:", informacion_personal)

# 3. Verificar existencia de la clave "telefono"
if "telefono" not in informacion_personal:
    # Si no existe, la agregamos con un número ficticio
    informacion_personal["telefono"] = "+34 123 456 789"
    print("\nTeléfono añadido:", informacion_personal["telefono"])
else:
    print("\nLa clave 'telefono' ya existe")

# 4. Eliminar la clave "edad"
del informacion_personal["edad"]
print("\nDiccionario tras eliminar 'edad':", informacion_personal)

# 5. Imprimir el diccionario final
print("\nDiccionario final:", informacion_personal)