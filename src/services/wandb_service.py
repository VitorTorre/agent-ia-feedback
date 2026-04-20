import wandb
from src.config import settings
from src.models.models import RequestData, ResponseData

class WandbService:
    def __init__(self):
        self.project_name = settings.wandb_project

    def log_analysis(self, request: RequestData, response: ResponseData):
        run = wandb.init(project=self.project_name, job_type="analysis", config=request.dict(), reinit=True)
        wandb.log({"pontuacao_risco": response.pontuacao_risco, "nivel_risco": response.nivel_risco, "num_fatores_criticos": len(response.fatores_criticos)})
        run.finish()

wandb_service = WandbService()