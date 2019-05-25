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

	return maior

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

	while True:
		x1 = iteracao(A, B, x0)
		# print(x1)

		if distanciaRelativa(x0, x1) < e:
			print(x1)
			return x1
		else:
			x0 = x1

#####################################################################
############################	MAIN	#############################
#####################################################################
A = [[5, 2, 1, 0],
	 [2, 5, 2, 1], 
	 [1, 2, 5, 2], 
	 [0, 1, 2, 5]]

B = [1, 2, 3, 4]

x0 = [1/5, 2/5, 3/5, 4/5]
e = 0.00001

gaussSeidel(A, B, x0, e)