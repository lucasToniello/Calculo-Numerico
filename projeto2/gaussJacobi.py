#####################################################################
####################	Gauss-Jacobi	 ############################
#####################################################################
def modulo(x):
	if x < 0:
		return (-1) * x
	else:
		return x

def maxModulo(x):
	maior = 0

	for i in range(0, len(x)):
		if modulo(x[i]) > maior:
			maior = modulo(x[i])

	# Ver essa divisão por 0 aqui
	return maior + 0.00000000000000001

def distanciaAbsoluta(x0, x1):
	n = len(x0)
	d = [0 for i in range(0, n)]

	for i in range(0, n):
		d[i] = x1[i] - x0[i]

	return maxModulo(d)

def distanciaRelativa(x0, x1):
	# print(distanciaAbsoluta(x0, x1), distanciaAbsoluta(x0, x1) / maxModulo(x1), end="\n\n\n")
	return distanciaAbsoluta(x0, x1) / maxModulo(x1)

def iteracao(A, B, x0):
	n = len(A)
	x1 = [0 for i in range(0, n)]

	for i in range(0, n):
		x1[i] = B[i]

		for j in range(0, n):
			if i != j:
				x1[i] = x1[i] - (A[i][j] * x0[j])

		x1[i] = x1[i] / A[i][i] 

	return x1

def gaussJacobi(A, B, x0, e):
	x1 = []

	while True:
		x1 = iteracao(A, B, x0)

		if distanciaRelativa(x0, x1) < e:
			return x1
		else:
			x0 = x1

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

# A = [[7, 1, 9, 0, 2, 1],
# 	 [3, 6, 2, 9, 6, 0],
# 	 [5, 4, 1, 8, 3, 2],
# 	 [1, 2, 9, 7, 0, 2],
# 	 [4, 6, 1, 0, 2, 8],
# 	 [3, 0, 4, 7, 6, 9]]

# B = [0, 4, 8, 5, 1, 2]

# x0 = [0, 4/6, 8, 5/7, 1/2, 2/9]

A = []
B = []
x0 = []

grau = (int)(input("Digite o grau do sistema: "))
print("Digite os valores da matriz A:")

for i in range(0, grau):
	new = []
	print("Valores da linha {}: " .format(i+1))

	for j in range(0, grau):
		new.append((float)(input("Valor {} {}: " .format(i+1, j+1))))

	A.append(new)

print("Digite os valores do vetor resolução (B):")

for i in range(0, grau):
	B.append(float(input("Valor {} do vetor: " .format(i+1))))

# Botar o nome oficial aqui
print("Digite os valores do vetor x0:")

for i in range(0, grau):
	x0.append(float(input("Valor {} do vetor: " .format(i+1))))

e = (float)(input("Digite a precisão e: "))

x = gaussJacobi(A, B, x0, e)
pprint(x)