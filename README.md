# 📌 Projeto: Busca de Operadoras de Saúde

Este repositório contém dois projetos:
- **API**: Backend em Python (FastAPI) que lê os dados das operadoras de saúde a partir de um arquivo CSV.
- **vue-operadoras**: Frontend em Vue.js que permite buscar operadoras de saúde.

## 🚀 Tecnologias Utilizadas
- **Backend**: Python, FastAPI, Pandas, Uvicorn
- **Frontend**: Vue.js, Axios

## 📂 Estrutura do Repositório
```
/
│── API/              # Backend FastAPI
│   ├── server.py     # Código principal da API
│   ├── requirements.txt # Dependências do backend
│   └── dados_operadoras.csv # Base de dados CSV
│
│── vue-operadoras/   # Frontend Vue.js
│   ├── src/          # Código-fonte do Vue.js
│   ├── package.json  # Dependências do frontend
│   └── vite.config.js # Configuração do Vite
│
│── README.md         # Instruções do projeto
```

## 📌 1️⃣ Configuração do Backend (API)

### 🛠️ **Pré-requisitos**
- Python 3.8+
- Pip

### 🔧 **Instalação**
```sh
cd API
pip install -r requirements.txt
```

### ▶️ **Rodando o Servidor**
```sh
uvicorn server:app --reload
```
- O backend estará disponível em `http://127.0.0.1:8000`

## 📌 2️⃣ Configuração do Frontend (Vue.js)

### 🛠️ **Pré-requisitos**
- Node.js 16+
- NPM ou Yarn

### 🔧 **Instalação**
```sh
cd vue-operadoras
npm install
```

### ▶️ **Rodando o Frontend**
```sh
npm run dev
```
- Acesse `http://localhost:5173/` no navegador.

## 📌 3️⃣ Testando a API no Postman
1. Abra o **Postman**.
2. Crie uma requisição **GET** para:
   ```
   http://127.0.0.1:8000/buscar/?q=nome_da_operadora
   ```
3. Veja os resultados retornados.
