# Conversor de Monedas - Clean Code

Este proyecto es una aplicación web para la conversión de monedas, desarrollada con FastAPI, HTML y CSS, siguiendo los principios de Clean Code.

## Conceptos de Clean Code Aplicados

A continuación se describen los conceptos de Clean Code aplicados y en qué archivos se encuentran:

### 1. Nombres significativos y pronunciables
- **Dónde:** `main.py`, `templates/index.html`, `static/styles.css`
- **Descripción:** Todas las variables, funciones y clases tienen nombres claros y descriptivos.

### 2. Funciones con una sola responsabilidad
- **Dónde:** `main.py`
- **Descripción:** Cada función realiza una única tarea específica, como obtener la tasa de cambio, renderizar la página principal o procesar la conversión.

### 3. Código DRY (Don't Repeat Yourself)
- **Dónde:** `main.py`, `templates/index.html`
- **Descripción:** Se evita la duplicación de lógica, reutilizando componentes y funciones cuando es posible.

### 4. Manejo adecuado de errores
- **Dónde:** `main.py`, `templates/index.html`
- **Descripción:** Se informa al usuario cuando ocurre un error en la obtención de la tasa de cambio, mostrando mensajes claros en la interfaz.

### 5. Separación de responsabilidades
- **Dónde:** `main.py`, `templates/index.html`, `static/styles.css`
- **Descripción:** El backend, la lógica de negocio, la presentación y los estilos están claramente separados en diferentes archivos y carpetas.

### 6. Código legible y mantenible
- **Dónde:** Todos los archivos
- **Descripción:** El código está bien estructurado, con comentarios mínimos y solo cuando es necesario.

### 7. Uso de clases para encapsular lógica
- **Dónde:** `main.py` (clase `CurrencyConverter`)
- **Descripción:** La lógica de conversión de monedas está encapsulada en una clase, facilitando su extensión y mantenimiento.

### 8. Manejo de configuración mediante variables de entorno
- **Dónde:** `main.py`, `.env`
- **Descripción:** La API key se gestiona mediante variables de entorno para mayor seguridad.

### 9. Diseño limpio  la interfaz
- **Dónde:** `static/styles.css`, `templates/index.html`
- **Descripción:** Se utiliza CSS moderno y una estructura HTML semántica para una experiencia de usuario clara y agradable.

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

2. Ejecuta la aplicación:
   ```bash
   python main.py
   ```
3. Accede a la app en `http://localhost:8000` 