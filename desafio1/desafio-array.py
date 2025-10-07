# OBJETIVO: Escribir un programa que elimine los elementos duplicados de una
# lista, asegurando que solo queden elementos únicos.

lista1[] = input("Introduce un array, recuerda delimitar cada elemento por comas: ") 

# 1. Se crea una lista vacía que almacenará los elementos únicos.
lista_sin_duplicados = []

# 2. Se inicia un ciclo 'for' para recorrer cada 'elemento' en la 'lista1' original.
for elemento in lista1:
    # 3. Se comprueba si el 'elemento' actual NO está ya en nuestra nueva lista.
    if elemento not in lista_sin_duplicados:
        # 4. Si no está, se agrega a la lista 'lista_sin_duplicados'.
        # Si ya existe, el código simplemente ignora el elemento y continúa con el siguiente.
        lista_sin_duplicados.append(elemento)

# 5. Al final del ciclo, se imprime la nueva lista que solo contiene elementos únicos.
print(lista_sin_duplicados)