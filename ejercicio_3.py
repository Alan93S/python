import numpy
radio = float(input("Ingrese radio de circulo: "))
area = numpy.pi * pow(radio, 2)
long = 2 * numpy.pi * radio

print("El área es: ", area)
print("La longitud es: ", long)
