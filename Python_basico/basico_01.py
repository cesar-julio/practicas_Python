import quantities as qtt
import inspect
import numpy as np

# Ver la información del modulo 
def mostrarModulos(modulo):
    """ Muestra en consola los submodulos de un modulo espesifico."""
    for nombres, datos in inspect.getmembers(modulo, inspect.ismodule):
        print(nombres, "*")
def contenidoPaquetes (paquete):
    for u in dir(paquete):
        print("*", u)


lista_simbolos = []

# Usar el modulo en sí
def fuerza(masa, aceleracion):
    ace = qtt.Quantity(aceleracion, "m/s**2")
    m = masa*qtt.kg
    f = m*ace
    return f

print(fuerza(10,12))