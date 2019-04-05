#Funcao que recebe inteiros n, m e 
#inicializa uma matriz quadrada com n linhas e m colunas
#devolve a matriz inicalizada
def inicializaMatriz(n, m):
	A = [0] * n
	for i in range (n):
		A[i] = [0] * m
	return A
#Funcao que recebe uma matriz A de dimensoes n, m e a preenche
#linha por linha
def preencheMatriz(A, n, m):
	for i in range (n):
		for j in range (m):
			A[i][j] = int(input())
	return
#Funcao que recebe como parametro o nome de uma matriz e
#cria a matriz a partir do input
def criaMatriz(nome):
	print("Entre com as dimensoes (n,m) da matriz " + nome + ":")
	n = int(input())
	m = int(input())
	A = inicializaMatriz(n, m)
	print("Entre com a matriz " + nome + ":")
	preencheMatriz(A, n, m)
	return A, n, m
#Funcao que recebe duas matrizes A e B junto com suas dimensoes e
#as multiplica se possível devolvendo o resultado em C
def multiplicaMatriz(A, nA, mA, B, nB, mB):
	if (mA != nB):
		print("Problemas com as dimensoes das matrizes")
		return None, 0, 0
	else:
		C = [0] * nA
		for i in range (nA):
			C[i] = [0] * mB
		for i in range (nA):
			for j in range (mB):
				for k in range (mA):
					C[i][j] = C[i][j] + (A[i][k]*B[k][j])
		return C, nA, mB			
#Funcao que recebe uma matriz A, com seu nome, de dimensoes n, m e 
#imprime seu conteúdo
def imprimeMatriz(A, n, m, nome):
	print("Matriz " + nome + ":")
	for i in range (n):
		for j in range (m):
			print(A[i][j], end=' ')
		print()	
	return	
def main():
	A, nA, mA = criaMatriz("A")
	B, nB, mB = criaMatriz("B")
	C, nC, mC = multiplicaMatriz(A, nA, mA, B, nB, mB)
	imprimeMatriz(A, nA, mA, "A")
	imprimeMatriz(B, nB, mB, "B")
	C, nC, mC = multiplicaMatriz(A, nA, mA, B, nB, mB)
	if (C is not None):
		imprimeMatriz(C, nC, mC, "C")
	return
main()	
	