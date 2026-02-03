#Tabla de caracteres Base64 para conversiones
from tablas import tabla_base64

#Funcion que hace la conversion de Base64 a decimal
def base64_a_decimal(caracter, tabla_base64):
    return tabla_base64[caracter]

#Convierte decimal a binario de 6 bits
def decimal_a_binario(numero):
    #String vacio
    binario = ""
    '''Divide el numero entre 2
    guarda el residuo
    repite hasta que el numero sea 0
    construye el binario
    '''
    while numero > 0:
        residuo = numero % 2
        binario = str(residuo) + binario
        numero = numero // 2
    #Relleno para que sea de 6 bits. Esto porque base64 es 2^6 = 64. 
    while len(binario) < 6:
        binario = "0" + binario

    return binario

#Funcion que hace todo el proceso. 
def base64_a_binario(texto, tabla_base64):
    resultado_binario = ""

    for caracter in texto:
        #Ignorar el padding, es decir el relleno en base64. 
        if caracter == '=':
            continue

        decimal = base64_a_decimal(caracter, tabla_base64)
        binario = decimal_a_binario(decimal)
        resultado_binario += binario

    return resultado_binario


entrada = "SG9sYQ=="
salida = base64_a_binario(entrada, tabla_base64)

print("Texto Base64:", entrada)
print("Texto Binario:", salida)
