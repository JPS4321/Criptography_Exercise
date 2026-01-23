BASE64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def a_binario_manual(numero, bits):
    """Convierte un número decimal a binario usando divisiones entre 2."""
    resultado = ""
    while numero > 0:
        resultado = str(numero % 2) + resultado
        numero = numero // 2

    return resultado.zfill(bits)


texto = input("Ingresa texto en Base64: ")
binario = ""

for caracter in texto:
    if caracter == "=":
        continue  # el padding no se convierte

    valor = BASE64.index(caracter)   # valor 0–63
    binario += a_binario_manual(valor, 6)  # Base64 usa 6 bits

print("Resultado en binario:")
print(binario)
