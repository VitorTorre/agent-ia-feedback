import asyncio
import os
from src.models.models import RequestData, ResponseData
from src.core.risk_analyzer import risk_analyzer
from src.core.mock_risk_analyzer import mock_risk_analyzer
from src.config import settings

class ServiceManager:
    def __init__(self):
        self.real_analyzer = risk_analyzer
        self.mock_analyzer = mock_risk_analyzer
        self._is_real_service_healthy = False
        self.health_check_interval = settings.health_check_interval_ms / 1000.0

    def _check_real_service_health(self):
        is_healthy = os.path.exists("real_service_enabled.flag")
        if is_healthy != self._is_real_service_healthy:
            if is_healthy:
                print("🟢 SERVIÇO REAL está ONLINE. Voltando a usá-lo.")
            else:
                print("🔴 SERVIÇO REAL está OFFLINE. Alternando para o MODO MOCK.")
        self._is_real_service_healthy = is_healthy

    def analyze(self, data: RequestData) -> ResponseData:
        self._check_real_service_health()
        if self._is_real_service_healthy:
            try:
                return self.real_analyzer.analyze(data)
            except Exception as e:
                print(f"🔴 FALHA NO SERVIÇO REAL DURANTE ANÁLISE: {e}. Usando MODO MOCK.")
                return self.mock_analyzer.analyze(data)
        else:
            return self.mock_analyzer.analyze(data)

    async def start_health_checker_loop(self):
        print(f"🩺 Iniciando verificador de saúde a cada {settings.health_check_interval_ms}ms...")
        while True:
            await asyncio.sleep(self.health_check_interval)
            self._check_real_service_health()

service_manager = ServiceManager()