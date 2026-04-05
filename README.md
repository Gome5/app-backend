# API de Controle Financeiro

API backend para gerenciamento de receitas e despesas.

# Descrição

Esta API permite cadastrar, listar e remover movimentações financeiras, separadas em:

* Receitas (entradas de capital)
* Despesas (gastos)

Os dados incluem descrição, valor e data.

# Tecnologias utilizadas

* Python 3.11+
* Flask
* Flask-OpenAPI3
* SQLite
* Flask-CORS

---

# Como rodar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/Gome5/app-backend.git
cd seu-repo
```

### 2. Criar ambiente virtual

```bash
python -m venv venv
```

### 3. Ativar ambiente virtual

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### 4. Instalar dependências

```bash
(env)$ pip install -r requirements.txt
```

### 5. Rodar a aplicação

```bash
(env)$ flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

---

##  Endpoints

###  Receitas

#### GET /receita

Lista todas as receitas

#### POST /receita

Adiciona uma nova receita

**Body (form-data):**

```
descricao: string
valor: float
data: YYYY-MM-DD
```

#### DELETE /receita?id=1

Remove uma receita pelo ID

---

### Despesas

#### GET /despesas

Lista todas as despesas

#### POST /despesa

Adiciona uma nova despesa

**Body (form-data):**

```
descricao: string
valor: float
data: YYYY-MM-DD
```

#### DELETE /despesa?id=1

Remove uma despesa pelo ID

---

## Formato de data

A API aceita datas no formato padrão:

```
YYYY-MM-DD
```

Exemplo:

```
2026-04-04
```

---

## Possíveis erros

* `400 Bad Request` → dados inválidos
* `500 Internal Server Error` → erro interno (ex: formato de data incorreto)

---

## Exemplo de requisição (POST receita)

```bash
curl -X POST http://localhost:5000/receita \
  -F "descricao=Salário" \
  -F "valor=5000" \
  -F "data=2026-04-04"
```

---

## 👨‍💻 Autor

Gabriel Gomes
