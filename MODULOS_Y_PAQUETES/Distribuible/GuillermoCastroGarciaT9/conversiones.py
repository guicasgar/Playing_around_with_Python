def hexa(decimal):
    if decimal < 0:
        return "El número debe ser positivo."
    hex_chars = "0123456789ABCDEF"
    result = ""
    while decimal > 0:
        decimal, resto = divmod(decimal, 16)
        result = hex_chars[resto] + result
    return result or "0"

def octal(decimal):
    if decimal < 0:
        return "El número debe ser positivo."
    result = ""
    while decimal > 0:
        decimal, resto = divmod(decimal, 8)
        result = str(resto) + result
    return result or "0"

def romano(decimal):
    if decimal < 1 or decimal > 3999:
        return "El número debe estar en el rango de 1 a 3999."
    valores = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romanos = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    result = ""
    for valor, romano in zip(valores, romanos):
        while decimal >= valor:
            result += romano
            decimal -= valor
    return result

def romtodec(romano):
    romano_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    decimal = 0
    prev_value = 0
    for numeral in reversed(romano):
        value = romano_numerals[numeral]
        if value < prev_value:
            decimal -= value
        else:
            decimal += value
        prev_value = value
    return decimal