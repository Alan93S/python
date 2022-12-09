valor = float(input("Ingrese valor del articulo: "))
paga = float(input("Ingrese cantidad de dinero con la que paga:"))
vuelto = paga - valor
dif = valor - paga
if valor < paga:
    print("tu vuelto es ", vuelto)

elif valor == paga:
    print("No tiene vuelto")

elif valor > paga:
    print("la diferencia es:", dif)
