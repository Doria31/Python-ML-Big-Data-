# 1. Desarrolle un algoritmo que lea un número, en caso de ser negativo lo
# imprima junto con su positivo.

# try:
#     numero = int(input("Introduce un número: "))
    
#     if numero < 0:
#         print(f"El número es negativo: {numero} y su valor positivo es: {abs(numero)}")
#     elif numero == 0:
#         print("El número ingresado es 0 o neutral")
#     else:
#         print(f"El número es positivo: {numero}").

# except ValueError:
#     print("¡Error! Por favor, ingresa un número entero positivo o negativo.")


# 2. desarrollar un programa que, dado una calificación de un alumno en un
# parcial, escribe aprobado si la calificación es superior a 3.

# try:
#     calificacion = float(input("Ingresa su calificación: "))
    
#     if calificacion >= 3:
#         print("¡Aprobado!")
#         print("----------------------------")
#         print("Escala de calificación:")
#         print("Superior a 3 Aprobado")
#         print("Inferior a 3 No aprobado")
    
#     else:
#         print("No aprobado")
#         print("----------------------------")
#         print("Escala de calificación:")
#         print("Superior a 3 Aprobado")
#         print("Inferior a 3 No aprobado")

# except ValueError:
#     print("¡Error! Por favor, ingresa una calificación válida.")


# 3.Desarrollar el algoritmo dado como dato el sueldo de un trabajador, le aplica
# un aumento del 15% si su sueldo es inferior a $300.000.

# try:
#     sueldo = int(input("Ingrese su sueldo: "))

#     if sueldo < 300000:
#         nuevoSueldo = sueldo * 1.15
#         print("¡Felicidades! Has obtenido un aumento en tu sueldo del 15%: ")
#         print(f"Sueldo anterior: {sueldo}")
#         print(f"Nuevo sueldo: {nuevoSueldo}")
#     else:
#         print("¡Lo siento! En el momento no tenemos beneficios para ti...")

# except ValueError:
#     print("¡Error! Por favor, ingresa un valor numérico válido para tu sueldo.")

# 4. desarrollar un algoritmo que asigne el sueldo a cinco empleados, teniendo
# en cuenta su categoría.

# print("¿Qué categoría tienes en la empresa?")
# print("------------------------------------")
# print("1. Desarrollador Junior")
# print("2. Desarrollador Semi-Senior")
# print("3. Desarrollador Senior")
# print("4. Líder Técnico")
# print("5. QA Tester")

# try:
#     opcion = int(input("Ingresa el número de la categoría: "))

#     if opcion == 1:
#         sueldo = 2500000
#         categoria = "Desarrollador Junior"
#     elif opcion == 2:
#         sueldo = 4500000
#         categoria = "Desarrollador Semi-Senior"
#     elif opcion == 3:
#         sueldo = 8000000
#         categoria = "Desarrollador Senior"
#     elif opcion == 4:
#         sueldo = 12000000
#         categoria = "Líder Técnico"
#     elif opcion == 5:
#         sueldo = 3500000
#         categoria = "QA Tester"
#     else:
#         print("¡Opción del menú no valida!")

#     print(f"Tu sueldo como {categoria} es: ${sueldo}")

# except ValueError:
#     print("¡Error! Por favor, ingresa un número válido para la categoría.")



# 5. Desarrollar un programa que capture tres números e imprima por pantalla
# cual es el número mayor, el menor, cuales son iguales, si los tres
# diferentes.

# try:
#     numero1 = float(input("Introduce el primer número: "))
#     numero2 = float(input("Introduce el segundo número: "))
#     numero3 = float(input("Introduce el tercer número: "))

#     mayor = max(numero1, numero2, numero3)
#     menor = min(numero1, numero2, numero3)

#     print(f"El número mayor es: {mayor}")
#     print(f"El número menor es: {menor}")

#     if numero1 == numero2 == numero3:
#         print("Los tres números son iguales.")
#     elif numero1 == numero2 or numero1 == numero3 or numero2 == numero3:
#         print("Hay al menos dos números iguales.")
#     else:
#         print("Los tres números son diferentes.")

