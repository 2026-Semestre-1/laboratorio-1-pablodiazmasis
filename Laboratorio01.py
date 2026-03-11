"""
Nombre: calculadora
Entradas: operacion, op1, op2
Salidas: El resultado de la operación según el número que correponda.
Restricciones: Los números deben ser mayor a cero.
               Los números debe ser un valor entero.
"""
def calculadora(operacion, op1, op2):

    if not(isinstance(op1, int)):
        return "Error: El numero uno debe ser un valor entero"

    if not(isinstance(op2, int)):
        return "Error: El numero dos debe ser un valor entero"

    if(isinstance(operacion, int)):
        if(operacion < 0 or operacion > 4):
            return "Error: La operación debe ser un número entre el 1 al 4 (1 = suma, 2 = resta, 3 = multiplicación, 4 = división entera)"
    else:
        return "Error: El digito debe ser entero"

    if (op1 < 0):
        op1 *= -1
    if (op2 < 0):
        op2 *= -1

    return calculadora_Aux(operacion, op1, op2)

def calculadora_Aux(operacion, op1, op2):
    resultado = 0

    if (operacion == 1):
        resultado = op1 + op2
    elif(operacion == 2):
        resultado = op1 - op2
    elif(operacion == 3):
        resultado = op1 * op2
    elif(operacion == 4):
        if(op2 == 0):
            return "No se puede dividir entre cero"
        else:
            resultado = op1 // op2

    return resultado


"""
Nombre: contadorDigitos
Entradas: num, digito
Salidas: La cantidad de coincidencias de un numero en especifico dentro de un numero.
Restricciones: El numero y digito deben ser un valor entero.
"""
def contadorDigitos(num, digito):
    if not(isinstance(num, int)):
        return "Error: El numero debe ser un valor entero positivo"
    
    if(isinstance(digito, int)):
        if(digito > 10):
            return "Error: El digito debe ser un numero del 1 al 9"
    else:
        return "Error: El digito debe ser entero"

    if(num < 0):
        num *= -1
    if(digito < 0):
        digito *= -1

    if(num == 0):
        return 1
        if(digito == 0):
            return 1
        else:
            return 0
        
    return contadorDigitos_Aux(num, digito)

def contadorDigitos_Aux(num, digito):
    
    i = 0
    while num != 0:
        a = num % 10
        
        if(a == digito):
            i += 1
            
        num //= 10
        
    return i

"""
Nombre: sumatoria_V2
Entradas: inicio, fin, distancia, excepcion
Salidas: La suma desde 0 en forma consecutiva hasta el valor de num
Restricciones: Ambos valores deben ser numerico entero y positivo.
               El valor de inicio deber ser menor o igual a valor de final
Ejemplo:
    sumatoria_V2(3,5)
    Descendente 5 + 4 + 3 = 12
"""
def sumatoria_V2(inicio, fin, distancia, excepcion):
    if(isinstance(inicio, int)):
        if(inicio < 0):
            return "Error: El inicio debe ser mayor a cero"
    else:
        return "Error: El inicio debe ser entero"

    if(isinstance(fin, int)):
        if(fin < 0):
            return "Error: El fin debe ser mayor a cero"
    else:
        return "Error: El fin debe ser entero"

    if(isinstance(distancia, int)):
        if(distancia > 10):
            return "Error: El parámetro distancia debe estar en 1 a 9"
    else:
        return "Error: El parametro distancia debe ser entero"
    
    if not isinstance(excepcion, int):
        return "Error: el parametro excepcion debe ser entero"

    if(distancia < 0 and fin >= inicio):
        return "Error: el parámetro inicio debe ser mayor o igual a fin"

    if(distancia > 0 and fin <= inicio):
        return "Error: el parámetro inicio debe ser menor o igual a fin"

    return sumatoria_V2_Aux(inicio, fin, distancia, excepcion)

def sumatoria_V2_Aux(inicio, fin, distancia, excepcion):
    resultado = 0
    i = inicio

    while (distancia > 0 and i <= fin) or (distancia < 0 and i >= fin):
        if(excepcion == 0) or (i % excepcion != 0):
            resultado += i

        i += distancia

    return resultado











