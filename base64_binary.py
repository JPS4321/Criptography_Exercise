import base64
texto = "SG9sYQ==" #Esto significa hola en base64. Lo encripte con uno online
#para convertir de base64 a binario se usa base64. No se si es legal
bytes_decodificados = base64.b64decode(texto)
binario = ''.join(format(byte, '08b') for byte in bytes_decodificados)
print("La palabra en binario es:", binario)
