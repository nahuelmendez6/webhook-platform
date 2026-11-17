"""
Para definir los modelos usamos la clase BaseModel de pydantic
"""

from pydantic import BaseModel
from typing import Optional

class ItemBase(BaseModel):
    """
    Clase base de la entidad Item, donde se definen los atributos y sus tipos
    """"
    
    name: str
    description: Optional[str] = None
    price: float

class ItemCreate(ItemBase):
    """
    Clase que se usa para crear un nuevo Item, hereda de ItemBase
    """
    pass

class ItemResponse(ItemBase):
    """
    Clase que se usa para responder con la información de un Item existente
    """
    id: int