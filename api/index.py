from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Project Z v2 backend running"}