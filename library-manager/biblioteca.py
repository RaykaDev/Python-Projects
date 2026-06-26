livros = dict()
emprestismos = []


def add_livros():
    try:
        titulo = input("Titulo do livro: ").lower()
        if not titulo.replace(" ", "").isalpha():
            # raise forçar um valueError manual, que o except captura como qualquer outro erro.
            raise ValueError("Titulo deve conter apenas letras.")

        dados_adicionais = {
            "quantidade": int(input("Quantidade de exemplares: ")),
            "autor": input("Nome do autor: "),
        }
        if not dados_adicionais["autor"].replace(" ", "").isalpha():
            raise ValueError("Nome do autor deve conter apenas letras.")

    except Exception as e:
        return f"[{e}] - Ocorreu um erro na entrada de dados."

    else:

        livros[titulo] = dados_adicionais
        return "Livro adicionado"


def listar_livros():
    print("LISTAR LIVROS")
    # Orderna o dict pela chave(titulo) em ordem alfabética e guarda em livros_ordenados
    livros_ordenados = dict(sorted(livros.items()))
    msg = []

    for title, info in livros_ordenados.items():
        msg.append(
            f"Título: {title} - Autor: {info["autor"]} - Quantidade: {info["quantidade"]}"
        )
    return "\n".join(msg) if msg else "Nenhum livro cadastrado."


def remover_livros():
    try:
        title_remove = input("Titulo do livro a ser removido: ").lower()

        if not title_remove.replace(" ", "").isalpha():
            raise ValueError("Titulo deve conter apenas letras.")

    except Exception as e:
        return f"ERROR [{e}] - Ocorreu um erro na entrada de dados."

    else:

        if title_remove in livros:
            del livros[title_remove]
            return "Livro removido"
        else:
            return "Livro não encontrado"


def atualizar_quantidade():
    try:
        title_livro = input("Titulo do livro para aplicar nova quantidade: ").lower()
        if not title_livro.replace(" ", "").isalpha():
            raise ValueError("Titulo deve conter apenas letras")
        qtd_nova = int(input("Nova quantidade: "))
    except Exception as e:
        return f"ERROR [{e} - Ocorreu um erro na entrada de dados]"

    else:
        if title_livro in livros:
            livros[title_livro]["quantidade"] = qtd_nova
            return f"Novo total: {qtd_nova} exemplares"
        else:
            return "Error - livro não encontrado."


def registrar_emprestimo():
    try:
        title_livro = input(
            "Qual é o titulo do livro para realizar o empréstimo?"
        ).lower()
        if not title_livro.replace(" ", "").isalpha():
            raise ValueError("O titulo deve conter apenas letras")
        qtd_desejada = int(
            input("Qual a quantidade de exemplares a serem emprestados: ")
        )
    except Exception as e:
        return f"ERROR [{e}] - Ocorreu um erro na entrada de dados"

    else:
        if title_livro in livros:
            qtd_disponivel = livros[title_livro]["quantidade"]
            if qtd_disponivel >= qtd_desejada:

                livros[title_livro]["quantidade"] -= qtd_desejada

                emprestismos.append({"titulo": title_livro, "quantidade": qtd_desejada})
                return f"Empréstimo realizado! Restam {livros[title_livro]['quantidade']} quantidades."
            else:
                return f"Exemplares insuficientes. Disponíveis: {qtd_disponivel}"
        else:
            return f"Livro '{title_livro}' não encontrado.'"


def exibir_historico_emprestimos():
    if not emprestismos:
        return "Nenhum empréstimo registrado"
    resultado = ["HISTÓRICO DE EMPRÉSTIMOS"]
    for emp in emprestismos:
        resultado.append(f"Livro: {emp['titulo']} | Quantidade: {emp['quantidade']}")
    return "\n".join(resultado)


def menu():
    return """
1. Adicionar livros
2. Listar livros
3. Remover livros
4. Atualizar quantidade de livros
5. Registrar empréstimo
6. Exibir historico de empréstimos
7. Sair
"""


def main():
    while True:
        print(menu())
        opcao = input("Opção: ").replace(" ", "")
        print()
        if opcao == "1":
            print(add_livros())
        elif opcao == "2":
            print(listar_livros())
        elif opcao == "3":
            print(remover_livros())
        elif opcao == "4":
            print(atualizar_quantidade())
        elif opcao == "5":
            print(registrar_emprestimo())
        elif opcao == "6":
            print(exibir_historico_emprestimos())
        elif opcao == "7":
            print("Encerrando programa...")
            break
        else:
            print("Opção inválida")


main()
