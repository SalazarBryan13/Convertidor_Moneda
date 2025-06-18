from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import requests
from typing import Optional
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

app = FastAPI(title="Conversor de Monedas")

# Montar archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configurar templates
templates = Jinja2Templates(directory="templates")

# API key para exchangerate-api.com 
API_KEY = os.getenv("EXCHANGE_RATE_API_KEY", "490b83547ffe37e21dba1533")

class CurrencyConverter:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://v6.exchangerate-api.com/v6"

    async def get_exchange_rate(self, from_currency: str, to_currency: str) -> Optional[float]:
        try:
            url = f"{self.base_url}/{self.api_key}/pair/{from_currency}/{to_currency}"
            response = requests.get(url)
            data = response.json()
            return data.get("conversion_rate")
        except Exception as e:
            print(f"Error al obtener la tasa de cambio: {e}")
            return None

converter = CurrencyConverter(API_KEY)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )

@app.post("/convert")
async def convert_currency(
    request: Request,
    amount: float = Form(...),
    from_currency: str = Form(...),
    to_currency: str = Form(...)
):
    rate = await converter.get_exchange_rate(from_currency, to_currency)
    if rate is None:
        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "error": "Error al obtener la tasa de cambio. Por favor, intente nuevamente."
            }
        )
    
    result = amount * rate
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "result": result,
            "amount": amount,
            "from_currency": from_currency,
            "to_currency": to_currency,
            "rate": rate
        }
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 