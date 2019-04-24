####################################################################
################	Método de newton-raphson	####################
####################################################################
import math

def f(x):
	# return math.pow(x, 3) - 9*x + 3
	# return math.pow(x, 3) - x + 1
	return 4*math.sin(x) - math.pow(math.e, x)

def df(x):
	# return 3*math.pow(x, 2) - 9
	# return 3*math.pow(x, 2) - 1
	return 4*math.cos(x) - math.pow(math.e, x)

def modulo(x):
	if x < 0:
		return (-1) * x
	else:
		return x

def metodoNewtonRaphson(e1, e2, x0):
	x1 = x0
	k = 1

	if modulo(f(x0)) < e1:
		return x0, 0
	else:
		x1 = x0 - (f(x0) / df(x0))
		print("Iteração {:02d}: |x1| = {:.10f}, |x1 - x0| = {:.10f}" .format(k, modulo(x1), modulo(x1-x0)))

	while (modulo(f(x1)) > e1) and (modulo(x1 - x0) > e2):
		x0 = x1
		x1 = x0 - (f(x0) / df(x0))
		k = k + 1
		print("Iteração {:02d}: |x1| = {:.10f}, |x1 - x0| = {:.10f}" .format(k, modulo(x1), modulo(x1-x0)))

	return x1, k

####################################################################
############################	MAIN	############################
####################################################################
print("\nPrecisões iniciais:")
e1 = (float)(input("e1: "))
e2 = (float)(input("e2: "))
x0 = (float)(input("Aproximação inicial: "))
print()

raizAproximada, iteracoes = metodoNewtonRaphson(e1, e2, x0)
print('\nA média aproximada é {}, e foram necessárias {} iterações' .format(raizAproximada, iteracoes))