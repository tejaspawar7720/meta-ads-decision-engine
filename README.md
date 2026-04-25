## How to run
pip install -r requirements.txt
uvicorn api:app --reload

## API Endpoints
POST /metrics - Submit daily ad data
GET  /metrics - Get all metrics
POST /decision/auto - Get automated decision
POST /decision/manual - Get custom decision
GET  /trend - Get 3-day trend analysis

## Docs
http://localhost:8000/docs