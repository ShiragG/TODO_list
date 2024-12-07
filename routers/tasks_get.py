from fastapi import APIRouter

router = APIRouter()

@router.get('/tasks')
def get_tasks():
    pass

@router.get('/tasks/{task_id}')
def get_tasks(task_id: int):
    pass