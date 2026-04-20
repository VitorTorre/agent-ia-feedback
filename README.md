# agent-ia-feedback
Nesse diretóirio mostro como desenvolvi um protótipo (Agent de IA: FOLLA-AI) bem como a aplicação do agent de IA que projetei além dos objetivos centrais dele que é são baseados em classificar feedbacks em massa, alinhar categorias próximas e compilar numa forma mais clara para se intuir um insight bem pensado e ajudar nos avanços dos negócios que utilizarem tal ferramenta.

# 🤖 FOLLA-AI – Agente Inteligente para Classificação e Síntese de Feedbacks

[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.118.2-green)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

## 📌 Visão Geral

**FOLLA-AI** é um agente de IA projetado para processar **grandes volumes de feedbacks de clientes** (texto, imagens, áudios) e transformá-los em **insights estratégicos** de negócio. Ele automatiza três tarefas essenciais:

1. **Classificação em massa** – rotula cada feedback com categorias pré-definidas ou dinâmicas.
2. **Alinhamento semântico** – agrupa categorias similares (ex: “envio atrasou” e “logística demorada”) usando embeddings.
3. **Compilação e insight** – gera relatórios agregados e recomendações acionáveis em linguagem natural.

O sistema é modular, escalável e pode ser integrado via API REST, CLI ou dashboards interativos.

---

## 🎯 Objetivos Centrais

| Objetivo e Descrição |

| **Escala** | Processar milhares de feedbacks por hora, com suporte a textos longos, imagens (OCR) e áudios (STT). |
| **Precisão** | Utilizar modelos de última geração (LLMs locais ou via API) para classificação e deduplicação de categorias. |
| **Acionabilidade** | Entregar insights como: *“45% dos feedbacks negativos mencionam tempo de carregamento – priorizar otimização no mobile”*. |
| **Flexibilidade** | Permitir troca de provedores de IA (OpenAI, Anthropic, Google, Together, modelos locais). |

---

## 🧠 Arquitetura (stack real do projeto)

```mermaid
flowchart LR
    A[Feedbacks] --> B(Pré-processamento)
    B --> C{Classificador}
    C -->|LLM API| D[OpenAI/Anthropic/Google]
    C -->|Modelo local| E[HuggingFace/TensorFlow]
    D --> F[Alinhamento de categorias]
    E --> F
    F --> G[Compilador]
    G --> H[(PostgreSQL)]
    H --> I[API FastAPI]
    I --> J[Dashboard / Relatório]


Camada	Ferramentas / Bibliotecas
API e backend	FastAPI, Uvicorn, Pydantic, SQLAlchemy, Alembic
Classificação / LLM	OpenAI, Anthropic, Google Generative AI, Together AI, Transformers (Hugging Face)
Embeddings	sentence-transformers, tiktoken
OCR	PaddleOCR, pytesseract
Processamento de dados	Pandas, NumPy, Scikit-learn
Machine Learning	TensorFlow, Keras, PyTorch (via transformers), PaddlePaddle
Banco de dados	PostgreSQL (via SQLAlchemy) + Alembic para migrações
Automação	PyAutoGUI, pywinauto (para interação com sistemas legados)
Monitoramento	Weights & Biases (wandb), Sentry
Container	Docker (Dockerfile presente)

Pré‑requisitos
Python 3.11 ou superior

PostgreSQL (opcional, mas recomendado)

Docker (opcional)

Executando o servidor
Executar no terminar para testar o servidor

# Iniciar a API FastAPI (modo desenvolvimento)
uvicorn src.main:app --reload --port 8000

# Acesse a documentação interativa em http://localhost:8000/docs
Uso via CLI

# Classificar feedbacks a partir de um arquivo CSV
python follar-agent/cli.py classify --input feedbacks.csv --output resultados.json

# Gerar relatório de insights
python follar-agent/cli.py insights --input feedbacks.csv --format html
📡 Endpoints da API (exemplos)
Método	Endpoint	Descrição
POST	/v1/classify	Classifica um ou múltiplos feedbacks (JSON ou CSV).
POST	/v1/align	Recebe uma lista de categorias e retorna grupos semânticos.
GET	/v1/insights/{job_id}	Obtém o relatório compilado de um job assíncrono.
POST	/v1/feedback/ocr	Extrai texto de imagem e classifica o feedback.
Exemplo de requisição adivinda da aplicação FOLLA-IA:

json
POST /v1/classify
{
  "feedbacks": [
    "O aplicativo trava toda vez que abro o chat",
    "Adoro o design, mas a lentidão irrita"
  ],
  "model": "gpt-4o-mini",
  "categories": ["desempenho", "ux", "funcionalidade"]
}
Resposta:

json
{
  "results": [
    {"text": "O aplicativo trava...", "category": "desempenho", "confidence": 0.92},
    {"text": "Adoro o design...", "category": "ux", "confidence": 0.88}
  ],
  "insights": "Priorize correções de desempenho: 50% dos feedbacks apontam travamentos."
}

    
