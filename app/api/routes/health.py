from fastapi import APIRouter


"""
APIRouter es una clase que permite agrupar y modularizar las operaciones de ruta 
(endpoints) de la aplicación FastAPI. Esto facilita la organización del código y la reutilización de rutas en diferentes partes de la aplicación.
"""
router = APIRouter()

@router.get("/health", tags=["Health"])
async def health_check():
    """
    Endpoint para verificar el estado de salud de la aplicación.
    Retorna un mensaje indicando que la aplicación está funcionando correctamente.
    """
    return {"status": "ok", "message": "Service is running"}