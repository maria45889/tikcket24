def encontrarMayor(val1: int, val2: int, val3: int) -> int:
    mayorAc = val1
    if val2 > mayorAc:
        mayorAc = val2
    if val3 > mayorAc:
        mayorAc = val3
    return mayorAc
resultado = encontrarMayor(10, 20, 15)
print(resultado)