Palabra = "Hola"
binario = ''.join(format(ord(c), '08b') for c in Palabra)
print("La palabra en binario es:", binario)