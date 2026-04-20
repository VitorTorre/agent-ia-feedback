import os
from src.models.models import RequestData, ResponseData

class RiskAnalyzer:
    def analyze(self, data: RequestData) -> ResponseData:
        if not os.path.exists("real_service_enabled.flag"):
            raise FileNotFoundError("Serviço real de análise não está disponível.")
        
        fatores = []
        pontuacao_base = 100

        if data.score_serasa >= 700:
            pontuacao_base -= 40
        elif data.score_serasa >= 500:
            pontuacao_base -= 20
        else:
            fatores.append("Score Serasa baixo.")

        if data.valor_solicitado <= data.renda_mensal * 5:
            pontuacao_base -= 30
        elif data.valor_solicitado <= data.renda_mensal * 10:
            pontuacao_base -= 15
        else:
            fatores.append("Valor solicitado é muito alto em relação à renda.")

        if data.tempo_emprego_meses >= 24:
            pontuacao_base -= 20
        elif data.tempo_emprego_meses >= 12:
            pontuacao_base -= 10
        else:
            fatores.append("Tempo de emprego é curto.")
        
        pontuacao_final = max(0, min(100, pontuacao_base))

        if pontuacao_final < 30:
            nivel = "Baixo"
        elif pontuacao_final < 70:
            nivel = "Medio"
        else:
            nivel = "Alto"
            
        return ResponseData(
            cliente_id=data.cliente_id,
            pontuacao_risco=pontuacao_final,
            nivel_risco=nivel,
            fatores_criticos=fatores
        )

risk_analyzer = RiskAnalyzer()