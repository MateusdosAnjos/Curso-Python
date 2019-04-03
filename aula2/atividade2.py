#Vamos criar uma função que decide o valor de desconto sobre o total de uma
#compra. Se o valor da compra for maior que 100 reais o desconto sera de 8%,
#caso contrario o desconto sera de 5% 
def main():
	totalCompra = float(input("Qual o total da compra?"))
	if totalCompra > 100:
		desconto = totalCompra * 0.08
		valorPagar = totalCompra * 0.92
		print("O total a pagar será de R$", valorPagar)
		print("O desconto foi de R$", desconto)
	else:
		desconto = totalCompra * 0.05
		valorPagar = totalCompra * 0.95
		print("O total a pagar será de R$", valorPagar)
		print("O desconto foi de R$", desconto)
main()	