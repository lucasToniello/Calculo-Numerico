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
		for j in range(i + 1, n + 1):
			soma = soma + A[i][j] * x[j]

		# Para então isolarmos o resultado de x e obtermos seu resultado
		x[i] = (B[i] - soma) / A[i][i]

	return x

def pprint(x):
	i = 1

	for prt in x:
		print("x{} = {}" .format(i, prt))
		i = i+1

#####################################################################
############################	MAIN	#############################
#####################################################################

# A = [[4, -1, 0, 0],
# 	 [-1, 4, -1, 0], 
# 	 [0, -1, 4, -1],
# 	 [0, 0, -1, 4]]

# B = [1, 1, 1, 1]

# A = [[4, 6, 7, 1, 2, 5],
# 	 [6, 8, 2, 12, 8, 0],
# 	 [7, 2, 3, 5, 3, 1],
# 	 [1, 12, 5, 1, 11, 3],
# 	 [2, 8, 3, 11, 9, 0],
# 	 [5, 0, 1, 3, 0, 10]]

# B = [10, 2, 3, 6, 12, 3]
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

eliminacao(A, B)
x = resolucaoSistema(A, B)
pprint(x);