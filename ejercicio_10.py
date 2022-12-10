x1 = float(input("ingresa coor en x punto 1: "))
y1 = float(input("ingresa coor en x punto 1: "))
x2 = float(input("ingresa coor en x punto 2: "))
y2 = float(input("ingresa coor en x punto 2: "))
x3 = float(input("ingresa coor en x punto 3: "))
y3 = float(input("ingresa coor en x punto 3: "))

a_triangulo = 1/2 * abs(x1 * (y2 - y3)+x2 * (y3 - y1) + x3 * (y1 - y2))

print(a_triangulo)
