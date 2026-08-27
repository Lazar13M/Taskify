from datetime import datetime
from app.schemas import TaskCreate,TaskUpdate

tasks=[]
next_id=1

def get_tasks():
    return tasks


def get_task(task_id:int):
    for task in tasks:
        if task["id"]==task_id:
            return task
    return None

def create_task(data:TaskCreate):
    global next_id
    task={
        "id":next_id,
        "title":data.title,
        "description":data.description,
        "completed":False,
        "created_at":datetime.now()
    }
    next_id+=1
    tasks.append(task)
    return task
#patch
def update_task(task_id:int,data:TaskUpdate):
    task=get_task(task_id)
    if task is None:
        return None
    #model dump pretvara Pydantic model u klasican dictionary
    updates=data.model_dump(exclude_unset=True)# ovo bi trebalo da je patch 
    #exclude_unset=True vraca dict samo sa poljima koja je klijent stvarno poslao
    # for key,value in updates.items():
    #     task[key]=value
    # return task
    if data.title is not None:
        task["title"]=data.title
    if data.description is not None:
        task["description"]=data.description
    if data.completed is not None:
        task["completed"]=data.completed
    return task


def delete_task(task_id:int):
    task=get_task(task_id)
    if task is None:
        return False
    tasks.remove(task)
    return True
