from pydantic import BaseModel, Field, field_validator
from typing import Any

class EventCreate(BaseModel):
    """
    Clase que se usa para crear un nuevo evento, hereda de BaseModel
    """
    event_type: str = Field(..., min_length=2)
    # Aceptamos cualquier diccionario JSON como payload
    payload: dict[str, Any]

    @field_validator("event_type")
    @classmethod
    def event_type_must_be_lowercase(cls, v:str) -> str:
        """
        Validador para asegurar que el event_type esté en minúsculas
        """
        if not v.islower():
            raise ValueError("event_type must be lowercase")
        return v