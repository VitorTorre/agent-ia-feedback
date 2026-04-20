from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.models.models import RequestData, ResponseData
from src.core.service_manager import service_manager
from src.services.wandb_service import wandb_service
from src.exceptions import AnalysisError
from src.db.database import save_analysis, get_db

router = APIRouter()

@router.post("/analyze", response_model=ResponseData)
async def analyze_risk(request_data: RequestData, db: Session = Depends(get_db)):
    try:
        analysis_result = service_manager.analyze(request_data)
        wandb_service.log_analysis(request_data, analysis_result)
        save_analysis(db, request_data, analysis_result)
        return analysis_result
    except Exception as e:
        raise AnalysisError(str(e))