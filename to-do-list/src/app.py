from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

task_dates = {}


class Task(BaseModel):
    id: int
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
    # utiliza a class task como modelo esperado
    dado_tarefa: Task,
):
    if not dado_tarefa.nome.strip():
        raise HTTPException(status_code=422, detail="Nome não pode ser vazio.")
    # verifica se há tarefa duplicadas
    if dado_tarefa.id in task_dates:
        raise HTTPException(status_code=400, detail="Esta tarefa já existe")
    # adiciona o objeto dado_tarefa no banco de dados
    task_dates[dado_tarefa.id] = dado_tarefa
    return {"mensagem": "Tarefa adicionada com sucesso", "Tarefa:": dado_tarefa}


# LISTAR TODAS AS TAREFAS
@app.get("/lista_tarefas")
def lista_tarefas():

    if not task_dates:
        raise HTTPException(status_code=404, detail="Não há nenhuma tarefa cadastrada")

    return {"Lista de tarefas": task_dates}


# MARCAR TAREFA COMO CONCLUIDA
@app.put("/concluir_tarefa")
def concluir_tarefa(tarefa_id: int | None = None, nome_tarefa: str | None = None):
    if tarefa_id is None and nome_tarefa is None:
        raise HTTPException(
            status_code=422, detail="Informe o id ou o nome da tarefa para atualizar."
        )
    # concluir tarefa por ID
    if tarefa_id is not None:
        if tarefa_id not in task_dates:
            raise HTTPException(status_code=404, detail="Esta tarefa não existe")
        # recebe(referencia) o objeto de acordo com a chave (id) de identificação
        tarefa_encontrada = task_dates[tarefa_id]
        # altera o valor dentro do objeto
        tarefa_encontrada.concluida = True
        return {"mensagem": "Tarefa concluida", "Tarefa:": tarefa_encontrada}

    # concluir tarefa por nome
    for tarefa in task_dates.values():
        if tarefa.nome.lower() == nome_tarefa.lower():
            # altera o valor dentro do objeto
            tarefa.concluida = True
            return {"mensagem": "Tarefa concluida", "Tarefa:": tarefa}
    raise HTTPException(status_code=404, detail="Esta tarefa não existe")


# EXCLUIR TAREFA
@app.delete("/deletar_tarefa")
def deletar_tarefa(tarefa_id: int | None = None, nome_tarefa: str | None = None):
    if tarefa_id is None and nome_tarefa is None:
        raise HTTPException(
            status_code=422, detail="Informe o id ou o nome da tarefa para deletar."
        )
    # busca por id
    if tarefa_id is not None:
        if tarefa_id not in task_dates:
            raise HTTPException(status_code=404, detail="Esta tarefa não existe")
        # deletar tarefa
        tarefa_deletada = task_dates.pop(tarefa_id)
        return {
            "mensagem": "Tarefa deletada com sucesso",
            "Tarefa deletada:": tarefa_deletada,
        }
    # busca por nome
    for id_atual, tarefa in task_dates.items():
        if tarefa.nome.lower() == nome_tarefa.lower():
            tarefa_deletada = task_dates.pop(id_atual)
            return {
                "mensagem": "Tarefa deletada com sucesso",
                "Tarefa deletada:": tarefa_deletada,
            }

    raise HTTPException(status_code=404, detail="Esta tarefa não existe")
