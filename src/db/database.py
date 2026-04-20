from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.config import settings
from .models import Base

engine = create_engine(settings.database_url, connect_args={"check_same_thread": False})
Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def save_analysis(db_session, request_data, response_data):
    from .models import AnalysisRecord
    db_record = AnalysisRecord(
        cliente_id=request_data.cliente_id,
        renda_mensal=request_data.renda_mensal,
        score_serasa=request_data.score_serasa,
        idade=request_data.idade,
        tempo_emprego_meses=request_data.tempo_emprego_meses,
        valor_solicitado=request_data.valor_solicitado,
        pontuacao_risco=response_data.pontuacao_risco,
        nivel_risco=response_data.nivel_risco,
        fatores_criticos=", ".join(response_data.fatores_criticos)
    )
    db_session.add(db_record)
    db_session.commit()
    db_session.refresh(db_record)
    return db_record