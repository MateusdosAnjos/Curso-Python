import math

def main():
	baseMaior = 9
	baseMenor = 3
	perimetro = 22

	laterais = perimetro - (baseMaior + baseMenor)
	hipotenusa = laterais/2
	catetoBase = (baseMaior - baseMenor) / 2 
	catetoAltura = math.sqrt(hipotenusa*hipotenusa - catetoBase*catetoBase)
	area = ((baseMaior + baseMenor) * catetoAltura) / 2
	print("A área do trapézio é: ", area)
main()