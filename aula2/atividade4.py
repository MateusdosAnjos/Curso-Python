#Vamos unir as atividades 2 e 3 em um unico codigo, para compreender o conceito
#de funcao.

def calculaDesconto(totalCompra):
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
    return valorPagar, desconto

def criaEstoque(entrada):
    itens = []
    preco = []
    estoque = {}
    arquivo = open(entrada, 'r')
    for linha in arquivo:
        itemValor = linha.split(" ")
        itens.append(itemValor[0])
        preco.append(float(itemValor[1]))
    for i in range (len(itens)):
        estoque[itens[i]] = preco[i]
    arquivo.close()

    return estoque

def main():
    estoque = criaEstoque("loja.txt")
    print(estoque)
main()