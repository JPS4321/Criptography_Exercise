def xor_binario(binario1, binario2):
    resultado = ""

    for i in range(len(binario1)):
        bit1 = binario1[i]
        bit2 = binario2[i]

        if bit1 == bit2:
            resultado += '0'
        else:
            resultado += '1'

    return resultado


binario = "01001000011011110110110001100001"
clave   = "10101010101010101010101010101010"

resultado = xor_binario(binario, clave)

print("Binario original:", binario)
print("Clave XOR:       ", clave)
print("Resultado XOR:   ", resultado)
