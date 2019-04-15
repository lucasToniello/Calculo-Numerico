####################################################################
################	Método de newton-raphson	####################
####################################################################
import math

def f(x):
	return math.pow(x, 3) - x - 1

def df(x):
	return 3*math.pow(x, 2) - 1

def modulo(x):
	if x < 0:
		return (-1) * x
	else:
		return x

# Número de iterações está errado
def metodoNewtonRaphson(e1, e2, x0):
	x1 = x0
	k = 1

	if modulo(f(x0)) < e1:
		return x0, 0
	else:
		x1 = x0 - (f(x0) / df(x0))
		print(x1)

	while (modulo(f(x1)) > e1) and (modulo(x1 - x0) > e2):
		x0 = x1
		x1 = x0 - (f(x0) / df(x0))
		k = k + 1
		print(x1)

	return x1, k

####################################################################
############################	MAIN	############################
####################################################################
print("\nPrecisões iniciais:")
e1 = (float)(input("e1: "))
e2 = (float)(input("e2: "))
x0 = (float)(input("\nAproximação inicial: "))

raizAproximada, iteracoes = metodoNewtonRaphson(e1, e2, x0)
print('\nA média aproximada é {}, e foram necessárias {} iterações' .format(raizAproximada, iteracoes))
