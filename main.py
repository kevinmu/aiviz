from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/models/{model_id}")
def read_model(model_id: int):
    return {"model_id": model_id}
