####################################################################
######################	Método da bissecção	########################
####################################################################
import math

def f(x):
	return math.pow(x, 3) - x - 1

def bisseccao(a, b):
	return (a + b) / 2

def metodoBisseccao(a, b, e):
	M = f(a)
	x = 0.0
	k = 0

	while (b - a) > e:
		x = bisseccao(a, b)

		if (M * f(x)) > 0:
			a = x
		else:
			b = x

		k = k + 1
		print("Iteração {:02d}: x = {:.10f}, b - a = {:.10f}" .format(k, x, b-a))

	return bisseccao(a, b), k

####################################################################
############################	MAIN	############################
####################################################################
print("\nIntervalo inicial:")
a = (float)(input("a: "))
b = (float)(input("b: "))
e = (float)(input("Precisão e: "))

raizAproximada, iteracoes = metodoBisseccao(a, b, e)
print('\nA média aproximada é {}, e foram necessárias {} iterações' .format(raizAproximada, iteracoes))