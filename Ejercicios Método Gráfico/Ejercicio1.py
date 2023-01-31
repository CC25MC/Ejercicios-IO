# Importamos la libreria y con ellos todos los comandos
from pulp import *

# Declaramos el problema de programacion lineal
problem = LpProblem("Problema_De_Programacion_Lineal_Ejericicio_2", LpMinimize)

#Declaramos las variables 
x1=LpVariable("x",lowBound=0)
x2=LpVariable("y",lowBound=0)

# Declaramos la funcion Objetivo, la cual en el problema es Minimizar Z= 2x+3y
# Como mi cedula es 27276551 procedo a sustituir con los valores correspondientes
problem += 5 * x1 + 1 * x2

# Restricciones
problem += -x1 + x2 <= 2
problem += x2 <= 5

problem.solve()

print("El Valor optimo para el problema de minimizar se obtiene con x =", x1.varValue ," y =",x2.varValue)