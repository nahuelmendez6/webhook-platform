from fastapi import FastAPI
from app.api.routes import health, items

app = FastAPI(
    title="Webhook Platform API",
    description="API para la plataforma de Webhooks",
    version="1.0.0"
)

# Incluir los routers de las rutas definidas en health.py y items.py
app.include_router(health.router, prefix="/api/v1")
app.include_router(items.router, prefix="/api/v1")