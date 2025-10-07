# OBJETIVO: Escribir un programa que verifique si una cadena o
# número se lee igual hacia adelante que hacia atrás.

# 1. Pedimos al usuario que ingrese el texto o número a verificar.
entrada_usuario = input("Introduce una cadena o número para verificar: ")

# 2. Preparamos la cadena para la comparación:
#    - Convertimos todos los caracteres a minúsculas con .lower()
#    - Eliminamos espacios y caracteres no alfanuméricos (como ',', '.', '!', '?')
#      para quedarnos solo con letras y números usando .isalnum()
cadena_limpia = ''.join(char for char in entrada_usuario.lower() if char.isalnum())

# 3. Creamos la versión invertida de la cadena limpia.
#    La notación [::-1] es un truco de Python para invertir cualquier secuencia.
cadena_invertida = cadena_limpia[::-1]

# 4. Comparamos la cadena limpia con su versión invertida.
if cadena_limpia == cadena_invertida:
    # Si son idénticas, es un palíndromo.
    print("Sí es un palíndromo!")
else:
    # De lo contrario, no lo es.
    print("No es un palíndromo")