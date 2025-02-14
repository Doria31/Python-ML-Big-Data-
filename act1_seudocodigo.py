#1. Se desea calcular la distancia recorrida (D) por un automóvil que tiene velocidad constante
# (m/s) durante un tiempo T (Sg), considerar que es un MRU (Movimiento Rectilíneo
# Uniforme). Tenga en cuenta que la formula del movimiento rectilíneo es:

# D = V * T

# velocidad = int(input("Ingresa la velocidad: "))
# tiempo = int(input("Ingresa el tiempo: "))

# distancia = velocidad * tiempo

# print(f"La distacia es igual a: {distancia}")

#2. Se necesita obtener el promedio de un estudiante a partir de sus tres notas parciales. El
# estudiante debe digitar sus tres notas y el sistema deberá darle el promedio del semestre.

# nota1 = float(input("Ingresa la nota #1: "))
# nota2 = float(input("Ingresa la nota #2: "))
# nota3 = float(input("Ingresa la nota #3: "))

# sumaNotas = nota1 + nota2 + nota3

# promedio = sumaNotas/3

# print(f"El promedio del estudiante es {promedio}")

# 3. Elaborar un algoritmo que permita ingresar el número de partidos ganados, perdidos y
# empatados, de un equipo en un torneo de futbol. Se debe de imprimir el puntaje total del
# equipo, tenga en cuenta que:
# a. Por cada partido ganado obtendrá 3 puntos.
# b. Por cada partido empatado 1 punto.
# c. Por cada partido perdido 0 puntos.
# Se desea imprimir la cantidad de partidos ganados, perdidos, empatados y el cálculo
# completo de la cantidad de puntos obtenidos del equipo de futbol.

# nombreEquipo = input("Ingre el nombre del equipo: ")
# partidosGanados = int(input("Ingrese el número de partidos ganados: "))
# partidosPerdidos = int(input("Ingrese el número de partidos perdidos: "))
# partidosEmpatados = int(input("Ingrese el número de partidos empatados: "))

# calPganados = partidosGanados*3
# calPempatado = partidosEmpatados*1
# puntosObtenidos = calPganados + calPempatado

# print("--------------------------Resultados-----------------------------------------")

# print(f"Los partidos ganados fueron: {partidosGanados}")
# print(f"Los partidos perdidos fueron: {partidosPerdidos}")
# print(f"Los partidos empatados fueron: {partidosEmpatados}")

# print(f"El puntaje obtenido del Equipo {nombreEquipo} de futbol fue: {puntosObtenidos}")

#4. Se requiere el algoritmo para elaborar la planilla de un empleado. Para ello se debe digitar:
# nombre del empleado, la cantidad de horas laboradas en el mes y la tarifa por hora. Se debe
# calcular el total devengado por el empleado en el mes e imprimir: Nombre del empleado,
# cantidad de horas laboradas y total devengado.

# nombreEmpleado = input("Ingre tu nombre:")
# horasLaboradas = int(input("Ingresa tus horas laboradas: "))
# tarifaHora = int(input("Ingresa la tarifa por hora: "))
# pension = 30000

# totalDevengado = tarifaHora * horasLaboradas
# salario = totalDevengado - pension

# print("---------------------- Colilla de Pago ----------------------------")

# print(f"Nombre del Empleado: {nombreEmpleado}")

# print("---------------------- DETALLES ----------------------------")
# print("---------------------- Devengado ----------------------------")
# print(f"Total horas laboradas: {horasLaboradas}")
# print(f"Total devengado: {totalDevengado}")

# print("---------------------- Deducciones ----------------------------")

# print(f"Descuento pensión: {pension}")

# print("---------------------- Total a pagar ----------------------------")

# print(f"Neto a pagar: {salario}")

# 5. Se tiene un triángulo rectángulo cuyos lados deberán ser digitados por el usuario. Se debe
# hallar la hipotenusa teniendo en cuenta la formula: H = raíz cuadrada (a**2 + b**2)

# import math

# a = int(input("Ingrese el cateto A: "))
# b = int(input("Ingrese el cateto B: "))

# hipotenusa = math.sqrt(a**2 + b**2)

# print(f"La hipotenusa es: {hipotenusa}")


# 6. Se tiene un horno en casa con temperaturas en grados Celsius centígrado), requiere
# transformar la temperatura de 70°C a grados Fahrenheit. Para ello tenga en cuenta la
# siguiente fórmula:
# F = (C * 1.8) + 32

# centigrados = int(input("Ingresa la temperatura en C:")) 

# fahrenheit = (centigrados * 1.8) + 32  

# print(f"{centigrados}°C son {fahrenheit}°F")  







