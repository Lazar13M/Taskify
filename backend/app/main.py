from fastapi import FastAPI
from app.schemas import TaskOut,TaskCreate,TaskUpdate
from app import crud
from fastapi import HTTPException
app=FastAPI()

@app.get("/health")
def healt_check():
    return {"state":"healty"}


@app.get("/tasks",response_model=list[TaskOut],status_code=200)
def list_tasks():
   return  crud.get_tasks()


@app.get("/tasks/{task_id}",response_model=TaskOut,status_code=200)
def list_task(task_id:int):
    task=crud.get_task(task_id)
    if task is  None:
        raise HTTPException(status_code=404,detail="item not found!")
    return task

@app.post("/tasks",response_model=TaskOut,status_code=201)
def make_task(data:TaskCreate):
    return crud.create_task(data)

@app.patch("/tasks/{task_id}",status_code=200)
def change_task(task_id:int,data:TaskUpdate):
   task=crud.update_task(task_id,data)
   if task is None:
       raise HTTPException(status_code=404,detail="not found!")
   return task


@app.delete("/tasks/{task_id}",status_code=204)
def remove_task(task_id:int):
    deleted= crud.delete_task(task_id)
    #delet_task vraca T/F ako je obr sve ok ako nije excp
    if not deleted:
        raise HTTPException(status_code=404,detail="task not found!")
    