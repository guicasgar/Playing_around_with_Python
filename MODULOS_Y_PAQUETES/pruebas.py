from Distribuible.GuillermoCastroGarciaT9.conversiones import hexa, octal, romano, romtodec

numero_decimal = 36
numero_hexadecimal = hexa(numero_decimal)
numero_octal = octal(numero_decimal)
numero_romano = romano(numero_decimal)
numero_romano_a_decimal = romtodec(numero_romano)

print(f"Número decimal: {numero_decimal}")
print(f"Número hexadecimal: {numero_hexadecimal}")
print(f"Número octal: {numero_octal}")
print(f"Número romano: {numero_romano}")
print(f"Número romano a decimal: {numero_romano_a_decimal}")