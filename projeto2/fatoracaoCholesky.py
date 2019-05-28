#####################################################################
########################	Cholesky	 ############################
#####################################################################
import math
import sys

def fatoracaoCholesky(A):
	# Verificar se ela é simétrica?
	n = len(A)
	G = [[0 for i in range(0, n)] for i in range(0, n)]

	for k in range(0, n):
		soma = 0

		for j in range(0, k):
			soma = soma + math.pow(G[k][j], 2)

		try:
			G[k][k] = math.sqrt(A[k][k] - soma)
		except:
			print("\n\nERRO: A matriz não é definida positiva\nEncerrando programa")
			sys.exit()

		for i in range(k, n):
			soma = 0

			for j in range(0, k):
				soma = soma + G[i][j] * G[k][j]

			G[i][k] = (A[i][k] - soma) / G[k][k]

	return G

def resolucaoSistemaSuperior(A, B):

	# Inicialização do vetor resolução
	x = [0 for i in range(0, len(A))]

	# Váriavel n irá conter o grau das operações
	n = len(A) - 1

	# Resolução da linha n
	x[n] = B[n] / A[n][n]

	# Resolução das demais linhas
	for i in range(n - 1, -1, -1):
		soma = 0

		# Primeiro substituimos todas os valores de x já conhecidos e somamos eles.
		for j in range(i + 1, n + 1):
			soma = soma + A[i][j] * x[j]

		# Para então isolarmos o resultado de x e obtermos seu resultado
		x[i] = (B[i] - soma) / A[i][i]

	return x

def resolucaoSistemaInferior(A, B):

	# Inicialização do vetor resolução
	x = [0 for i in range(0, len(A))]

	# Váriavel n irá conter o grau das operações
	n = len(A) - 1

	# Resolução da linha 0
	x[0] = B[0] / A[0][0]

	# Resolução das demais linhas
	for i in range(1, n + 1):
		soma = 0

		# Primeiro substituimos todas os valores de x já conhecidos e somamos eles.
		for j in range(i - 1, -1, -1):
			soma = soma + A[i][j] * x[j]

		# Para então isolarmos o resultado de xi e obtermos seu resultado
		x[i] = (B[i] - soma) / A[i][i]

	return x

# Função retirada de https://www.geeksforgeeks.org/transpose-matrix-single-line-python/x
# Transpõe a matriz A
def transposta(A):
	T = [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
	return T

def pprint(x):
	i = 1

	if type(x[0]) == list:
		for prt in x:
			print(prt)
	
	else:
		for prt in x:
			print("x{} = {:.10f}" .format(i, prt))
			i = i+1

	print()

#####################################################################
############################	MAIN	#############################
#####################################################################
A = []
B = []

grau = (int)(input("Digite o grau do sistema: "))
print("Digite os valores da matriz A:")

for i in range(0, grau):
	new = []
	print("Valores da linha {}: " .format(i+1))

	for j in range(0, grau):
		new.append((int)(input("Valor {} {}: " .format(i+1, j+1))))

	A.append(new)

print("Digite os valores do vetor resolução (B):")

for i in range(0, grau):
	B.append(int(input("Valor {} do vetor: " .format(i+1))))

print()

# Acha a matriz G a partir da fatoração de Cholesky
G = fatoracaoCholesky(A)
print("\nFator de Cholesky: ")
pprint(G)

# Resolve o sistema Gy = b
Y = resolucaoSistemaInferior(G, B)

# Resolve o sistema G^Tx = y
x = resolucaoSistemaSuperior(transposta(G), Y)

print("Resolução do sistema:")
pprint(x)