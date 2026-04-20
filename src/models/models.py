from pydantic import BaseModel, Field
from typing import List

class RequestData(BaseModel):
    cliente_id: str = Field(..., example="c-12345")
    renda_mensal: float = Field(..., gt=0, example=5000.00)
    score_serasa: int = Field(..., ge=0, le=1000, example=750)
    idade: int = Field(..., ge=18, example=35)
    tempo_emprego_meses: int = Field(..., ge=0, example=24)
    valor_solicitado: float = Field(..., gt=0, example=15000.00)

class ResponseData(BaseModel):
    cliente_id: str
    pontuacao_risco: int = Field(..., ge=0, le=100, description="Pontuação de risco de 0 (baixo) a 100 (alto).")
    nivel_risco: str = Field(..., example="Medio")
    fatores_criticos: List[str] = Field(..., example=["Valor solicitado é alto para a renda.", "Tempo de emprego é curto."])



    # src/db/models.py
from sqlalchemy import Column, Integer, String, Float, DateTime, Text, Boolean, JSON # Adicione JSON
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

# ... (mantenha o AnalysisRecord antigo se quiser, ou remova-o)

class FeedbackAnalysis(Base):
    __tablename__ = "feedback_analyses"

    id = Column(Integer, primary_key=True, index=True)
    feedback_texto = Column(String, nullable=False, index=True)
    sentimento = Column(String, index=True)  # positivo/negativo/neutro
    topicos = Column(JSON)  # Salva como JSONB no PostgreSQL
    acao_sugerida = Column(Text)
    urgencia = Column(String, index=True)
    confianca_score = Column(Float) # A confiança que o LLM retornou
    processing_time_ms = Column(Integer) # Quanto tempo a análise levou
    created_at = Column(DateTime, default=datetime.utcnow, index=True)