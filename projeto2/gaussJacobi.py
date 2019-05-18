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

	return maior

def distanciaAbsoluta(x0, x1):
	n = len(x0)
	d = [0 for i in range(0, n)]

	for i in range(0, n):
		d[i] = x1[i] - x0[i]

	return maxModulo(d)

def distanciaRelativa(x0, x1):
	# print(distanciaAbsoluta(x0, x1), maxModulo(x1), distanciaAbsoluta(x0, x1) / maxModulo(x1))
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
		# print(x1)

		if distanciaRelativa(x0, x1) < e:
			return x1
		else:
			x0 = x1

#####################################################################
############################	MAIN	#############################
#####################################################################
A = [[10, 2, 1],
	 [1, 5, 1], 
	 [2, 3, 10]]

B = [7, -8, 6]

x0 = [0.7, -1.6, 0.6]
e = 0.05

gaussJacobi(A, B, x0, e)