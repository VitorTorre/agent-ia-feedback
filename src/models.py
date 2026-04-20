# src/models.py
from pydantic import BaseModel, Field
from typing import List

class RequestData(BaseModel):
    """Define a estrutura dos dados de entrada da nossa API."""
    cliente_id: str = Field(..., example="c-12345")
    renda_mensal: float = Field(..., gt=0, example=5000.00)
    score_serasa: int = Field(..., ge=0, le=1000, example=750)
    idade: int = Field(..., ge=18, example=35)
    tempo_emprego_meses: int = Field(..., ge=0, example=24)
    valor_solicitado: float = Field(..., gt=0, example=15000.00)

class ResponseData(BaseModel):
    """Define a estrutura dos dados de saída da nossa API."""
    cliente_id: str
    pontuacao_risco: int = Field(..., ge=0, le=100, description="Pontuação de risco de 0 (baixo) a 100 (alto).")
    nivel_risco: str = Field(..., example="Medio")
    fatores_criticos: List[str] = Field(..., example=["Valor solicitado é alto para a renda.", "Tempo de emprego é curto."])