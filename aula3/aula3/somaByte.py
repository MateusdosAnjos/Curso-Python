def leByte():
	a = [0, 0, 0, 0, 0, 0, 0, 0]

	i = 7
	while i >= 0:
		a[i] = int(input())
		i = i - 1
	print("Byte = ",end='')
	imprimeByte(a)
	print("Em base 10: ",end='')
	print(base2para10(a))	
	return a

def eleva(a, b):
	resultado = 1
	i = 0
	while i < b:
		resultado = resultado * a
		i = i + 1
	return resultado
		
def base2para10(a):
	resultado = 0

	for i in range (8):
		resultado = resultado + (a[i] * eleva(2, i))

	return resultado

def imprimeByte(a):
	i = 7
	while i >= 0:
		print(a[i], end='')
		i = i - 1
	print()	
	return
		
def imprimeResultado(c):
	print("Resultado na base 2 (byte): ", end='')
	imprimeByte(c)
	print("Resultado em base 10: ",end='')
	print(base2para10(c))
	return	

def somaByte(a, b):
	c = [0, 0, 0, 0, 0, 0, 0, 0]
	vaiUm = 0

	for i in range(8):
		soma = a[i] + b[i] + vaiUm
		if (soma > 1):
			vaiUm = 1
		else:
			vaiUm = 0	
		c[i] = soma%2
		soma = 0

	if (vaiUm == 1):
		print("Overflow detectado! Resultado estará em mod 256")
	return c

def main():
	print("Programa que soma dois bytes a e b e devolve c, tal que: c = a + b")
	print("Entre com o byte a")
	a = leByte()
	print("Entre com o byte b")
	b = leByte()
	c = somaByte(a, b)
	imprimeResultado(c)
	return
main()