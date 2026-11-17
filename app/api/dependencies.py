"""
Inyeccion de dependencias: seguridad y obtencion del usuario
"""
from fastapi import Header, HTTPException, Depends
from typing import Annotated

# 1. Dependencia basica: validar API key
async def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != "my-secret-api-key":
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return x_api_key

# 2. Dependencia anidada: Obtener un usuario usando la validacion de la API Key
async def get_current_user(api_key: str = Depends(verify_api_key)):
    # Aquí en el futuro consultaríamos a la base de datos
    # Por ahora devolvemos un usuario simulado
    return {"id": 1, "username": "admin_user", "role": "admin"}