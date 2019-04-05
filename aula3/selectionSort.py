#Funcao que recebe uma lista A e devolve o indice do elemento
#de menor valor da lista A no intervalo [i, j[
def selecionaMenor(A, i, j):
	menor = i
	while i < j:
		if (A[i] < A[menor]):
			menor = i
		i = i + 1	
	return menor
#Algoritmo SelectionSort	
def selectionSort(A):
	menor = 0
	n = len(A)
	for i in range (n):
		menor = selecionaMenor(A, i, n)
		aux = A[i]
		A[i] = A[menor]
		A[menor] = aux
	return	

def main():
	A = [3, 2, 1, 7, 4, 4, 9, 0, 2, 7, 1, 5]
	print("Antes de ordenar:")
	print(A)
	selectionSort(A)
	print("Depois de ordenar:")
	print(A)
main()	
