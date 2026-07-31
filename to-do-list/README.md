# 📚 To-Do List API

Este é um projeto desenvolvido para treinar lógica de programação, criação de APIs REST e persistência de dados no back-end com Python.
**O objetivo é simples:** gerenciar uma lista de tarefas via API, permitindo adicionar, listar, concluir e remover tarefas, com os dados persistidos em um banco de dados SQLite.
<br>

## ✨ Sobre o Projeto

Neste sistema, as tarefas são armazenadas em um banco de dados SQLite, mapeado através do SQLAlchemy (ORM), onde cada tarefa é um registro contendo id, nome, descrição e status de conclusão. As requisições de entrada e saída são validadas com modelos Pydantic (`BaseModel`). <br> O usuário pode interagir com o sistema através dos endpoints da API, testados via Swagger UI (`/docs`), Insomnia ou Postman.

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
  <br>

## 🛠️ Tecnologias Utilizadas

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white)](https://docs.pydantic.dev/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)](https://www.sqlalchemy.org/)
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
<br>

## ▶️ Como Rodar o Projeto

1. **Clone o repositório:**

```bash
https://github.com/RaykaDev/Python-Projects.git
```

2. **Navegue até a pasta do projeto:**

```bash
Python-Projects/todo-list-api
```

3. **Instale as dependências com Poetry:**

```bash
poetry install
```

4. **Execute o servidor:**

```bash
poetry run fastapi dev src/app.py
```

Ao subir a aplicação pela primeira vez, o arquivo `tarefas.db` é criado automaticamente na raiz do projeto.

5. **Acesse a documentação interativa (Swagger UI):**

```bash
http://127.0.0.1:8000/docs
```

<br>

## 🔐 Autenticação

Todos os endpoints de tarefas exigem autenticação básica (usuário e senha). Por se tratar de um projeto de estudo, as credenciais estão fixas no código (sem uso de variáveis de ambiente) para facilitar os testes:

- **Usuário:** `user`
- **Senha:** `user`

No Swagger UI, clique no botão **Authorize** (canto superior direito) e informe as credenciais antes de testar as rotas.

No Swagger UI, clique no botão **Authorize** (canto superior direito) e informe as credenciais antes de testar as rotas.
<br>

## 📌 Endpoints

| Método   | Rota               | Descrição                                                         |
| -------- | ------------------ | ----------------------------------------------------------------- |
| `GET`    | `/`                | Rota raiz de boas-vindas                                          |
| `POST`   | `/nova_tarefa`     | Adiciona uma nova tarefa ao banco de dados                        |
| `GET`    | `/lista_tarefas`   | Lista as tarefas cadastradas, com suporte a paginação e ordenação |
| `PUT`    | `/concluir_tarefa` | Marca uma tarefa como concluída (por nome)                        |
| `DELETE` | `/deletar_tarefa`  | Remove uma tarefa do banco de dados (por nome)                    |

<br>

## 📌 Parâmetros de Listagem (`/lista_tarefas`)

| Parâmetro     | Tipo   | Padrão | Descrição                                             |
| ------------- | ------ | ------ | ----------------------------------------------------- |
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
- Testes de API com Swagger UI e Insomnia
