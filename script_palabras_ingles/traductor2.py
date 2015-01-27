#-*-encoding:utf-8-*-


parientes = {'aunt': [['tia'], ['áont']],
             'bachelor': [['soltero', 'soltera'], ['beíchelor']],
             'brother in law': [['cuniado'], ['brázar in lóu']],  #poner ñ
             'brother': [['hermano'], ['brazár']],
             'children': [['hijos'], ['children']],
             'cousin': [['primo', 'prima'], ['cósin']],
             'daddy': [['papa'], ['dádi']],
             'daughter in law': [['nuera'], ['dótar in lóu']],
             'daughter': [['hija'], ['dótar']],
             'divorced': [['divociado', 'divorciada'], ['divórsd']],
             'engaged': [['comprometido', 'comprometida'], ['enguéiched']],
             'family': [['familia'], ['fémili']],
             'father in law': [['suegro'], ['fázar in lóu']],
             'father': [['padre'], ['fázar']],
             'foster daughter': [['hija adoptiva'], ['fóster dótar']],
             'foster son': [['hijo adoptivo', 'hija adoptiva'], ['fóster son']],
             'granddaughter': [['nieta'], ['grand dótar']],
             'grandfather': [['abuelo'], ['grand fázar']],
             'grandmother': [['abuela'], ['grand mázar']],
             'grandparents': [['abuelos'], ['grand parents']],
             'grandson': [['nieto'], ['grand son']],
             'husband': [['esposo'], ['júsband']],
             'married': [['casado', 'casada'], ['mérid']],
             'mommy': [['mama'], ['moni']],
             'mother in law': [['suegra'], ['mázar in lóu']],
             'mother': [['madre'], ['mázar']],
             'nephew': [['sobrino'], ['néfiu']],
             'niece': [['sobrina'], ['nis']],
             'orphan': [['huerfano', 'huerfana'], ['órfan']],
             'parents': [['padres'], ['parénts']],
             'relatives': [['parientes'], ['rélativs']],
             'single': [['soltero', 'soltera'], ['sínguel']],
             'sister in law': [['cuniada'], ['sister in lóu']],  # poner ñ
             'sister': [['hermana'], ['sister']],
             'son in law': [['yerno'], ['son in lóu']],
             'son': [['hijo'], ['son']],
             'stepdaughter': [['hijastra'], ['step-dótar']],
             'stepfather': [['padrastro'], ['step-fázar']],
             'stepmother': [['madrastra'], ['step-mázar']],
             'stepson': [['hijastro'], ['step-son']],
             'twins': [['gemelos'], ['tuíns']],
             'uncle': [['tio'], ['ónkel']],
             'widow': [['viudo', 'viuda'], ['uídou']],
             'widower': [['viudo', 'viuda'], ['uídouer']],
             'wife': [['esposa'], ['uáif']]
            }

meses = {'January': [['enero'], ['chyánuari']],
         'February': [['febrero'], ['fébruari']],
         'March': [['marzo'], ['march']],
         'April': [['abril'], ['éipril']],
         'May': [['mayo'], ['méi']],
         'June': [['junio'], ['chyun']],
         'July': [['julio'], ['chyulái']],
         'August': [['agosto'], ['ógost']],
         'September': [['septiembre'], ['septémber']],
         'October': [['octubre'], ['octóber']],
         'November': [['noviembre'], ['novémber']],
         'December': [['diciembre'], ['dicémber']]
        }

dias_semana = {'Monday': [['lunes'], []],
               'Tuesday': [['martes'], []],
               'Wednesday': [['miercoles'], []],
               'Thursday': [['jueves'], []],
               'Friday': [['viernes'], []],
               'Saturday': [['sabado'], []],
               'Sunday': [['domingo'], []]}

frases_populares = {'Yes': [['si'], ['ies']],
                    'No': [['no'], ['no']]}

adjetivos_posesivos = {'My': [['mi'], []],
             'Your': [['tu'], []],
             'His': [['de el'], []],
             'Her': [['de ella'], []],
             'Its': [['de el'], []],
             'Our': [['nuestro'], []],
             'your': [['de ustedes'], []],
             'Their': [['su'], []]}

pronombres_personales = {'I': [['yo'], ['i']],
                         'You': [['tu'], ['iu']],
                         'He': [['el'], ['ji']],
                         'She': [['ella'], ['shi']],
                         'It': [['el', 'ella'], ['it']],
                         'We': [['nosotros'], ['ui']],
                         'They': [['ellos'], ['zei']]}

