tabla_base64 = {
    'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,
    'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,
    'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,
    'Y':24,'Z':25,
    'a':26,'b':27,'c':28,'d':29,'e':30,'f':31,'g':32,'h':33,
    'i':34,'j':35,'k':36,'l':37,'m':38,'n':39,'o':40,'p':41,
    'q':42,'r':43,'s':44,'t':45,'u':46,'v':47,'w':48,'x':49,
    'y':50,'z':51,
    '0':52,'1':53,'2':54,'3':55,'4':56,'5':57,'6':58,'7':59,
    '8':60,'9':61,
    '+':62,'/':63
}

def decimal_a_binario_6(numero):
    binario = ""

    while numero > 0:
        binario = str(numero % 2) + binario
        numero //= 2

    while len(binario) < 6:
        binario = "0" + binario

    return binario

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

    for c in mensaje:
        if c != '=':
            decimal = tabla_base64[c]
            binario += decimal_a_binario_6(decimal)

    texto = ""

    for i in range(0, len(binario), 8):
        byte = binario[i:i+8]
        if len(byte) == 8:
            texto += chr(binario_a_decimal(byte))

    return texto

mensaje_base64 = "SG9sYQ=="

resultado = base64_a_ascii(mensaje_base64)

print("Base64:", mensaje_base64)
print("ASCII:", resultado)
