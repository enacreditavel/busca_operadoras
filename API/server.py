from fastapi import FastAPI, Query
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Permite apenas este domínio
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos os headers
)

# Carrega os dados do CSV
CSV_FILE = "./operadoras.csv"
df = pd.read_csv(CSV_FILE, delimiter=";", dtype=str)  # Garante que tudo seja tratado como string


@app.get("/buscar/")
def buscar_operadoras(q: str = Query(..., min_length=1)):
    """Busca operadoras que contenham o termo informado."""

    resultados = df[df.apply(lambda row: row.astype(str).str.contains(q, case=False, na=False).any(), axis=1)]

    return{"resultados":  resultados.where(pd.notna(resultados), None).to_dict(orient="records")}

# Para rodar o servidor:
# uvicorn server:app --reload

