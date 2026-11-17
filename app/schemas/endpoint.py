from pydantic import BaseModel, Field, HttpUrl

class EndpointCreate(BaseModel):
    """
    Clase que se usa para crear un nuevo endpoint, hereda de BaseModel
    """
    name: str = Field(..., max_length=100)
    # HttpUrl valida automaticamente que sea una URL valida (http/https)
    url: HttpUrl
    description: str | None = None