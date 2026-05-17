#ADICIONAR TAREFAS#
def adicionar_tarefa(tarefas, nome):
        nova_tarefa = nome.lower()  
        #verifica se existe nova_tarefa em tarefas
        if nova_tarefa in tarefas:
                return "Essa tarefa já existe"
        else:
                #adiciona nova_tarefa no dicionário
                tarefas[nova_tarefa] = False
                return f"Tarefa '{nova_tarefa}' adicionada com sucesso!"


#LISTAR TAREFAS
def listar_tarefas(tarefas):
        #se não houver nenhuma tarefa 
        if not tarefas:
                return "Nenhuma tarefa cadastrada"
        else:
                resultado = ""
                #sortear tarefa em ordem alfabética e
                #pecorrer tarefas
                for tarefa_existente in sorted(tarefas):
                        #acessar status das tarefas
                        status = tarefas[tarefa_existente]
                        if status == True:
                               resultado += f" {tarefa_existente} ✅ Concluída\n"
                        else:
                               resultado += f"{tarefa_existente} ❌  Não concluída\n"
                return resultado.strip()
                

#REMOVER TAREFA
def remover_tarefa(tarefas, nome):
        #solicitar o nome via input
        nome = nome.lower()
        #se existir remove e exibe
        if nome in tarefas:
                #remove tarefa 
                del tarefas[nome]
                return f"Tarefa '{nome}' removida com sucesso!"
        else:
                return "Erro: Tarefa não encontrada."
        
                

#MARCAR TAREFA COMO CONCLUÍDA
def marcar_concluida(tarefas, nome):
        #solicitar nome da tarefa
        nome = nome.lower()
        #comparar se nova tarefa já existe tarefa
        if nome in tarefas:
                tarefas[nome] = True
                return f"Tarefa '{nome}' marcada como concluída!"
        else:
                return "Erro: Tarefa não encontrada."
                

#EXIBIR MENU

def exibir_menu():
        return """
1 - Adicionar tarefa  
2 - Listar tarefas  
3 - Remover tarefa  
4 - Marcar tarefa como concluída  
5 - Sair 

"""
                
        
#FUNÇÃO PRINCIPAL
def main():
        #inicilializar tarefas
        tarefas = {}
        #continua executando até optar por sair
        while True:
                #exibir menu 
                 print(exibir_menu())
                #pegar opção do usuário
                 opcao = input("Opção: ").strip()
                 if opcao == "1":
                        nome = input("Nova tarefa: ")
                        print(adicionar_tarefa(tarefas, nome))
                 elif opcao == "2":
                        print(listar_tarefas(tarefas))
                 elif opcao == "3":
                        nome = input("Remover tarefa: ")
                        print(remover_tarefa(tarefas, nome))
                 elif opcao == "4":
                        nome = input("Concluir tarefa: ")  
                        print(marcar_concluida(tarefas, nome))
                 elif opcao == "5":
                        print("Saindo do programa...")
                        break
                 else:
                        print("Opção inválida. Tente novamente.")

        
main()