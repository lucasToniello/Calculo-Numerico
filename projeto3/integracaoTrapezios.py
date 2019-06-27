import math

# Obs: é necessário escolher a função que se deseja integrar aqui
def f(x):
	return math.pow(math.e, x) * math.sin(x)
	# return math.pow(math.e, -math.pow(x, 2))

def integracaoTrapezios(a, b, numIntervalos):

	h = (b - a) / numIntervalos
	soma = f(a)

	for i in range(1, numIntervalos):
		soma += 2*f(a+(h*i))

	return (h/2) * (soma + f(b))

#####################################################################
############################	MAIN	#############################
#####################################################################

a = float(input("Valor inferior da integral: "))
b = float(input("Valor superior da integral: "))
numIntervalos = int(input("Digite o número de intervalos: "))

print("O valor da integral é: {}\n " .format(integracaoTrapezios(a, b, numIntervalos)))