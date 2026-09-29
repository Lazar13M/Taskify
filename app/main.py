from fastapi import FastAPI

app = FastAPI(title="Taskify")


@app.get("/health")
def health():
    return {"status": "ok"}
