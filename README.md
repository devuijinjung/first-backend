# first-backend

FastAPI 기반 백엔드 연습 프로젝트.

## Run (macOS)

````bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn src.app.main:app --reload
Endpoints
GET /

GET /health

Swagger: /docs

yaml
코드 복사

(※ README 안에 코드블록이 겹쳐 보이면, 그대로 붙여넣은 뒤 저장하면 정상으로 보임)

---

## 10) Git 커밋 & 푸시
```bash
git add .
git commit -m "Set up FastAPI project structure"
git push
````
