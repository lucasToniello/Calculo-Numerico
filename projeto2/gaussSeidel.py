#####################################################################
####################	Gauss-Seidel	 ############################
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
			if j < i:
				x1[i] = x1[i] - (A[i][j] * x1[j])
			elif j > i:
				x1[i] = x1[i] - (A[i][j] * x0[j])
			else:
				pass

		x1[i] = x1[i] / A[i][i] 

	return x1

def gaussSeidel(A, B, x0, e):
	x1 = []
	iteracoes = 0

	while True:
		x1 = iteracao(A, B, x0)
		iteracoes = iteracoes + 1

		if distanciaRelativa(x0, x1) < e:
			return x1, iteracoes
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

x, iteracoes = gaussSeidel(A, B, x0, e)
print("\nResolução do sistema após {} iteracoes:" .format(iteracoes))
pprint(x)