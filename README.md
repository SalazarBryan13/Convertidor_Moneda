# Conversor de Monedas - Clean Code

Este proyecto es una aplicación web para la conversión de monedas, desarrollada con FastAPI, HTML y CSS, siguiendo los principios de Clean Code.

## Conceptos de Clean Code Aplicados

A continuación se describen los conceptos de Clean Code aplicados y en qué archivos se encuentran, con ejemplos de código:

### 1. Nombres significativos y pronunciables
- **Implementación:** `main.py`, `templates/index.html`, `static/styles.css`
- **Descripción:** Todas las variables, funciones y clases tienen nombres claros y descriptivos..

**Ejemplo de `main.py`:**
```python
class CurrencyConverter:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://v6.exchangerate-api.com/v6"

    async def get_exchange_rate(self, from_currency: str, to_currency: str) -> Optional[float]:
        # Nombres claros que indican exactamente qué hace cada parámetro
```

### 2. Funciones con una sola responsabilidad
- **Localización:** `main.py`
- **Descripción:** Cada función realiza una única tarea específica.

**Ejemplo de `main.py`:**
```python
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    # Solo se encarga de renderizar la página principal
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/convert")
async def convert_currency(request: Request, amount: float = Form(...), from_currency: str = Form(...), to_currency: str = Form(...)):
    # Solo se encarga de la conversión de monedas
    rate = await converter.get_exchange_rate(from_currency, to_currency)
    # ...
```

### 3. Código DRY (Don't Repeat Yourself)
- **Ubicación:** `main.py`, `templates/index.html`
- **Descripción:** Se evita la duplicación de lógica.

**Ejemplo de `templates/index.html`:**
```html
<!-- Reutilización de la estructura de opciones de moneda -->
<select id="from_currency" name="from_currency" required>
    <option value="USD" {% if from_currency == 'USD' %}selected{% endif %}>USD - Dólar Americano</option>
    <option value="EUR" {% if from_currency == 'EUR' %}selected{% endif %}>EUR - Euro</option>
    <!-- ... -->
</select>
```

### 4. Manejo adecuado de errores
- **Componentes:** `main.py`, `templates/index.html`
- **Descripción:** Se informa al usuario cuando ocurre un error.

**Ejemplo de `main.py`:**
```python
async def get_exchange_rate(self, from_currency: str, to_currency: str) -> Optional[float]:
    try:
        url = f"{self.base_url}/{self.api_key}/pair/{from_currency}/{to_currency}"
        response = requests.get(url)
        data = response.json()
        return data.get("conversion_rate")
    except Exception as e:
        print(f"Error al obtener la tasa de cambio: {e}")
        return None
```

### 5. Separación de responsabilidades
- **Arquitectura:** `main.py`, `templates/index.html`, `static/styles.css`
- **Descripción:** El backend, la lógica de negocio, la presentación y los estilos están claramente separados.

**Ejemplo de estructura:**
```
proyecto/
├── main.py           # Lógica de negocio y backend
├── templates/        # Presentación
│   └── index.html
└── static/          # Estilos
    └── styles.css
```

### 6. Código legible y mantenible
- **Alcance:** Todos los archivos
- **Descripción:** El código está bien estructurado y es fácil de entender.

**Ejemplo de `static/styles.css`:**
```css
:root {
    --primary-color: #2c3e50;
    --secondary-color: #3498db;
    --background-color: #f5f6fa;
    /* Variables CSS para mantener consistencia */
}

.container {
    max-width: 800px;
    margin: 2rem auto;
    padding: 2rem;
    /* Estructura clara y organizada */
}
```

### 7. Uso de clases para encapsular lógica
- **Módulo:** `main.py` (clase `CurrencyConverter`)
- **Descripción:** La lógica de conversión está encapsulada en una clase.

**Ejemplo de `main.py`:**
```python
class CurrencyConverter:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://v6.exchangerate-api.com/v6"

    async def get_exchange_rate(self, from_currency: str, to_currency: str) -> Optional[float]:
        # Toda la lógica de conversión está encapsulada aquí
```

### 8. Manejo de configuración mediante variables de entorno
- **Entorno:** `main.py`, `.env`
- **Descripción:** La API key se gestiona mediante variables de entorno.

**Ejemplo de `main.py`:**
```python
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("EXCHANGE_RATE_API_KEY", "tu_api_key_aqui")
```

### 9. Diseño limpio y moderno en la interfaz
- **Frontend:** `static/styles.css`, `templates/index.html`
- **Descripción:** Se utiliza CSS  y una estructura HTML semántica.

**Ejemplo de `templates/index.html`:**
```html
<div class="container">
    <h1>Conversor de Monedas</h1>
    <form action="/convert" method="post" class="converter-form">
        <!-- Estructura semántica y clara -->
    </form>
</div>
```

---

## Estructura del Proyecto

- `main.py`: Lógica principal de la aplicación y rutas de FastAPI
- `templates/index.html`: Interfaz de usuario (frontend)
- `static/styles.css`: Estilos de la aplicación
- `requirements.txt`: Dependencias del proyecto
- `.env`: Variables de entorno (no incluido en el repositorio)

---

## Cómo ejecutar

1. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
2. Configura tu archivo `.env` con la API key de ExchangeRate-API.
3. Ejecuta la aplicación:
   ```bash
   python main.py
   ```
4. Accede a la app en `http://localhost:8000` 