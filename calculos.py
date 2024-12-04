def valorMayor(valor1: int, valor2: int, valor3: int) -> int:
    mayorActual = valor1
    if valor2 > mayorActual:
        mayorActual = valor2
    if valor3 > mayorActual:
        mayorActual = valor3
    return mayorActual
resultado = valorMayor(10, 20, 15)
print(resultado)

def determinarResultadosIMC(resultado):
    if resultado >= 0 and resultado <16:
        return "Delgadez severa"
    elif resultado >= 16 and resultado <17:
        return "Delgadez moderada"
    elif resultado >= 17 and resultado <18.5:
        return "Delgadez leve"
    elif resultado >= 18.5 and resultado<25:
        return "Peso normal"
    elif resultado >= 25 and resultado <30:
        return "Sobrepeso"
    elif resultado >= 30 and resultado <35:
        return "Obesidad grado 1"
    elif resultado >= 35 and resultado <40:
        return "Obesidad grado 2"
    elif resultado >= 40:
        return "Obesidad grado 3"
    else:
        return "IMC fuera de rango"
        
def calcularCuota(monto,interesAnual,numeroMeses):
    interesMensual=(interesAnual/12)/100
    coutaMensual=(monto*interesMensual)/(1-(1+interesMensual)**(-numeroMeses))
    return coutaMensual


def calcularEdad(año_nacimiento):
  
    import datetime
    año_actual = datetime.datetime.now().year
    
    if año_nacimiento <= 0:
        return -1  

    if año_nacimiento > año_actual:
        return -1

    edad = año_actual - año_nacimiento
    
    return edad

