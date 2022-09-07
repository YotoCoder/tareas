def cargar_diccionario_ingredientes():
    """
    lee el archivo ingredientes.txt y con esa información
    carga el diccionario de ingredientes a ser usado mas adelante
    """

    with open('ingredientes.txt', 'r', encoding='utf-8') as archivo:
        separador = ' '
        ingredientes = {}
        
        for linea in archivo:
            clave, valor = linea.split(separador)
            ingredientes[clave.strip()] = int(valor.strip())

        return ingredientes

def cargar_diccionario_recetas():
    """
    lee el archivo recetas.csv y con esa información carga el
    Diccionario de recetas a ser usado mas adelante
    """
    with open('recetas.csv', 'r', encoding='utf-8') as archivo:
        diccionario_recetas = {}
        
        for linea in archivo:
            linea = linea.rstrip('\n')
            linea = list(linea.split(','))
            diccionario_recetas[linea.pop(0)] = linea
        
    return diccionario_recetas

def print_stocks(): 
    """
    A partir del diccionario de ingredientes genera el listado que debe imprimirse 
    """
    print('Stock actual de ingredientes disponibles')

    for clave in diccionario_ingredientes:
        print(f'{clave} {diccionario_ingredientes[clave]}')

def reponer_ingredientes(lista_ingredientes):
    """
    después de cada operación de preparación o reposición
    se le pasa la lista de ingredientes a reponer y le
    suma uno al stock de cada uno de los que aparecen en el diccionario
    """
    for clave in lista_ingredientes:
        try:
            if diccionario_ingredientes[clave] >= 0:
                diccionario_ingredientes[clave] = diccionario_ingredientes[clave] + 1
        except:
            pass
    print_stocks()

def preparar_receta(receta):
    """
    Se le pasa el nombre de una receta con lo cual extrae desde el
    diccionario de recetas la lista de ingredientes para actualizar con ello el diccionario de
    ingredientes (ojo con los casos especiales)
    """
    disponibilidad = True

    try:
        for clave in diccionario_recetas[receta]:
            if diccionario_ingredientes[clave] > 0:
                disponibilidad = True
            else:
                disponibilidad = False
                print(f'*** No se puede hacer {receta} porque falta {clave} ***')
                print_stocks()
                return 0

        if disponibilidad:
            for clave in diccionario_recetas[receta]:
                if diccionario_ingredientes[clave]:
                    diccionario_ingredientes[clave] -= 1

    except:
        print(f'*** Lo sentimos pero no preparamos {receta} ***\n')
    print_stocks()

# Cargar ingredientes
diccionario_ingredientes = cargar_diccionario_ingredientes()

# Cargar recetas
diccionario_recetas = cargar_diccionario_recetas()

activo = True

while activo:

    try:
        orden = list(input('Ingresa la receta que quieres o REPONER: ').split(' '))
        if orden[0] == 'PREPARAR':
            preparar_receta(orden[1])
        elif orden[0] == 'REPONER':
            reponer_ingredientes(orden)
        elif orden[0] == 'STOP':
            activo = False
        else:
            print('Ingrese un comando valido')
    except:
        print('A ocurrido un error...')
        activo = False