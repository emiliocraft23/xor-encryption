def xor(t, k):
    resultado = ""
    for i in range(0, len(t), 8):
        bloque = t[i:i+8]
        for j, c in enumerate(bloque):
            bit_llave = int(k[j])
            resultado += chr(ord(c) ^ bit_llave) 
    return resultado
t = "Hola mundo!"
k = "11001010"
c = xor(t, k)
print(f"Original: {t}\nLlave: {k}\nCifrado: {repr(c)}\nDescifrado: {xor(c, k)}")
