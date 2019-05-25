#####################################################################
########################	Cholesky	 ############################
#####################################################################
import math

def fatoracaoCholesky(A):
	# Verificar se ela é simétrica?
	n = len(A)
	G = [[0 for i in range(0, n)] for i in range(0, n)]

	for k in range(0, n):
		soma = 0

		for j in range(0, k):
			soma = soma + math.pow(G[k][j], 2)

		G[k][k] = math.sqrt(A[k][k] - soma)

		for i in range(k, n):
			soma = 0

			for j in range(0, k):
				soma = soma + G[i][j] * G[k][j]

			G[i][k] = (A[i][k] - soma) / G[k][k]

	return G

def resolucaoSistema(A, B):

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
		for j in range(i + 1, n):
			soma = soma + A[i][j] * x[j]

		# Para então isolarmos o resultado de x e obtermos seu resultado
		x[i] = (B[i] - soma) / A[i][i]

	return x

#####################################################################
############################	MAIN	#############################
#####################################################################

A = [[4, 2, 1, 0],
	 [2, 4, 2, 1],
	 [1, 2, 4, 2], 
	 [0, 1, 2, 4]]

B = [10, 10, 10, 10]

G = fatoracaoCholesky(A)
# Faz a transposição de G
Y = resolucaoSistema(G, B)
print(resolucaoSistema(G, Y))