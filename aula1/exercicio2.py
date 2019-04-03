def main():
	peso = int(input("Qual seu peso? "))
	altura = float(input("Qual sua altura? "))
	print ("peso =", peso, "kg") 
	print ("altura =", altura, "metros")
	print ("IMC =", (peso/((altura)*(altura))))
main()	