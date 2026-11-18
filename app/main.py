import time
import uuid
import httpx
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, BackgroundTasks
from fastapi.middleares.cors import CORSMiddleware
from app.api.routes import health, items

# 1. Lifespan: Incialización y liberación del cliente HTTP
http_client: httpx.AsyncClient | None = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global http_client
    # Startip: Incializar recurso globales
    http_client = httpx.AsyncClient()
    print("🟢 HTTPX Client inicializado")

    yield # Aqui la app esta corriendo y recibiendo trafico

    await http_client.aclose()
    print("🔴 HTTPX Client cerrado")





app = FastAPI(
    title="Webhook Platform API",
    lifespan=lifespan
    description="API para la plataforma de Webhooks",
    version="1.0.0"
)

# Incluir los routers de las rutas definidas en health.py y items.py
app.include_router(health.router, prefix="/api/v1")
app.include_router(items.router, prefix="/api/v1")