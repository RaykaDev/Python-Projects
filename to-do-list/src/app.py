from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

lista_tarefas: list["Tarefa"] = []


class Tarefa(BaseModel):
    id: int | None = None
    nome: str
    descricao: str
    concluida: bool = False


# raiz da API
@app.get("/")
def home():
    return {"TO-DO-LIST": "Organize suas  tarefas"}


# ADICIONA NOVA TAREFA
@app.post("/nova_tarefa")
def nova_tarefa(
    # utiliza a class Tarefa como modelo esperado
    dado_tarefa: Tarefa,
):
    if not dado_tarefa.nome.strip():
        raise HTTPException(status_code=422, detail="Nome não pode ser vazio.")

    # verifica se há tarefa duplicadas
    for tarefa in lista_tarefas:
        if tarefa.nome.lower() == dado_tarefa.nome.lower():
            raise HTTPException(status_code=400, detail="Esta tarefa já existe")

    lista_tarefas.append(dado_tarefa)
    return {"mensagem": "Tarefa adicionada com sucesso", "Tarefa:": dado_tarefa}


# LISTAR TODAS AS TAREFAS
@app.get("/lista_tarefas")
def listar_tarefas():

    if not lista_tarefas:
        raise HTTPException(status_code=404, detail="Não há nenhuma tarefa cadastrada")
    return {"Lista de tarefas": lista_tarefas}


# MARCAR TAREFA COMO CONCLUIDA
@app.put("/concluir_tarefa")
def concluir_tarefa(nome_tarefa: str | None = None):
    if nome_tarefa is None:
        raise HTTPException(
            status_code=422, detail="Informe o nome da tarefa para atualizar"
        )
    for tarefa in lista_tarefas:
        if tarefa.nome.lower() == nome_tarefa.lower():
            tarefa.concluida = True
            return {"mensagem": "Tarefa concluida", "Tarefa": tarefa}
    raise HTTPException(status_code=404, detail="Esta tarefa não existe.")


# EXCLUIR TAREFA
@app.delete("/deletar_tarefa")
def deletar_tarefa(nome_tarefa: str | None = None):
    if nome_tarefa is None:
        raise HTTPException(
            status_code=422, detail="Informe o nome da tarefa para deletar"
        )
    for i, tarefa in enumerate(lista_tarefas):
        if tarefa.nome.lower() == nome_tarefa.lower():
            tarefa_deletada = lista_tarefas.pop(i)
            return {
                "mensagem": "Tarefa deletada com sucesso",
                "Tarefa deletada:": tarefa_deletada,
            }
    raise HTTPException(status_code=404, detail="Esta tarefa não existe.")
