# -*- coding: utf-8 *-*
__author__ = 'jenriqueps'
# Problema
"""introducir dos numeros por teclado. Imprimir los numeros que hay entre ellos
comenzando por el mas pequeno. Contar cuantos hay y cuantos de ellos son
pares. Calcular la suma de los pares"""
# Recibiendo numeros

def enter():
    "consistenciando funcion"
    if True:
        try:
            numero1 = input("ingrese numero :")
            numero2 = input("ingrese siguiente numero:")
            lista =[numero1, numero2]
            return lista
        except:
            print('Error')
        else:
            enter()
lista = enter()

if lista[0] == lista[1]:
    print("Los dos son iguales no hay numeros enteros entre ellos.")
else:
    num_max = max(lista)    # obteniendo el numero mayor
    num_min1 = min(lista)   # obteniendo el numero menor
    num_min = num_min1 + 1  # aumentando  mas 1 al numero menor par eleminarlo
                            # del rango
    rango_entre_numero = range((num_min), (num_max))    # obteniendo rango
    cantidad_de_numeros = len(rango_entre_numero)   # cantidad de numeros
    print("cantidad de numeros entre {} y {} es: {} " ).format(num_min1,
                                                               num_max,
                                                               cantidad_de_numeros)
    numeros_pares = []      # lista de numeros pares
    suma_pares = 0          # variable almacena la suma de los numeros pares

    print('Los numeros Pares son:')
    # declarando bucle para obtener numeros pares y añadirlos a variable
    # numeros_pares
    for par in rango_entre_numero:
        if par % 2 == 0:
            numeros_pares.append(par)
            suma_pares += par

    print(numeros_pares)
    print("La cantidad total de pares es: {}").format(len(numeros_pares))
    print("La suma de los numeros pares es: {}").format(suma_pares)

