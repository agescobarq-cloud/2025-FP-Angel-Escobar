# Crear y escribir en el archivo my_notes.txt
with open('my_notes.txt', 'w') as file:
    # Escribir tres líneas de notas personales
    file.write("Nota 1: Recordar terminar la tarea de Python.\n")
    file.write("Nota 2: Comprar víveres el fin de semana.\n")
    file.write("Nota 3: Llamar a mamá para el domingo.\n")

# Abrir y leer el archivo my_notes.txt
with open('my_notes.txt', 'r') as file:
    # Leer el contenido línea por línea
    line = file.readline()
    while line:
        # Mostrar cada línea en la consola
        print(line.strip())  # strip() elimina espacios y saltos de línea adicionales
        line = file.readline()

# Nota: El uso de 'with' asegura que el archivo se cierre automáticamente