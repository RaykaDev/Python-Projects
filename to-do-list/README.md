# 📚 To-Do List API

Este é um projeto desenvolvido para treinar lógica de programação, criação de APIs REST e manipulação de dados no back-end com Python.
**O objetivo é simples:** gerenciar uma lista de tarefas via API, permitindo adicionar, listar, concluir e remover tarefas.
<br>

## ✨ Sobre o Projeto

Neste sistema, as tarefas são armazenadas em um dicionário utilizando o **id** da tarefa como chave e um objeto `Task` (modelo Pydantic) como valor, contendo nome, descrição e status de conclusão. <br> O usuário pode interagir com o sistema através dos endpoints da API, testados via Swagger UI (`/docs`), Insomnia ou Postman.

**O sistema também:**

- adiciona novas tarefas com nome e descrição, gerando o id automaticamente
- lista todas as tarefas cadastradas, com nome, descrição e status de conclusão
- marca uma tarefa como concluída, buscando por id ou por nome
- remove uma tarefa existente, buscando por id ou por nome
- valida os dados de entrada com Pydantic (`BaseModel`)
- trata erros com `HTTPException`, retornando status codes apropriados (404, 422, etc.)
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

3. **Instale as dependências:**

```bash
pip install fastapi uvicorn
```

4. **Execute o servidor:**

```bash
fastapi dev app.py
```

5. **Acesse a documentação interativa (Swagger UI):**

```bash
http://127.0.0.1:8000/docs
```

<br>

## 📌 Endpoints

| Método   | Rota               | Descrição                                        |
| -------- | ------------------ | ------------------------------------------------ |
| `GET`    | `/`                | Rota raiz de boas-vindas                         |
| `POST`   | `/nova_tarefa`     | Adiciona uma nova tarefa                         |
| `GET`    | `/lista_tarefas`   | Lista todas as tarefas cadastradas               |
| `PUT`    | `/concluir_tarefa` | Marca uma tarefa como concluída (por id ou nome) |
| `DELETE` | `/deletar_tarefa`  | Remove uma tarefa (por id ou nome)               |

<br>

## 📌 Aprendizados

- Criação de APIs REST com FastAPI
- Validação de dados com Pydantic (`BaseModel`)
- Manipulação de dicionários como estrutura de "banco de dados" em memória
- Uso de path params e query params, e suas diferenças de obrigatoriedade
- Tratamento de erros com `HTTPException`
- Diferença entre `is None` e comparação de valores
- Testes de API com Swagger UI e Insomnia
