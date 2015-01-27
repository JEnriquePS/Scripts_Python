#-*-encoding:utf-8-*-
import random
from traductor2 import var, listado


class Diccionario:
    list_string = listado()

    def __init__(self):
        self.choice_category()
        self.enter()
        self.letters_keys()
        self.solution()
        self.final()

    def choice_category(self):
        """Imprimiendo lista de opciones"""
        #for para recorrer lista_string y imprimir las cadenas
        i = 0
        for options in self.list_string:
            i += 1
            print('{0}.-{1}'.format(i, options.capitalize()))

    def enter(self):
        count_list = len(self.list_string)
        try:
            choices_categories = input('Seleciona un numero:\t')
            number_choices = choices_categories - 1
            if number_choices in range(0, count_list):
                #self.listado diccionario escogido
                self.listado = var[self.list_string[number_choices]]
            else:
                self.enter()
        except:
            print('ingresastes un numero raro')
            self.enter()
        else:
            print('Comencemos')

    def letters_keys(self):
        """toma el diccionario escogido en -*-choices_categorys-*- para
        seleccionar las claves y despues retornar un lista ordenada al azar"""
        self.key_listado = self.listado.keys()
        random.shuffle(self.key_listado)

    def word_start(self):
        input_word = raw_input('cual es tu traduccion de {0}?:\n'.format(
            self.word_choose.capitalize()))

        #eliminado los espacios en blancos
        buscar = " "
        remplazar = ""
        input_word2 = input_word.replace(buscar, remplazar)

        #verificando si input_word solo tiene letras del alfabeto
        if input_word:
            if input_word2.isalpha():
                #convierte las letras a minusculas
                self.letter_lower = input_word.lower()
            else:
                print('Escribe una palabra')
                self.word_start()
        else:
            print('Escribe tu respuesta')
            self.word_start()

    def solution(self):
        #recorriendo la lista
        for word in self.key_listado:
            #pasando word a una variable para llevarla a la funcion word_start
            self.word_choose = word
            #obteniendo el valor de la clave word en listado
            en_letter = self.listado[word]
            en_letter1 = en_letter[0]
            en_letter2 = en_letter[1]
            for n in range(1, 4):
                if n < 3:
                    self.word_start()
                    choice_word = self.letter_lower
                    if choice_word in en_letter1:
                        if en_letter2:
                            print('Muy Bien se pronuncia "{0}"\n'
                                  'Tambien pudo ser {1}'.format(en_letter2[0],
                                                                en_letter1))
                            break
                        else:
                            print('Muy Bien Tambien pudo ser {0}'.format(
                                en_letter1))
                            break
                elif n == 3:
                    print('ultimo intento')
                    self.word_start()
                    choice_word = self.letter_lower
                    if choice_word in en_letter1:
                        if en_letter2:
                            print('Muy Bien se pronuncia "{0}"\n'
                                  'Tambien pudo ser {1}'.format(en_letter2[0],
                                                                en_letter1))
                            break
                        else:
                            print('Muy Bien Tambien pudo ser {0}'.format(
                                en_letter1))
                            break
                    else:
                        print('La Traduccion correcta es: {}'.format(en_letter1))

    def final(self):
        answer = raw_input('¿Deseas Salir?\n')
        answer = answer.lower()
        list_positive = ['si', 'yes']
        list_negative = ['no', 'not']
        if answer in list_positive:
            exit(0)
        elif answer in list_negative:
            self.__init__()
        else:
            self.final()

dictionary = Diccionario()
