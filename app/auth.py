from fastapi import Security, HTTPException, status
from fastapi.security import APIKeyHeader

api_key_header = APIKeyHeader(name="GreenhouseDb-Key")

def check_key(api_key_header: str = Security(api_key_header)):

    # Ping the Db for this key 

    # If not found 
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Device is not authorized."
    )

