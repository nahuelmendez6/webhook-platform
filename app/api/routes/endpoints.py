from fastapi import APIRouter, Depends
from app.api.dependencies import get_current_user
from app.schemas.endpoint import EndpointCreate

router = APIRouter()

@router.post("/endpoints")
async def create_endpoint(
    # valida automaticamente el body de la peticion (json) utilizando el modelo pydantic
    endpoint: EndpointCreate,
    # inyeccion de dependencias para obtener el usuario actual
    # esto le dice a FastAPI que necesita un usuari para funcionar
    current_user: dict = Depends(get_current_user)
):
    """
    Endpoint para crear un nuevo endpoint.
    Requiere autenticación mediante API Key y obtiene el usuario actual.
    """
    # Simulamos la creación del endpoint
    return {
        "message": "Endpoint creado exitosamente",
        "endpoint": endpoint.model_dump(),
        "created_by": current_user["username"]
    }