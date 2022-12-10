dis = float(input("ingresa distancia recorrida en metros: "))
minutos = float(input("ingresa minutos: "))
seg = int(input("Ingresa segundos:"))
cen = int(input("Ingresa centésimas:"))

tse = (minutos * 60) + seg + (cen / 100)
vms = dis / tse
vkh = (vms*3600)/1000

print("la velocidad en KMH es de:", vkh)
