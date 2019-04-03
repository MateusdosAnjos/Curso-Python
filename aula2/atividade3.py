#Vamos criar uma funçao que recebe um arquivo .txt referente ao estoque de uma 
#loja com o nome e preço dos produtos e devolve um dicionario com nome de 
#cada produto sendo uma chave de valor igual ao preço do produto.
def main():
    itens = []
    preco = []
    dic = {}
    arquivo = open("loja.txt", 'r')
    for linha in arquivo:
        itemValor = linha.split(" ")
        itens.append(itemValor[0])
        preco.append(float(itemValor[1]))
    for i in range (len(itens)):
        dic[itens[i]] = preco[i]
    arquivo.close()
main()