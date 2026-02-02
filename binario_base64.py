tabla_base64 = {
    0:'A',  1:'B',  2:'C',  3:'D',  4:'E',  5:'F',  6:'G',
    7:'H',  8:'I',  9:'J',  10:'K', 11:'L', 12:'M', 13:'N',
    14:'O', 15:'P', 16:'Q', 17:'R', 18:'S', 19:'T', 20:'U',
    21:'V', 22:'W', 23:'X', 24:'Y', 25:'Z',
    26:'a', 27:'b', 28:'c', 29:'d', 30:'e', 31:'f', 32:'g',
    33:'h', 34:'i', 35:'j', 36:'k', 37:'l', 38:'m', 39:'n',
    40:'o', 41:'p', 42:'q', 43:'r', 44:'s', 45:'t', 46:'u',
    47:'v', 48:'w', 49:'x', 50:'y', 51:'z',
    52:'0', 53:'1', 54:'2', 55:'3', 56:'4', 57:'5',
    58:'6', 59:'7', 60:'8', 61:'9',
    62:'+', 63:'/'
}


def binario_a_decimal(binario):
    decimal = 0
    potencia = len(binario) - 1

    for bit in binario:
        if bit == '1':
            decimal += 2 ** potencia
        potencia -= 1

    return decimal


def dividir_en_bloques(binario):
    while len(binario) % 6 != 0:
        binario += '0'

    bloques = []

    for i in range(0, len(binario), 6):
        bloques.append(binario[i:i+6])

    return bloques


def binario_a_base64(binario, tabla_base64):
    resultado = ""
    bloques = dividir_en_bloques(binario)

    for bloque in bloques:
        decimal = binario_a_decimal(bloque)
        resultado += tabla_base64[decimal]

    return resultado


entrada = "01001000011011110110110001100001"
salida = binario_a_base64(entrada, tabla_base64)

print("Binario:", entrada)
print("Base64:", salida)