# except ValueError:
#     print("¡Error! Por favor, ingresa un número válido.")


# 6. Escriba el algoritmo que al capturar un numero entero convierta grados
# centígrados a kelvin, si captura un numero flotante diga si es mayor a 10.5,
# y si captura un carácter escriba su nombre.

# Capturar la entrada del usuario
# entrada = input("Introduce un número o un carácter: ")

# # Verificar si es un número entero
# if entrada.isdigit() or (entrada[0] == '-' and entrada[1:].isdigit()):
#     numero = int(entrada)
#     # Convertir grados Celsius a Kelvin
#     kelvin = numero + 273.15
#     print(f"{numero} grados Celsius son {kelvin} Kelvin.")
    
# # Verificar si es un número flotante
# elif entrada.replace('.', '', 1).isdigit() and entrada.count('.') < 2:
#     numero_flotante = float(entrada)
#     if numero_flotante > 10.5:
#         print(f"{numero_flotante} es mayor a 10.5")
#     else:
#         print(f"{numero_flotante} no es mayor a 10.5")

# # Si no es un número, asumir que es un carácter
# else:
#     print(f"Has introducido el carácter: {entrada}")

#7. Desarrolle un algoritmo que lea de un registro: el nombre, la edad, el sexo,
# el estado civil de cualquier persona e imprima el nombre de la persona, si
# corresponde a un hombre casado mayor de 40 años o a una mujer soltera
# menor de 50 años.

# try:
#     nombre = input("Introduce el nombre: ")
#     if not nombre.isalpha():
#         raise ValueError("El nombre solo debe contener letras.")
    
#     edad = input("Introduce la edad: ")
#     if not edad.isdigit() or int(edad) <= 0:
#         raise ValueError("La edad debe ser un número entero positivo.")
#     edad = int(edad)
    
#     sexo = input("Introduce el sexo (masculino/femenino): ").lower()
#     if sexo not in ["masculino", "femenino"]:
#         raise ValueError("El sexo debe ser 'masculino' o 'femenino'.")
    
#     estadoCivil = input("Introduce el estado civil (casado/soltero): ").lower()
#     if estadoCivil not in ["casado", "soltero"]:
#         raise ValueError("El estado civil debe ser 'casado' o 'soltero'.")
    
#     if (sexo == "masculino" and estadoCivil == "casado" and edad > 40) or (sexo == "femenino" and estadoCivil == "soltero" and edad < 50):
#         print(f"Nombre: {nombre}")

# except ValueError as e:
#     print(f"¡Error! {e}")

    
# 8. Prepare un algoritmo que identifique e imprima el número medio de un
# conjunto de tres números únicos. El número medio es aquel que no es el
# menor ni el mayor.

# try:
#     numero1 = input("Introduce el primer número: ")
#     if not numero1.isdigit():
#         raise ValueError("El primer número debe ser un valor numérico entero.")
#     numero1 = int(numero1)

#     numero2 = input("Introduce el segundo número: ")
#     if not numero2.isdigit():
#         raise ValueError("El segundo número debe ser un valor numérico entero.")
#     numero2 = int(numero2)

#     numero3 = input("Introduce el tercer número: ")
#     if not numero3.isdigit():
#         raise ValueError("El tercer número debe ser un valor numérico entero.")
#     numero3 = int(numero3)

#     # Calcular el número medio
#     if (numero1 > numero2 and numero1 < numero3) or (numero1 < numero2 and numero1 > numero3):
#         medio = numero1
#     elif (numero2 > numero1 and numero2 < numero3) or (numero2 < numero1 and numero2 > numero3):
#         medio = numero2
#     else:
#         medio = numero3

#     # Imprimir el número medio
#     print(f"El número medio es: {medio}")

# except ValueError as e:
#     print(f"¡Error! {e}")

# 9.Dados tres números enteros únicos, a, b y c. Elabore un algoritmo que los
# ordene de mayor a menor e imprímalos.

# try:
#     a = input("Introduce el primer número: ")
#     if not a.isdigit():
#         raise ValueError("El primer número debe ser un valor numérico entero.")
#     a = int(a)

