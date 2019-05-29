#####################################################################
####################	Gauss-Jacobi	 ############################
#####################################################################

# Função que calcula o módulo de um valor x
def modulo(x):
	if x < 0:
		return (-1) * x
	else:
		return x

# Cálcula o maior valor de um vetor x em módulo
def maxModulo(x):
	maior = 0

	for i in range(0, len(x)):
		if modulo(x[i]) > maior:
			maior = modulo(x[i])

	return maior

def distanciaAbsoluta(x0, x1):
	n = len(x0)
	d = [0 for i in range(0, n)]

	for i in range(0, n):
		d[i] = x1[i] - x0[i]

	return maxModulo(d)

def distanciaRelativa(x0, x1):
	return distanciaAbsoluta(x0, x1) / maxModulo(x1)

# Realiza uma iteração do método de Gauss-Jacobi
def iteracao(A, B, x0):
	n = len(A)
	x1 = [0 for i in range(0, n)]

	for i in range(0, n):
		# x1 recebe o valor do vetor B na mesma linha
		x1[i] = B[i]

		# Subtraimos todos os valores que não são da diagonal da linha atual, 
		# substituindo o valor de xj pelo seu respectitivo em x0
		for j in range(0, n):
			if i != j:
				x1[i] = x1[i] - (A[i][j] * x0[j])

		# E então achamos o valor de xi isolando ele na equação
		x1[i] = x1[i] / A[i][i] 

	return x1

def gaussJacobi(A, B, x0, e):
	x1 = []
	iteracoes = 0

	# Loop é realizado até que a distância relativa seja menor que a precisão e,
	# também contamos o número de iterações
	while True:
		x1 = iteracao(A, B, x0)
		iteracoes = iteracoes + 1

		if distanciaRelativa(x0, x1) < e:
			return x1, iteracoes
		else:
			x0 = x1

# Função que printa na tela os resultados do sistema
def pprint(x):
	i = 1

	for prt in x:
		print("x{} = {}" .format(i, prt))
		i = i+1

#####################################################################
############################	MAIN	#############################
#####################################################################
A = []
B = []
x0 = []

# Recebemos os valores de entrada do usuário
grau = (int)(input("Digite o grau do sistema: "))
print("Digite os valores da matriz A:")

for i in range(0, grau):
	new = list(map(float, input().split()))
	A.append(new)

print("Digite os valores do vetor constante (B):")
B = list(map(float, input().split()))

print("Digite os valores do vetor x0")
x0 = list(map(float, input().split()))

e = (float)(input("Digite a precisão e: "))

# Resolve o sistema por gaussJacobi, também calculando o número de iterações
x, iteracoes = gaussJacobi(A, B, x0, e)
print("\nResolução do sistema após {} iteracoes:" .format(iteracoes))
pprint(x)