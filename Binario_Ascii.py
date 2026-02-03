from tablas import tabla_base64_ASCII as tabla_base64

# Convertir numero decimal a binario de 6 bits
def decimal_a_binario_6(numero):
    binario = ""

    # Divide el numero entre 2 hasta que sea 0
    while numero > 0:
        binario = str(numero % 2) + binario
        numero //= 2

    # Relleno a 6 bits
    while len(binario) < 6:
        binario = "0" + binario

    return binario

# Convertir binario a decimal
def binario_a_decimal(binario):
    decimal = 0
    potencia = len(binario) - 1

    for bit in binario:
        if bit == '1':
            decimal += 2 ** potencia
        potencia -= 1

    return decimal


def base64_a_ascii(mensaje):
    binario = ""

    # BASE64 a BINARIO
    for c in mensaje:
        if c != '=':  # ignora padding
            decimal = tabla_base64[c]
            binario += decimal_a_binario_6(decimal)

    texto = ""

    # BINARIO a ASCII
    for i in range(0, len(binario), 8):
        byte = binario[i:i+8]
        if len(byte) == 8:
            texto += chr(binario_a_decimal(byte))

    return texto


mensaje_base64 = "SG9sYQ=="
resultado = base64_a_ascii(mensaje_base64)

print("Base64:", mensaje_base64)
print("ASCII:", resultado)