#     b = input("Introduce el segundo número: ")
#     if not b.isdigit():
#         raise ValueError("El segundo número debe ser un valor numérico entero.")
#     b = int(b)

#     c = input("Introduce el tercer número: ")
#     if not c.isdigit():
#         raise ValueError("El tercer número debe ser un valor numérico entero.")
#     c = int(c)

#     # Crear la lista de números y ordenarlos de mayor a menor
#     numeros = [a, b, c]
#     numeros.sort(reverse=True)

#     # Imprimir los números ordenados
#     print(f"Los números ordenados de mayor a menor son: {numeros}")

# except ValueError as e:
#     print(f"¡Error! {e}")


# 10.A ciertos estudiantes se les dice que su calificación final será el promedio
# de las dos calificaciones más altas de entre las tres que se han obtenido en
# el curso. Haga un algoritmo que permita a un estudiante efectuar el cálculo
# correspondiente a su nota final.

# try:
#     calificacion1 = float(input("Introduce la primera calificación: "))
#     calificacion2 = float(input("Introduce la segunda calificación: "))
#     calificacion3 = float(input("Introduce la tercera calificación: "))

#     # Ordenar las calificaciones de mayor a menor
#     calificaciones = [calificacion1, calificacion2, calificacion3]
#     calificaciones.sort(reverse=True)

#     # Calcular el promedio de las dos calificaciones más altas
#     notaFinal = (calificaciones[0] + calificaciones[1]) / 2

#     # Imprimir la nota final
#     print(f"La nota final del estudiante es: {notaFinal}")

# except ValueError:
#     print("¡Error! Por favor, ingresa un número válido.")


# 11.Escriba un algoritmo que acepte o rechace una pieza en forma de varilla,
# para una empresa de acuerdo a los siguientes criterios:
# a. Su longitud debe ser mayor de 7.5 cm pero no exceder los 9 cm
# b. Su diámetro no debe ser menor que 0.5 cm ni mayor de 1.3 cm.
# c. Por ningún motivo su masa debe exceder los 5.8 cm
# i. Nota: masa = diámetro * longitud / densidad; densidad = 3.5 Gr/cm 

# try:
#     longitud = float(input("Introduce la longitud de la varilla: "))
#     diametro = float(input("Introduce el diámetro de la varilla: "))

#     masa = (diametro * longitud) / 3.5  # g/cm³

#     if 7.5 < longitud <= 9 and 0.5 <= diametro <= 1.3 and masa <= 5.8:
#         print("La pieza es aceptada.")
#         print(f"La masa de la varilla es: {masa}")
#     else:
#         print("La pieza es rechazada.")
    
# except ValueError:
#     print("¡Error! Por favor, ingresa un número válido.")


# 12.Un vendedor desea calcular su comisión total sobre las ventas de varios
# artículos. Al vendedor le corresponde el 3% de comisión sobre artículos
# cuyo precio es menor de $2.000.oo y el 5% de comisión sobre artículos
# cuyo precio es de $2000.oo o más. El vendedor hizo 50 ventas y desea
# saber también cuántas ventas hizo menores de 2000 y cuantas mayores o
# iguales a 2000.

# comisionTotal = 0
# ventasMenores = 0
# ventasMayorIgual = 0

# for i in range(3):
#     while True:
#         try:
#             precio = float(input(f"Introduce el precio de la venta {i + 1}: $"))
#             if precio <= 0:
#                 print("El precio debe ser un número positivo. Inténtalo de nuevo.")
#                 continue
#             break  # Si el precio es válido, salimos del bucle
#         except ValueError:
#             print("¡Error! Por favor, ingresa un número válido.")
    
#     if precio < 2000:
#         comisionTotal += precio * 0.03  
#         ventasMenores += 1
#     else:
#         comisionTotal += precio * 0.05 
#         ventasMayorIgual += 1

# print(f"Comisión total: ${comisionTotal}")
# print(f"Ventas menores de $2,000: {ventasMenores}")
# print(f"Ventas mayores o iguales a $2,000: {ventasMayorIgual}")


