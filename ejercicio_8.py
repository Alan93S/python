import numpy
radio = float(input("ingrese radio: "))
gen = float(input("ingrese generatris: "))
alt = float(input("ingrese altura: "))

area_base = numpy.pi * pow(radio, 2)
area_lateral = numpy.pi * radio * gen
area_total = area_base + area_lateral
volumen = (1/3)*area_base*alt

print(area_base)
print(area_lateral)
print(area_total)
print(volumen)
