from pydantic import BaseModel

class DeliveryCreate(BaseModel):
    """
    Clase que se usa para crear una nueva entrega, hereda de BaseModel
    """
    endpoint_id: int
    event_id: int
    status: str
    status_code: int | None = None