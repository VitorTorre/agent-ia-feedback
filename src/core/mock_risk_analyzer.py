import random
from src.models.models import RequestData, ResponseData

class MockRiskAnalyzer:
    def analyze(self, data: RequestData) -> ResponseData:
        print(f"[MOCK] Analisando cliente {data.cliente_id} com dados falsos...")
        fake_score = random.randint(0, 100)
        
        if fake_score < 30:
            fake_level = "Baixo"
            fake_factors = ["Histórico de pagamentos excelente (MOCK)."]
        elif fake_score < 70:
            fake_level = "Medio"
            fake_factors = ["Risco moderado, verificar mais a fundo (MOCK)."]
        else:
            fake_level = "Alto"
            fake_factors = ["Alto risco de inadimplência (MOCK)."]

        return ResponseData(
            cliente_id=data.cliente_id,
            pontuacao_risco=fake_score,
            nivel_risco=fake_level,
            fatores_criticos=fake_factors
        )

mock_risk_analyzer = MockRiskAnalyzer()