verbos = {
          'cook': [['cocinar'], []],
          'dance': [['bailar'], []],
          'drive': [['manejar'], []],
          'fix': [['arreglar'], []],
          'go': [['ir'], []],
          'hear': [['escuchar'], []],
          'make': [['hacer'], []],
          'open': [['abrir'], []],
          'paint': [['pintar'], []],
          'play': [['jugar'], []],
          'read': [['leer'], []],
          'ride': [['montar'], []],
          'run': [['correr'], []],
          'sing': [['cantar'], []],
          'speak': [['hablar'], []],
          'stay': [['estar'], []],
          'study': [['estudiar'], []],
          'swim': [['nadar'], []],
          'type': [['tipear'], []],
          'write': [['escribir'], []]
          }

cuerpo = {
          'Body': [['cuerpo'], []],
          'head': [['cabeza'], []],
          'neck': [['cuello'], []],
          'shoulder': [['hombro'], []],
          'arm': [['brazo'], []],
          'elbow': [['codo'], []],
          'hand': [['mano'], []],
          'finger': [['dedo'], []],
          'chest': [['pecho'], []],
          'belly': [['barriga'], []],
          'leg': [['pierna'], []],
          'knee': [['rodilla'], []],
          'foot': [['pie'], ['fut']],
          'feet': [['pies'], ['fiit']],
          'nail': [['unia'], []],
          'muscle': [['musculo'], []],
          'bone': [['hueso'], []],
          'skin': [['piel'], []],
          'hair': [['pelo'], []],
          'back': [['espalda'], []]
          }

adverbios = {
             'although': [['aunque'], []],
             'as a result': [['como consecuencia'], []],
             'at first': [['al principio'], []],
             'because': [['porque'], []],
             'besides': [['ademas'], []],
             'but': [['pero', 'aunque'], []],
             'despite the fact': [['a pesar de'], []],
             'finally': [['finalmente'], []],
             'first of all': [['antes que nada'], []],
             'firstly': [['en primer lugar'], []],
             'however': [['sin embargo', 'no obstante'], []],
             'in addition': [['ademas'], []],
             'in my opinion': [['desde mi punto de vista'], []],
             'in my view': [['desde mi punto de vista'], []],
             'secondly': [['en segundo lugar'], []],
             'the truth is that': [['la verdad es que'], []],
             'therefore': [['por lo tanto'], []],
             'though': [['aunque'], []]
             }

preposiciones = {
                 'about': [['acerca de', 'sobre de', 'alrededor de', 'aproximadamente'], []],
                 'above': [['por encima de', 'sobre'], []],
                 'across': [['a traves de'], []],
                 'after': [['detras de', 'despues de'], []],
                 'along': [['a lo largo de'], []],
                 'among': [['entre'], []],
                 'around': [['alrededor de', ' aproximadamente', 'sobre'], []],
                 'as': [['como'], []],
                 'at': [['en', 'a'], []],
                 'before': [['antes que', 'antes de', 'delante de'], []],
                 'below': [['debajo de', 'bajo'], []],
                 'beside': [['al lado de', 'junto a'], []],
                 'between': [['entre'], []],
                 'by': [['por', 'junto a', 'por delante de', 'de acuerdo con', 'alrededor de'], []],
                 'down': [['abajo'], []],
                 'during': [['durante'], []],
                 'for': [['en direcciona', 'desde hace', 'por'], []],
                 'from': [['de', 'desde', 'a partir de'], []],
                 'in': [['en', 'dentro de'], []],
                 'inside': [['dentro de'], []],
                 'into': [['en'], []],
                 'near': [['cerca de'], []],
                 'next to': [['al lado de'], []],
                 'of': [['de'], []],
                 'off': [['fuera de', 'saliendo de'], []],
                 'on': [['sobre', 'encima', 'en'], []],
                 'opposite': [['enfrente de'], []],
                 'outside': [['fuera de'], []],
                 'over': [['sobre', 'por encima de', 'al otro lado de'], []],
                 'round': [['alrededor de', 'cerca de', 'aproximadamente'], []],
                 'since': [['desde'], []],
                 'through': [['a traves de'], []],
                 'to': [['hacia', 'a', 'hasta'], []],
                 'towards': [['hacia'], []],
                 'under': [['debajo de'], []],
                 'until': [['hasta'], []],
                 'up': [['arriba de'], []],
                 'with': [['con'], []],
                 'without': [['sin'], []]
                 }
verbos_irregulares = {
                      'as': [['como'], []],
                      }

var = locals()
list_string = []


def listado():
    variable_delete = ['var', 'list_string', 'variable_delete', 'listado']
    for variable in var.keys():
        if variable.startswith('__'):
            del variable
        elif variable in variable_delete:
            del variable
        else:
            list_string.append(variable)
    list_string.sort()
    return list_string
