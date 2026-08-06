# 📚 To-Do List API
 
Este é um projeto desenvolvido para treinar lógica de programação, criação de APIs REST e persistência de dados no back-end com Python.
**O objetivo é simples:** gerenciar uma lista de tarefas via API, permitindo adicionar, listar, concluir e remover tarefas, com os dados persistidos em um banco de dados SQLite.
<br>
 
## ✨ Sobre o Projeto
 
Neste sistema, as tarefas são armazenadas em um banco de dados SQLite, mapeado através do SQLAlchemy (ORM), onde cada tarefa é um registro contendo id, nome, descrição e status de conclusão. As requisições de entrada e saída são validadas com modelos Pydantic (`BaseModel`). <br> O usuário pode interagir com o sistema através dos endpoints da API, testados via Swagger UI (`/docs`), Insomnia ou Postman.
 
A aplicação é executada em um container Docker/Podman, com o ambiente Python e as dependências gerenciadas via Poetry.
 
**O sistema também:**
 
- exige autenticação básica (usuário e senha) para acessar qualquer endpoint de tarefas
- persiste os dados em um banco de dados SQLite (`tarefas.db`), garantindo que as tarefas não se percam ao reiniciar o servidor
- adiciona novas tarefas com nome e descrição, validando que o nome não seja vazio e que não haja duplicidade
- lista todas as tarefas cadastradas, com nome, descrição e status de conclusão
- permite paginação na listagem, através dos parâmetros `page` e `size`
- permite ordenação na listagem, através do parâmetro `ordenar_por` (por `nome` ou `concluida`)
- marca uma tarefa como concluída, buscando pelo nome
- remove uma tarefa existente, buscando pelo nome
- valida os dados de entrada e formata as respostas com Pydantic (`BaseModel` e `response_model`)
- trata erros com `HTTPException`, retornando status codes apropriados (400, 401, 404, 422, etc.)
  <br>
## 📁 Estrutura de Arquivos
 
O projeto está organizado da seguinte forma:
 
- `app.py`: Script principal contendo a aplicação FastAPI, o modelo do banco de dados e todas as rotas.
- `tarefas.db`: Banco de dados SQLite gerado automaticamente ao rodar a aplicação.
- `Dockerfile`: Define a imagem do container, instalação do Poetry e das dependências do projeto.
- `docker-compose.yml`: Configura o ambiente do container, incluindo portas, volumes e variáveis de ambiente.
- `pyproject.toml` / `poetry.lock`: Arquivos de configuração e lock das dependências do Poetry.
- `.env`: Armazena as variáveis de ambiente utilizadas pela aplicação (não versionado).
  <br>
## 🛠️ Tecnologias Utilizadas
 
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white)](https://docs.pydantic.dev/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)](https://www.sqlalchemy.org/)
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Poetry](https://img.shields.io/badge/Poetry-60A5FA?style=for-the-badge&logo=poetry&logoColor=white)](https://python-poetry.org/)
[![Podman](https://img.shields.io/badge/Podman-892CA0?style=for-the-badge&logo=podman&logoColor=white)](https://podman.io/)
<br>
 
## ▶️ Como Rodar o Projeto
 
Este projeto foi containerizado, então basta ter o **Docker** (ou **Podman**, usado no desenvolvimento) e o **Docker Compose** (ou `podman-compose`) instalados na sua máquina. Não é necessário instalar Python, Poetry ou nenhuma dependência manualmente — tudo é resolvido dentro do container.
 
1. **Clone o repositório:**
```bash
git clone https://github.com/RaykaDev/Python-Projects.git
```
 
2. **Navegue até a pasta do projeto:**
```bash
cd Python-Projects/todo-list-api
```
 
3. **Crie o arquivo `.env` na raiz do projeto** (veja a seção [🔐 Autenticação](#-autenticação) abaixo para os valores usados neste projeto de estudo):
```dotenv
DATABASE_URL=sqlite:///./tarefas.db
my_user=user
my_password=user
```
 
4. **Construa e suba os containers:**
```bash
docker-compose up --build -d
```
 
> Se estiver usando Podman: `podman-compose up --build -d`
 
Esse comando builda a imagem (instalando Poetry e dependências) e sobe a aplicação em segundo plano (`-d`), já com **volumes configurados para sincronizar o código local com o container**, permitindo recarregamento automático (`--reload`) durante o desenvolvimento.
 
5. **Acesse a documentação interativa (Swagger UI):**
```bash
http://localhost:8000/docs
```
 
6. **Para parar os containers:**
```bash
docker-compose down
```
 
> Se estiver usando Podman: `podman-compose down`
 
<br>

## 🔐 Autenticação
 
Todos os endpoints de tarefas exigem autenticação básica (usuário e senha). As credenciais são carregadas via variáveis de ambiente (`.env`) e, **por se tratar de um projeto de estudo e testes, estão expostas abaixo apenas para facilitar a reprodução do exercício** — em um projeto real, as credenciais não estariam publicadas na documentação: 
 
- **Usuário:** `user`
- **Senha:** `user`
No Swagger UI, clique no botão **Authorize** (canto superior direito) e informe as credenciais antes de testar as rotas.
<br>
 
## 📌 Endpoints
 
| Método   | Rota               | Descrição                                                         |
| -------- | ------------------ | ------------------------------------------------------------------|
| `GET`    | `/`                | Rota raiz de boas-vindas                                          |
| `POST`   | `/nova_tarefa`     | Adiciona uma nova tarefa ao banco de dados                        |
| `GET`    | `/lista_tarefas`   | Lista as tarefas cadastradas, com suporte a paginação e ordenação |
| `PUT`    | `/concluir_tarefa` | Marca uma tarefa como concluída (por nome)                        |
| `DELETE` | `/deletar_tarefa`  | Remove uma tarefa do banco de dados (por nome)                    |
 
<br>

## 📌 Parâmetros de Listagem (`/lista_tarefas`)
 
| Parâmetro     | Tipo   | Padrão | Descrição                                             |
| ------------- | ------ | ------ | ------------------------------------------------------|
| `page`        | int    | `1`    | Número da página desejada                             |
| `size`        | int    | `6`    | Quantidade de itens por página                        |
| `ordenar_por` | string | `None` | Campo de ordenação (aceita `"nome"` ou `"concluida"`) |
 
<br>

## 📌 Aprendizados
 
- Criação de APIs REST com FastAPI
- Persistência de dados com SQLite e SQLAlchemy (ORM)
- Modelagem de tabelas com `declarative_base`, `Column` e tipos como `Integer`, `String` e `Boolean`
- Gerenciamento de sessões do banco de dados com `sessionmaker` e `Depends`
- Validação de dados com Pydantic (`BaseModel`) e serialização de respostas com `response_model`
- Uso de `Config.from_attributes` para converter objetos do SQLAlchemy em modelos Pydantic
- Uso de query params opcionais e suas validações
- Tratamento de erros com `HTTPException`
- Diferença entre `is None` e comparação de valores
- Implementação de autenticação básica com `HTTPBasic` e `secrets.compare_digest`
- Lógica de paginação e ordenação com métodos do SQLAlchemy (`offset`, `limit`, `order_by`)
- Containerização da aplicação com Docker/Podman, incluindo build de imagem, volumes e variáveis de ambiente
- Gerenciamento de dependências com Poetry dentro de um container
- Testes de API com Swagger UI e Insomnia
 
