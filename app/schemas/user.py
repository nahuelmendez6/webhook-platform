from pydantic import BaseModel, Field, EmailStr

class UserCreate(BaseModel):
    """
    Clase que se usa para crear un nuevo usuario, hereda de BaseModel
    """
    # validaciones de longitud
    username: str = Field(..., min_length=3, max_length=5, description="Nombre de usuario, entre 3 y 5 caracteres")
    # validacion de formato email automatico
    email: EmailStr
    password: str = Field(..., min_length=8, description="Contraseña del usuario, mínimo 8 caracteres")


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

    # Permite leer desde modelos de base de datos
    model_config = {"from_attributes": True}