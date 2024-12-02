def valorMayor(valor1: int, valor2: int, valor3: int) -> int:
    mayorActual = valor1
    if valor2 > mayorActual:
        mayorActual = valor2
    if valor3 > mayorActual:
        mayorActual = valor3
    return mayorActual
resultado = valorMayor(10, 20, 15)
print(resultado)