#13.desarrollar un algoritmo que halle la nota total de una materia en el SENA, y
# determine si la gano o la reprobó
# competencia = input("Ingresa la competencia a evaluar: ")

# try:
#     evidencia1 = float(input("Ingresa la nota de la Evidencia #1: "))
#     evidencia2 = float(input("Ingresa la nota de la Evidencia #2: "))
#     evidencia3 = float(input("Ingresa la nota de la Evidencia #3: "))
#     examenfinal = float(input("Ingresa la nota del Examen final: "))
#     proyectofinal = float(input("Ingresa la nota del Proyecto Final: "))

#     sumanotas = evidencia1 + evidencia2 + evidencia3 + examenfinal + proyectofinal

#     notatotal = sumanotas/5

#     if notatotal >= 3.2:
#         print(f"El resultado de la competencia de {competencia} fue ¡Aprobado! ")
#     else:
#         print(f"El resultado de la competencia de {competencia} fue ¡No Aprobado! ")

# except ValueError:
#     print("¡Error! Por favor, ingresa un número válido.")

    

# 14. Desarrollar un algoritmo que evalué la siguiente expresión aritmética 1/n.

# # Solicitar al usuario el valor de n
# try:
#     n = float(input("Introduce el valor de n: "))

#     # Validar que n no sea cero
#     if n != 0:
#         resultado = 1 / n
#         print(f"El resultado de la expresión 1/n es: {resultado}")
#     else:
#         print("¡No se puede dividir por cero!")

# except ValueError:
#     print("¡Error! Por favor, ingresa un número válido.")


# 15. desarrollar el algoritmo que evalué la formula cuadrática o general.

# import math

# try:
#     # Solicitar los coeficientes a, b, c
#     a = float(input("Introduce el valor de a: "))
#     b = float(input("Introduce el valor de b: "))
#     c = float(input("Introduce el valor de c: "))

#     # Calcular el discriminante (b^2 - 4ac)
#     discriminante = b**2 - 4*a*c

#     # Verificar el discriminante
#     if discriminante > 0:
#         # Dos soluciones reales y distintas
#         x1 = (-b + math.sqrt(discriminante)) / (2 * a)
#         x2 = (-b - math.sqrt(discriminante)) / (2 * a)
#         print(f"Las soluciones son x1 = {x1} y x2 = {x2}")
#     elif discriminante == 0:
#         # Una solución real
#         x = -b / (2 * a)
#         print(f"La solución es x = {x}")
#     else:
#         # No hay soluciones reales
#         print("No hay soluciones reales (las soluciones son complejas).")

# except ValueError:
#     print("¡Error! Por favor, ingresa un número válido.")
# except ZeroDivisionError:
#     print("¡Error! El valor de a no puede ser cero.")


# 16.desarrollar un algoritmo que capture un número y diga si es par o impar.

# try:
#     numero = int(input("Introduce un número: "))

#     # Se verifica si el número es divisible y el residuo es 0
#     if numero % 2 == 0:
#         print(f"El número {numero} es par.")
#     else:
#         print(f"El número {numero} es impar.")

# except ValueError:
#     print("¡Error! Por favor, ingresa un número entero válido.")


# 17.desarrollar el algoritmo que lea tres números y diga si uno es divisible del otro.

#Capturar los tres números
try:
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))
    num3 = int(input("Introduce el tercer número: "))

    # Verificar si alguno es divisible por otro
    if num1 % num2 == 0:
        print(f"{num1} es divisible por {num2}")
    elif num2 % num3 == 0:
        print(f"{num2} es divisible por {num3}")
    elif num1 % num3 == 0:
        print(f"{num1} es divisible por {num3}")
    else:
        print("Ningún número es divisible por otro.")

except ValueError:
    print("¡Error! Por favor, ingresa números enteros válidos.")


# 18.Desarrollar un algoritmo que capture un número y diga si negativo o positivo.

try:
    numero = float(input("Introduce un número: "))

    if numero > 0:
        print(f"El número {numero} es positivo.")
    elif numero < 0:
        print(f"El número {numero} es negativo.")
    else:
        print("El número es cero.")

except ValueError:
    print("¡Error! Por favor, ingresa un número válido.")




    










    
