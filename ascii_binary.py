## Tabla ascii para realizar conversiones de caracteres a valores decimales.
from tablas import tabla_ascii

#Recibe un solo carcater, lo busca en la tabla ascii y lo devuelve 
def ascii_a_decimal(caracter, tabla_ascii):
    return tabla_ascii[caracter]

#Convierte un numero decimal a binario de 8 bits
def decimal_a_binario(numero):
    #Se incia el string vacio
    binario = ""
    # Divindo el numero entre 2, guarda el residuo hasta que sea 0 y lo guarda en el string
    while numero > 0:
        residuo = numero % 2
        binario = str(residuo) + binario
        numero = numero // 2
    # Mete un Relleno por si el binario es menor a 8 bits. 
    while len(binario) < 8:
        binario = "0" + binario

    return binario

# Funcio que ejecuta todo el proceso
def ascii_a_binario(caracter, tabla_ascii):
    decimal = ascii_a_decimal(caracter, tabla_ascii)
    binario = decimal_a_binario(decimal)
    return binario


texto = "Hola"

#Ciclo for para cada caracter.
for c in texto:
    print(ascii_a_binario(c, tabla_ascii))
