#####################################################################
############################	Gauss	 ############################
#####################################################################
def eliminacao(A, B):
	# Váriavel n irá conter o grau das operações
	n = len(A)

	# Para chegarmos em uma matriz triângular inferior, precisamos eliminar n colunas
	for k in range(0, n):

		# Para cada coluna, devemos eliminar k + 1 linhas
		for i in range(k + 1, n):
			# m contém o valor que irá eliminar o "primeiro" valor da linha
			m = A[i][k] / A[k][k]
			# Para evitarmos erros de pontos flutuantes, o "primeiro" valor da linha é zerado manualmente
			A[i][k] = 0

			# Agora basta fazermos as operações de subtração para os outros valores da linha
			for j in range (k + 1, n):
				# Novamente, para evitarmos erros de pontos flutuantes, os valores da subtração
				# são aproximados em 10 casas decimais.
				A[i][j] = round(A[i][j] - m * A[k][j], 10)

			# Por fim o vetor B também tem sua subtração efetuada da mesma forma
			B[i] = round(B[i] - m * B[k], 10)


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

A = [[3, 2, 4],
	 [1, 1, 2],
	 [4, 3, -2]]

B = [1, 2, 3]

eliminacao(A, B)
print(resolucaoSistema(A, B))