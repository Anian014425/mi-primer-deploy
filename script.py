# Variables básicas

nombre = "Mundo"

version = 3.12

intentos = [1, 2, 3]

 

# Operaciones y f-strings con formato avanzado

saludo = f"¡Hola, {nombre.upper()}!"

total_intentos = sum(intentos)

ratio = 100 / total_intentos

 

# Salida estructurada

print(saludo)

print(f"• Python versión: {version}")

print(f"• Intentos sumados: {' + '.join(map(str, intentos))} = {total_intentos}")

print(f"• Operación en f-string (100 / {total_intentos}): {ratio:.2f}%")

print(f"• Condicional en línea: {'Listo para despegar' if ratio > 10 else 'Pendiente'}")