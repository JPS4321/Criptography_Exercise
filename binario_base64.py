#Misma tabla de conversion de los demas scripts. 
from tablas import tabla_base64

#Funcion que convierte un binario a decimal
def binario_a_decimal(binario):
    #Acumulador del resultado y exponente de la potencia 2 que corresponde a cada bit.
    decimal = 0
    potencia = len(binario) - 1
    
    for bit in binario:
        if bit == '1':
            decimal += 2 ** potencia
        potencia -= 1

    return decimal

#Como binario funciona en bloques de 6 bits, si la longitud del binario no es multiplo de 6, se le agrega ceros al final.
def dividir_en_bloques(binario):
    while len(binario) % 6 != 0:
        binario += '0'

    bloques = []
    #DIvide el flujo en bloques consecutivos de 6 bits
    for i in range(0, len(binario), 6):
        bloques.append(binario[i:i+6])

    return bloques


def binario_a_base64(binario, tabla_base64):
    #Guardara el resultado 
    resultado = ""
    #Lista de bloques de 6 bits
    bloques = dividir_en_bloques(binario)
    #Conversion de bloque por bloque
    for bloque in bloques:
        decimal = binario_a_decimal(bloque)
        resultado += tabla_base64[decimal]

    return resultado


entrada = "01001000011011110110110001100001"
salida = binario_a_base64(entrada, tabla_base64)

print("Binario:", entrada)
print("Base64:", salida)
