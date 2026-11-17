from fastapi import APIRouter, Query
from app.schemas.item import Item, ItemResponse, ItemCreate

router = APIRouter()

# GET /api/v1/info
@router.get("/info", tags=["Info"])
async def get_info():
    return {"app": "Webhook Platform", "version": "1.0.0"}

# POST /api/v1/items (Request Body y Response Model)
@router.post("/items", response_model=ItemResponse, tags=["Items"])
async def create_item(item: ItemCreate):
    """
    Endpoint para crear un nuevo Item.
    Recibe un objeto ItemCreate en el cuerpo de la solicitud y retorna un objeto ItemResponse con la información del Item creado.
    """
    return ItemResponse(id=1, **item.model_dump())  # Simulando la creación de un Item con id=1

# GET /api/v1/items/{item_id} (Path Parameter y Query Parameter)
@router.get("/items/{item_id}", response_model=ItemResponse, tags=["Items"])
async def get_item(
    item_id: int, 
    include_details: bool = Query(False, description="Incluir detalles extra")
):
    # Simulamos la búsqueda
    item_data = {
        "id": item_id,
        "name": f"Item {item_id}",
        "price": 10.5
    }
    if include_details:
        item_data["description"] = "Detalles adicionales solicitados por query param"
        
    return item_data