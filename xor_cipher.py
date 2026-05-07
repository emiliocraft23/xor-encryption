def xor(t, k):
    resultado = ""
    for i, c in enumerate(t):
        bit_llave = int(k[i % len(k)])
        resultado += chr(ord(c) ^ bit_llave)
    return resultado

t = "Hola Mundo!"
k = "11001010"
c = xor(t, k)
print(f"Original: {t}\nLlave: {k}\nCifrado: {repr(c)}\nDescifrado: {xor(c, k)}")