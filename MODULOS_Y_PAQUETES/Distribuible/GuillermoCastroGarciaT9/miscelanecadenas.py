def porcentaje(frase, cc=4):
    palabras = frase.split()
    total_palabras = len(palabras)
    
    palabras_menos_cc = []
    for palabra in palabras:
        if len(palabra) < cc:
            palabras_menos_cc.append(palabra)
    porcentaje_menos_cc = (len(palabras_menos_cc) / total_palabras) * 100
    
    porcentaje_mas_cc = 100 - porcentaje_menos_cc
    
    return porcentaje_menos_cc, porcentaje_mas_cc

def histograma(frase):
    frecuencia_vocales = {}
    vocales = "aeiouAEIOU"
    
    for letra in frase:
        if letra in vocales:
            frecuencia_vocales[letra] = frecuencia_vocales.get(letra, 0) + 1

    def obtener_frecuencia(item):
        return item[1]
    
    for vocal, frecuencia in sorted(frecuencia_vocales.items(), key=obtener_frecuencia, reverse=True):
        print(f"{vocal} {frecuencia} {'*' * frecuencia}")

def cuatrovocales(texto):
    def contar_vocales(palabra):
        return len(set(letra for letra in palabra if letra in "aeiouAEIOU")) >= 4
    
    palabras = texto.split()
    palabras_cuatro_vocales = []
    for palabra in palabras:
        if contar_vocales(palabra):
            palabras_cuatro_vocales.append(palabra)
    
    return len(palabras_cuatro_vocales)

def cesar(texto):
    caracteres_base = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz,.-¿?="
    resultado = ""
    
    for caracter in texto:
        if caracter in caracteres_base:
            indice = (caracteres_base.index(caracter) + 6) % len(caracteres_base)
            resultado += caracteres_base[indice]
        else:
            resultado += caracter
    
    return resultado

def descesar(texto):
    caracteres_base = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz,.-¿?="
    resultado = ""
    
    for caracter in texto:
        if caracter in caracteres_base:
            indice = (caracteres_base.index(caracter) - 6) % len(caracteres_base)
            resultado += caracteres_base[indice]
        else:
            resultado += caracter
    
    return resultado