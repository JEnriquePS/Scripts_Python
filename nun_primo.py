def primo(num):
    """ Obtiene numeros Primos en un rango de (1,num)"""
    acumulador_suma = 0
    total_de_numeros_primos = 0
    while num > 1:
        count = 1
        count_nun_primos = 0

        while num >= count:
            if num % count == 0:
                count_nun_primos += 1
                count += 1
            else:
                count += 1
            if count_nun_primos > 2:
                break

        if count_nun_primos == 2:
            total_de_numeros_primos += 1
            acumulador_suma += num
            print ("Num-Primo-{}: {}".format(total_de_numeros_primos, num))

        num -= 1
        #print count
        #print count1

    print ("Suma Total de numeros Primos: {}".format(acumulador_suma))
    print ("Numeros Primos Encomtrados {}.".format(total_de_numeros_primos))

primo(5000)



