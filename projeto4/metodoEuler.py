import math

def p1(x, y):
	return float((2*x) - (x*y))

def p2(x, y):
	return float((-y) + (x*y))

def resolucaoSistema(x0, y0, t, numIntervalos):
	h = (t[1] - t[0]) / numIntervalos

	for i in range(0, numIntervalos):
		x1 = x0 + (h*p1(x0, y0))
		y1 = y0 + (h*p2(x0, y0))

		x0 = x1
		y0 = y1

		print("Iteração {}: p1 = {:.10f}, p2 = {:.10f}" .format(i, x1, y1))

	return x0, y0

#####################################################################
############################	MAIN	#############################
#####################################################################

numIntervalos = (int)(input("Número de intervalos: "))

t = [0, 10]
x0 = 1
y0 = 0.1

p1, p2 = resolucaoSistema(x0, y0, t, numIntervalos)
print("Solução com {} subintervalos: P1(t) = {:.10f}, P2(t) = {:.10f}\n" .format(numIntervalos, p1, p2))