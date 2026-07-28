from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets
from pydantic import BaseModel

app = FastAPI()

lista_tarefas: list["Tarefa"] = []

security = HTTPBasic()

# para teste
my_user = "user"
my_password = "user"


class Tarefa(BaseModel):
    id: int | None = None
    nome: str
    descricao: str
    concluida: bool = False


def autenticar_usuario(credentials: HTTPBasicCredentials = Depends(security)):
    is_username_correct = secrets.compare_digest(credentials.username, my_user)
    is_password_correct = secrets.compare_digest(credentials.password, my_password)

    if not (is_username_correct and is_password_correct):
        raise HTTPException(
            status_code=401,
            detail="Usuário ou senha incorretos",
            headers={"WWW-Authenticate": "Basic"},
        )


# raiz da API
@app.get("/")
def home():
    return {"TO-DO-LIST": "Organize suas  tarefas"}


# ADICIONA NOVA TAREFA
@app.post("/nova_tarefa")
def nova_tarefa(
    # utiliza a class Tarefa como modelo esperado
    dado_tarefa: Tarefa,
    credentials: HTTPBasicCredentials = Depends(autenticar_usuario),
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
def listar_tarefas(
    credentials: HTTPBasicCredentials = Depends(autenticar_usuario),
    ordenar_por: str | None = None,
    page: int = 1,
    size: int = 6,
):
    if page < 1 or size < 1:
        raise HTTPException(
            status_code=400, detail="Page e Size devem ser maiores que zero"
        )

    if not lista_tarefas:
        raise HTTPException(status_code=404, detail="Não há nenhuma tarefa cadastrada")

    if ordenar_por is not None and ordenar_por != "nome":
        raise HTTPException(status_code=422, detail="Só é possível ordenar por 'nome' ")

    if ordenar_por == "nome":
        tarefas_ordenadas = sorted(
            lista_tarefas, key=lambda tarefa: tarefa.nome.lower()
        )
    else:
        tarefas_ordenadas = lista_tarefas

    # paginação
    start = (page - 1) * size
    end = start + size
    tarefas_paginadas = tarefas_ordenadas[start:end]

    if not tarefas_paginadas:
        raise HTTPException(status_code=404, detail="Página não encontrada")

    return {"Lista de tarefas": tarefas_paginadas}


# MARCAR TAREFA COMO CONCLUIDA
@app.put("/concluir_tarefa")
def concluir_tarefa(
    nome_tarefa: str | None = None,
    credentials: HTTPBasicCredentials = Depends(autenticar_usuario),
):
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
def deletar_tarefa(
    nome_tarefa: str | None = None,
    credentials: HTTPBasicCredentials = Depends(autenticar_usuario),
):
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
