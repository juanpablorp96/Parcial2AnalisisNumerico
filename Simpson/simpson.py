from math import *
def f(x):
  #funcion
  return sqrt(1+(cos(x) * cos(x)))

def simpson(a,b):
  #Regla de simpson
  c=(a+b)/2.0
  h=abs(b-a)/2.0
  return h*(f(a)+4.0*f(c)+f(b))/3.0

# calcula la integral de 0 a 2
print("Respuesta regla Simpson:")
print (simpson(0,2))