from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

DATABASE_URL = "sqlite:///./tarefas.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

app = FastAPI(
    title="Lista de Tarefas",
    description="API para gerenciar tarefas",
    version="1.0.0",
    contact={"name": "Rayka"},
)


security = HTTPBasic()

# para fins de testes, não utilizei variáveis de ambiente
my_user = "user"
my_password = "user"


class tarefaDB(Base):
    __tablename__ = "Tarefas"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    descricao = Column(String, index=True)
    concluida = Column(Boolean, default=False)


class Tarefa(BaseModel):
    id: int | None = None
    nome: str
    descricao: str
    concluida: bool = False

    class Config:
        from_attributes = True


Base.metadata.create_all(bind=engine)


def sessao_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


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


@app.post("/nova_tarefa", response_model=Tarefa)
def nova_tarefa(
    # utiliza a class Tarefa como modelo esperado
    dado_tarefa: Tarefa,
    db: Session = Depends(sessao_db),
    credentials: HTTPBasicCredentials = Depends(autenticar_usuario),
):
    # tarefa existe?
    db_tarefa = db.query(tarefaDB).filter(tarefaDB.nome == dado_tarefa.nome).first()

    # se existe
    if db_tarefa:
        raise HTTPException(status_code=400, detail="Esta tarefa já existe no sistema")

    # cria objeto tarefa
    nova_tarefa = tarefaDB(
        nome=dado_tarefa.nome,
        descricao=dado_tarefa.descricao,
        concluida=dado_tarefa.concluida,
    )
    # persistir dados tarefa
    db.add(nova_tarefa)
    db.commit()
    db.refresh(nova_tarefa)

    return nova_tarefa


# LISTAR TODAS AS TAREFAS


@app.get("/lista_tarefas")
def listar_tarefas(
    db: Session = Depends(sessao_db),
    credentials: HTTPBasicCredentials = Depends(autenticar_usuario),
    ordenar_por: str | None = None,
    page: int = 1,
    size: int = 6,
):
    if page < 1 or size < 1:
        raise HTTPException(
            status_code=400, detail="Page e Size devem ser maiores que zero"
        )

    start = (page - 1) * size

    tarefas_query = db.query(tarefaDB)

    # ordenar tarefas por nome e concluida
    if ordenar_por == "nome":
        tarefas_query = tarefas_query.order_by(tarefaDB.nome)
    elif ordenar_por == "concluida":
        tarefas_query = tarefas_query.order_by(tarefaDB.concluida)

    total_tarefas = tarefas_query.count()
    tarefas = tarefas_query.offset(start).limit(size).all()

    if not tarefas:
        raise HTTPException(status_code=404, detail="Nenhuma tarefa encontrada")

    return {
        "page": page,
        "size": size,
        "total_registros": total_tarefas,
        "tarefas": [
            {"nome": t.nome, "descrição": t.descricao, "concluída": t.concluida}
            for t in tarefas
        ],
    }


# MARCAR TAREFA COMO CONCLUIDA


@app.put("/concluir_tarefa", response_model=Tarefa)
def concluir_tarefa(
    nome_tarefa: str | None = None,
    db: Session = Depends(sessao_db),
    credentials: HTTPBasicCredentials = Depends(autenticar_usuario),
):
    if nome_tarefa is None:
        raise HTTPException(
            status_code=422, detail="Informe o nome da tarefa para atualizar"
        )
    db_tarefa = db.query(tarefaDB).filter(tarefaDB.nome == nome_tarefa).first()

    if not db_tarefa:
        raise HTTPException(status_code=404, detail="Essa tarefa não existe no sistema")

    db_tarefa.concluida = True
    db.commit()
    db.refresh(db_tarefa)

    return db_tarefa


# EXCLUIR TAREFA


@app.delete("/deletar_tarefa", response_model=Tarefa)
def deletar_tarefa(
    nome_tarefa: str | None = None,
    db: Session = Depends(sessao_db),
    credentials: HTTPBasicCredentials = Depends(autenticar_usuario),
):
    if nome_tarefa is None:
        raise HTTPException(
            status_code=422, detail="Informe o nome da tarefa para deletar"
        )
    db_tarefa = db.query(tarefaDB).filter(tarefaDB.nome == nome_tarefa).first()

    if not db_tarefa:
        raise HTTPException(status_code=404, detail="Esta tarefa não existe no sistema")

    db.delete(db_tarefa)
    db.commit()

    return db_tarefa
