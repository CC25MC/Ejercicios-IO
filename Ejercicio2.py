# Importamos la libreria y con ellos todos los comandos
from pulp import *

# Declaramos el problema de programacion lineal
problem = LpProblem("Problema_De_Programacion_Lineal_Ejericicio_2", LpMaximize)

#Declaramos las variables 
x1=LpVariable("x",lowBound=0)
x2=LpVariable("y",lowBound=0)

# Declaramos la funcion Objetivo, la cual en el problema es Maximizar Z= x + 1.5y
# Como mi cedula es 27276551 procedo a sustituir con los valores correspondientes
problem += 5 * x1 + 1 * x2

# Restricciones
problem += 2 * x1 + 2 * x2 <= 16
problem += x1 + 2 * x2 <= 12
problem += 4 *x1 + 2 * x2 <= 28

problem.solve()

print("El Valor optimo para el problema de Maximizar se obtiene con x =", x1.varValue ," y =",x2.varValue,  "sustituyendo en la funcion objetivo Z= 5x+1y =", 5 * x1.varValue + 1 * x2.varValue)