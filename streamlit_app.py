from fastapi import FastAPI
from src.main import HospitalQueue

app = FastAPI()

queue = HospitalQueue()


@app.get("/")
def status():
    return {
        "status": "Project Z v2 backend running"
    }


@app.post("/add/{name}")
def add_patient(name: str):
    queue.queue.append(name)
    return {"added": name}


@app.get("/next")
def next_patient():
    if len(queue.queue) == 0:
        return {"message": "Queue empty"}
    p = queue.queue.pop(0)
    return {"serving": p}


@app.get("/all")
def all_patients():
    return {"queue": queue.queue}