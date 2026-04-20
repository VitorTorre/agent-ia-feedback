import uvicorn
import asyncio
from fastapi import FastAPI
from src.api.endpoints import router as analysis_router
from src.config import settings
from src.core.service_manager import service_manager

app = FastAPI(title=settings.app_name, description="API para análise de risco e fornecimento de insights.", version=settings.app_version)
app.include_router(analysis_router, tags=["Analysis"])

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(service_manager.start_health_checker_loop())

@app.get("/")
def read_root():
    return {"message": f"Bem-vindo à {settings.app_name}. Acesse /docs para a documentação."}

if __name__ == "__main__":
    print("Iniciando o servidor FOLLAR Agent com Health Check...")
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)