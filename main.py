from fastapi import FastAPI, HTTPException
import logging


app = FastAPI(title="Calculadora API")

#Esses logs vão para o stdout, que é capturado automaticamente pelo Terminal, Docker e pelo Azure App Service
logger = logging.getLogger("Calc Logger")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s"
           )

@app.get("/")
def root():
    logger.info("v1 Endpoint root chamado")
    return {
        "message": "v1 API de Calculadora no ar",
        "operations": ["soma", "subtracao", "multiplicacao", "divisao"]
    }

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/soma")
def soma(a: float, b: float):
    return {"resultado": a + b}


@app.get("/soma3")
def soma3(a: float, b: float, c: float):
    return {"resultado": a + b + c}

@app.get("/subtracao")
def subtracao(a: float, b: float):
    return {"resultado": a - b}

@app.get("/multiplicacao")
def multiplicacao(a: float, b: float):
    return {"resultado": a * b}

@app.get("/divisao")
def divisao(a: float, b: float):
    if b == 0:
        raise HTTPException(status_code=400, detail="Divisao por zero nao permitida")
    return {"resultado": a / b}
