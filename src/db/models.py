from sqlalchemy import Column, Integer, String, Float, DateTime, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class AnalysisRecord(Base):
    __tablename__ = "analysis_records"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    cliente_id = Column(String, index=True)
    renda_mensal = Column(Float)
    score_serasa = Column(Integer)
    idade = Column(Integer)
    tempo_emprego_meses = Column(Integer)
    valor_solicitado = Column(Float)
    pontuacao_risco = Column(Integer)
    nivel_risco = Column(String)
    fatores_criticos = Column(Text)
    did_default = Column(Boolean, nullable=True)