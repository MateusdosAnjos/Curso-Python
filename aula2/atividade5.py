#Vamos criar uma funcao que recebe em um arquivo .txt uma lista das 
#quantidades de cada produto que foi comprado e devolve o valor total da
#compra
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

def imprimeEstoque(estoque):
        for item in estoque:
            print(item + " " + str(estoque[item]))

def calculaTotal(listaDeCompra, estoque):
    totalCompra = 0
    itemComprado = []
    quantidade = []
    arquivo = open(listaDeCompra, 'r')
    for linha in arquivo:
        itemQuantidade = linha.split(" ")
        itemComprado.append(itemQuantidade[0])
        quantidade.append(float(itemQuantidade[1]))
    arquivo.close()
    for i in range (len(itemComprado)):
        totalCompra = totalCompra + (estoque[itemComprado[i]] * quantidade[i])

    return totalCompra

def main():
    estoque = criaEstoque("loja.txt")
    imprimeEstoque(estoque)
    totalCompra = calculaTotal("listaDeCompra.txt", estoque)
    print("O total de sua compra foi: R$" + str(totalCompra))
main()