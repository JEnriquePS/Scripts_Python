# -*- coding: utf-8 *-*
__author__ = 'jenriqueps'
"""introducir dos numeros por teclado. Imprimir los numeros que hay entre ellos
comenzando por el mas pequeno. Contar cuantos hay y cuantos de ellos son
pares. Calcular la suma de los pares"""
numero1 = input("ingrese numero :")
numero2 = input("ingrese siguiente numero:")

lista = [numero1, numero2]
if numero1 == numero2:
    print("Los dos son iguales no hay numeros enteros entre ellos.")
else:
    num_max = max(lista)
    num_min1 = min(lista)
    num_min = num_min1 + 1
    rango_entre_numero = range((num_min), int(num_max))
    cantidad_de_numeros = len(rango_entre_numero)
    print("cantidad de numeros entre {} y {} es: {} " ).format(num_min1,
                                                               num_max,
                                                               cantidad_de_numeros)
    numeros_pares = []
    suma_pares = 0

    print('Los numeros Pares son:')
    for par in rango_entre_numero:
        if par % 2 == 0:
            numeros_pares.append(par)
            suma_pares += par

    print(numeros_pares)
    print("La cantidad total de pares es: {}").format(len(numeros_pares))
    print("La suma de los numeros pares es: {}").format(suma_pares)


