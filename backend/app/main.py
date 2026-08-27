from fastapi import FastAPI

app=FastAPI()

@app.get("/return")
def return_dict():
    return {}