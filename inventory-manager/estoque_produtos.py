#DICIONÁRIO PRODUTOS
produtos = {}

#ADICIONAR PRODUTOS
def adicionar_produtos():
    nome_produto = str(input("Nome do produto: "))
    qtd = int(input(f"Quantidade do produto {nome_produto}: "))
    valor = int(input(f"Valor do produto {nome_produto}: "))
    
    #criar um id para cada produto com base no tamanho do dicionário
    gerar_id = len(produtos) + 1
    
    #modificando dicionário 
    produtos[gerar_id] = {
        "nome": nome_produto,
        #segundo dict contendo o valor e quantidade
        "detalhes": {
            "quantidade": qtd,
            "valor": valor
        }
    }

#liSTAR PRODUTOS #AJUSTAR
def  listar_produtos():
    #lista de msg
    msg = []
    #ordenar produtos por ordem alfabética
    produtos_ordenados = sorted(produtos.items(), key=lambda item: item[1]["nome"])
    #percorrer 
    for chave, valor in produtos_ordenados:
        #acessando valores
        nome_p = valor["nome"]
        qtd = valor["detalhes"]["quantidade"]
        preco = valor["detalhes"]["valor"]
        msg_p = f"Produto: {nome_p} - Quantidade disponível: {qtd} - Preço: R$ {preco}"
        msg.append(msg_p)
    return msg
    
#REMOVER PRODUTOS
def remover_produto():
    produto_removido = input("Remover produto: ").strip().lower()
    for chave, valor in produtos.items():
        chave_produto = chave
    if produto_removido == valor["nome"]:
        #apaga pelo id do produto
        del produtos[chave_produto]
    else:
        return "[ERROR] Produto não encontrado!"
    
    
#ATUALIZAR QUANTIDADE DE PRODUTOS
def atualizar_quantidade():
    #pede nome do produto e quantidade a ser atualizada
    nome_p = input("Nome do produto: ").strip().lower()
    qtd_p = input("Nova quantidade: ")
    #pecorremos o dict produtos, obtendo a chave e o valor
    for chave, valor in produtos.items():
        #se o nome informado já existir no dict 
        nome_prod_atual = valor["nome"]
        if nome_p == nome_prod_atual:
        #qtd atualizada
            valor["detalhes"]["quantidade"] = qtd_p
            break
    else:
        return "[ERROR] Produto não encontrado"
                
        

#MENU 
def exibir_menu():
    return """
1 - Adicionar produto
2 - Listar produtos 
3 - Remover produto
4 - Atualizar a quantidade de produto
5 - Sair 
"""

#PROGRAMA PRINCIPAL
def main():
    while True:
        print(exibir_menu())
        opcao = input("Opção: ").strip()
        
        if opcao == "1":
            adicionar_produtos()
        elif opcao == "2":
            resultado = listar_produtos()
            for item in resultado:
                print(item)  
        elif opcao == "3":
            print(remover_produto())
        elif opcao == "4":
            print(atualizar_quantidade())
        elif opcao == "5":
            print("Encerrando programa...")
            break
        else:
            print("Opção inválida")

main()            