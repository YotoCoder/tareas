# libreria nativa para limpiar la consola
import os

# declarando variables globales
ip = input('\n\nIngrese la dirección ip si no tiene una presione enter: ')
clase = ''

# Octetos en binario
def calcular_mascara_sub_red():
    # Lista de octetos
    x = [0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0]

    for i in range(prefijo):
        x[i] = 1

    # diviendo octetos
    oct1 = x[0:8]
    oct2 = x[8:16]
    oct3 = x[16:24]
    oct4 = x[24:32] 

    # declarando variables de tipo string
    n1 = str()
    n2 = str()
    n3 = str()
    n4 = str()

    # recorriendo el octeto y convirtiendole a string 
    for i in oct1:
        n1 += str(i)
    # casteando de string binario a decimal
    oct1 = int(str(n1), 2)

    for j in oct2:
        n2 += str(j)
    # casteando de string binario a decimal    
    oct2 = int(str(n2), 2)

    for k in oct3:
        n3 += str(k)
    # casteando de string binario a decimal
    oct3 = int(str(n3), 2)

    for l in oct4:
        n4 += str(l)
    oct4 = int(str(n4), 2)

    # Mascara de sub red
    mascara_sub_red = (str(oct1) + '.' + str(oct2) + '.' + str(oct3) + '.' + str(oct4))
    
    # accediendo a variable global para poder manipularla dentro de la función
    global clase
    # determinar la clase de la mascara
    if(oct2 == 0):
        clase = 'A'
    elif(oct3 == 0):
        clase = 'B'
    elif(oct4 == 0):
        clase = 'C'
    
    print(f'Clase: {clase}')

    # /8 -> Clase A (255.0.0.0)
    # /16 -> Clase B (255.255.0.0)
    # /24 -> Clase C (255.255.255.0)

    return mascara_sub_red

# Convirtiendo ip ingresada a binario
def ip_a_binario():
    # Declarando lista vacia
    ip_bi = ['','','','']

    indice = 0

    for i in ip:
        if i == '.':
            indice += 1
            continue
        ip_bi[indice] += i

    ip_bin_1 = format(int(ip_bi[0]), '08b')
    ip_bin_2 = format(int(ip_bi[1]), '08b')
    ip_bin_3 = format(int(ip_bi[2]), '08b')
    ip_bin_4 = format(int(ip_bi[3]), '08b')

    return ([list(str(ip_bin_1)), list(str(ip_bin_2)), list(str(ip_bin_3)), list(str(ip_bin_4))])

# Claculadora del broadcast
def calcular_broadcast():
    ip_binaria = list(ip_a_binario())
    x = 4
    z = bits_de_host

    # Recorriendo lista en reversa para añadir valores binarios
    for i in reversed(ip_binaria):
        y = 8
        x -= 1

        for j in reversed(i):
            y -= 1
            z -= 1
            if(z >= 0):
                ip_binaria[x][y] = '1'
    
    # Convertir de lista a string
    t = ''
    for i in ip_binaria[0]:
        t += i
    t1 = ''
    for i in ip_binaria[1]:
        t1 += i
    t2 = ''
    for i in ip_binaria[2]:
        t2 += i
    t3 = ''
    for i in ip_binaria[3]:
        t3 += i

    # Retornando los octetos en base decimal de tipo string

    return (str(int(str(t), 2)) + '.' + str(int(str(t1), 2)) + '.' + str(int(str(t2), 2)) + '.' + str(int(str(t3), 2)))

# Calculadora de subred 
def calcular_sub_red():
    ip_binaria = list(ip_a_binario())
    broadcast = []
    x = 4
    z = bits_de_host

    for i in reversed(ip_binaria):
        y = 8
        x -= 1

        for j in reversed(i):
            y -= 1
            z -= 1
            if(z >= 0):
                ip_binaria[x][y] = '0'
    t = ''
    for i in ip_binaria[0]:
        t += i
    t1 = ''
    for i in ip_binaria[1]:
        t1 += i
    t2 = ''
    for i in ip_binaria[2]:
        t2 += i
    t3 = ''
    for i in ip_binaria[3]:
        t3 += i

    return (str(int(str(t), 2)) + '.' + str(int(str(t1), 2)) + '.' + str(int(str(t2), 2)) + '.' + str(int(str(t3), 2)))
     
# si no se ingresa la ip solo se pedira el prefijo de subred al usuario
if not ip:
    os.system('cls')

    prefijo = int(input('No se ingresó una ip por favor ingrese el prefijo para calcular las ips validas: '))

    print(f'\nSu Prefijo: /{prefijo}\n')

    # calculando bist de host
    bits_de_host = 32 - prefijo

    # Calculando ips maximos
    ips_maximos = 2 ** bits_de_host

    # Calculando hosts maximos
    hosts_maximos = (2 ** bits_de_host) - 2

    # Imprimiendo datos del servidor
    print(f'IPs maximos: {ips_maximos}')
    print(f'IPs Disponibles: {hosts_maximos}')
    print(f'\nMascara de sub red: {calcular_mascara_sub_red()}')

    ip = ''

    if(clase == 'A'):
        ip = '192.0.0.1'
    elif(clase == 'B'):
        ip = '192.168.0.1'
    elif(clase == 'C'):
        ip = '192.168.192.1'

    # /8 -> Clase A (255.0.0.0)
    # /16 -> Clase B (255.255.0.0)
    # /24 -> Clase C (255.255.255.0)

    print(f'Su ip asignada: {ip}')

else:    
    prefijo = int(input('Ingrese el prefijo de subred: '))

    print(f'\nSu IP: {ip} \nSu Prefijo: /{prefijo}\n')

    # calculando bist de host
    bits_de_host = 32 - prefijo

    # Calculando ips maximos
    ips_maximos = 2 ** bits_de_host

    # Calculando hosts maximos
    hosts_maximos = (2 ** bits_de_host) - 2

    broadcast = calcular_broadcast()
    mascara = calcular_mascara_sub_red()
    subred = calcular_sub_red()

    # Imprimiendo datos del servidor
    print(f'IPs maximos: {ips_maximos}')
    print(f'Ips disponibles: {hosts_maximos}')
    print(f'\nMascara de sub red: {mascara}')
    print(f'Direccion de red: {subred}/{prefijo}')
    print(f'Broadcast: {broadcast}\n\n')

    # identificar si la ip es valida
    if(ip == broadcast or ip == subred):
        print(f'Su dirección ip: {ip} es invalida, no puede ser igual al broadcast o la subred.\n')

    else:
        print(f'Su ip: {ip} es valida bienvenido.\n')