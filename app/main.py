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
async def lifespan(app: FastAPI): # define una funcion asincrona que recibe la instancia de FastAPI como parametro
    global http_client  # trabajamos con la funcion declarada afuera de la funcion
    # Startup: Incializar recurso globales
    http_client = httpx.AsyncClient()   # crea un cliente http asincrono
    print("🟢 HTTPX Client inicializado")

    yield # Aqui la app esta corriendo y recibiendo trafico

    # Shutdown: Liberar las conexiones al apagar
    await http_client.aclose()
    print("🔴 HTTPX Client cerrado")





app = FastAPI(
    title="Webhook Platform API",
    lifespan=lifespan
    description="API para la plataforma de Webhooks",
    version="1.0.0"
)

# 2. Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # En produccion, limitar a dominios reales
    allow_credentials=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)


# 3. Middleware personalizado: Duración y Request ID
@app.middleware("http")
async def add_process_time_and_request_id(request: Request, call_next):
    # Generar ID único para trazar la petición en los logs
    request_id = str(uuid.uuid4())
    start_time = time.time()

    # call_next envia la peticion al router y espera la respuesta
    response = await call_next(request)

    # calcular duración
    process_time = time.time() - start_time

    # Inyectar cabeceras en la respuesta saliente (modificacion de response)
    response.headers["X-Process-Time"] = f"{process_time:.4f} sec"
    response.headers["X-Request-ID"] = request_id

    return response

# Incluir los routers de las rutas definidas en health.py y items.py
app.include_router(health.router, prefix="/api/v1")
app.include_router(items.router, prefix="/api/v1")


# ---------- LOGICA DE EVENTOS Y BACKGROUND TASKS --------

# 4. Funcion que se ejecutara en segundo plano
async def process_event_task(event_id: str, payload: dict):
    print(f"⚙️ Iniciando procesamiento en background del evento: {event_id}")
    
    # Simulamos el envío de un webhook usando nuestro cliente global del Lifespan
    # await http_client.post("https://ejemplo.com/webhook", json=payload)
    
    print(f"✅ Evento {event_id} procesado y enviado.")


# 5. Endpoint para recibir el evento
@app.post("/api/v1/events",  tags=["Events"])
async def create_event(payload: dict, backgound_tasks: BackgroundTasks):
    # Simulamos guardar rapido en db
    event_id = str(uuid.uuid4())

    # Encolar la tarea pesada/lenta en segundo plano
    background_tasks.add_task(process_event_task, event_id, payload)

    return {
        "message": "Evento recibido. Procesamiento en segundo plano iniciado.",
        "event_id": event_id,
        "status": "queued"
    }