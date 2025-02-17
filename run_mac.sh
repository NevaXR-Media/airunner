export $(cat .env | xargs)
uvicorn main:app --port 1234 --reload