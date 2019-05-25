####################################################################
####################	Método do Ponto Fixo	####################
####################################################################
import math

def f(x):
	return math.pow(math.e, x) - 4*math.pow(x, 2)

# Função de iteração
def g(x):
	return math.pow(x+1, 1/3)

def modulo(x):
	if x < 0:
		return (-1) * x
	else:
		return x

def metodoPontoFixo(e1, e2, x0):
	x1 = x0
	k = 1

	if modulo(f(x0)) < e1:
		return x0, 0
	else:
		x1 = g(x0)
		print("Iteração {:02d}: |x1| = {:.10f}, |x1 - x0| = {:.10f}" .format(k, modulo(x1), modulo(x1-x0)))

	while (modulo(f(x1)) > e1) and (modulo(x1 - x0) > e2):
		x0 = x1
		x1 = g(x0)
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

raizAproximada, iteracoes = metodoPontoFixo(e1, e2, x0)
print('\nA média aproximada é {}, e foram necessárias {} iterações' .format(raizAproximada, iteracoes))