from fastapi.security import OAuth2PasswordBearer
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
import os
from app.data_modules.models import User
from app.routers import auth, users
from security import get_current_user


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

# Diretório onde os arquivos serão salvos
UPLOAD_DIRECTORY = "uploads"
os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)  # Cria a pasta se não existir


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Domínios permitidos
    allow_credentials=True,  # Permitir envio de cookies
    allow_methods=["*"],  # Métodos HTTP permitidos
    allow_headers=["*"],  # Cabeçalhos permitidos
)

app.include_router(users.router)
app.include_router(auth.router)



@app.get("/protected-route")
async def protected_route(current_user: User = Depends(get_current_user)):
    return {"message": f"Hello, {current_user.username}! This is a protected route."}