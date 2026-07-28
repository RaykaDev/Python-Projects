# 📚 To-Do List API

Este é um projeto desenvolvido para treinar lógica de programação, criação de APIs REST e manipulação de dados no back-end com Python.
**O objetivo é simples:** gerenciar uma lista de tarefas via API, permitindo adicionar, listar, concluir e remover tarefas.
<br>

## ✨ Sobre o Projeto

Neste sistema, as tarefas são armazenadas em uma lista, onde cada item é um objeto `Tarefa` (modelo Pydantic), contendo id opcional, nome, descrição e status de conclusão. <br> O usuário pode interagir com o sistema através dos endpoints da API, testados via Swagger UI (`/docs`), Insomnia ou Postman.

**O sistema também:**

- exige autenticação básica (usuário e senha) para acessar qualquer endpoint de tarefas
- adiciona novas tarefas com nome e descrição, validando que o nome não seja vazio e que não haja duplicidade
- lista todas as tarefas cadastradas, com nome, descrição e status de conclusão
- permite paginação na listagem, através dos parâmetros `page` e `size`
- permite ordenação na listagem, através do parâmetro `ordenar_por` (por nome)
- marca uma tarefa como concluída, buscando pelo nome
- remove uma tarefa existente, buscando pelo nome
- valida os dados de entrada com Pydantic (`BaseModel`)
- trata erros com `HTTPException`, retornando status codes apropriados (400, 401, 404, 422, etc.)
  <br>

## 📁 Estrutura de Arquivos

O projeto está organizado da seguinte forma:

- `app.py`: Script principal contendo a aplicação FastAPI e todas as rotas.
  <br>

## 🛠️ Tecnologias Utilizadas

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white)](https://docs.pydantic.dev/)
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

5. **Acesse a documentação interativa (Swagger UI):**

```bash
http://127.0.0.1:8000/docs
```

<br>

## 🔐 Autenticação

Todos os endpoints de tarefas exigem autenticação básica (usuário e senha). Para testes, utilize:

- **Usuário:** `user`
- **Senha:** `user`

No Swagger UI, clique no botão **Authorize** (canto superior direito) e informe as credenciais antes de testar as rotas.
<br>

## 📌 Endpoints

| Método   | Rota               | Descrição                                                         |
| -------- | ------------------ | ----------------------------------------------------------------- |
| `GET`    | `/`                | Rota raiz de boas-vindas                                          |
| `POST`   | `/nova_tarefa`     | Adiciona uma nova tarefa                                          |
| `GET`    | `/lista_tarefas`   | Lista as tarefas cadastradas, com suporte a paginação e ordenação |
| `PUT`    | `/concluir_tarefa` | Marca uma tarefa como concluída (por nome)                        |
| `DELETE` | `/deletar_tarefa`  | Remove uma tarefa (por nome)                                      |

<br>

## 📌 Parâmetros de Listagem (`/lista_tarefas`)

| Parâmetro     | Tipo   | Padrão | Descrição                                   |
| ------------- | ------ | ------ | ------------------------------------------- |
| `page`        | int    | `1`    | Número da página desejada                   |
| `size`        | int    | `6`    | Quantidade de itens por página              |
| `ordenar_por` | string | `None` | Campo de ordenação (aceita apenas `"nome"`) |

<br>

## 📌 Aprendizados

- Criação de APIs REST com FastAPI
- Validação de dados com Pydantic (`BaseModel`)
- Manipulação de listas como estrutura de "banco de dados" em memória
- Uso de query params opcionais e suas validações
- Tratamento de erros com `HTTPException`
- Diferença entre `is None` e comparação de valores
- Implementação de autenticação básica com `HTTPBasic` e `secrets.compare_digest`
- Lógica de paginação com slicing de listas
- Ordenação de listas de objetos com `sorted()` e `lambda`
- Testes de API com Swagger UI e Insomnia
