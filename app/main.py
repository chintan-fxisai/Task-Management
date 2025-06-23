from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root_path():
    return {"Hello": "World"}
