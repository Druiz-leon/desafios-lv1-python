#OBJETIVO 1: Escribe un programa que encuentre el valor máximo o 
# mínimo en un array sin utilizar funciones integradas como max() o min().

lista=[8, 2, 40, 3, 4, 5, 80, 6, 7, 1]
numeroMin=lista[0]
numeroMax=lista[0]
for elemento in lista:
    if elemento > numeroMax:
        numeroMax = elemento
    if elemento < numeroMin:
        numeroMin = elemento
print(f"El número máximo es: {numeroMax}")
print(f"El número mínimo es: {numeroMin}")

#OBJETIVO 2: Escribe un programa que determine la longitud de una cadena 
# sin utilizar la función integrada len().

cadena = "Ejemplo de cadena para el desafio3 lv1"
contador = 0

for caracter in cadena:
    contador += 1

print(f"La longitud de la cadena es: {contador}")