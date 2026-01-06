from fastapi import HTTPException,status,Depends,APIRouter
from sqlalchemy.orm import Session
from .. import models,schemas
from ..database import get_db
from ..oauth2 import get_current_user
from typing import List

router = APIRouter(
    prefix='/tasks',
    tags=['Tasks']
)

@router.get('/',status_code=status.HTTP_200_OK,response_model=List[schemas.TaskResponse])
def get_tasks(db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    tasks = db.query(models.Task).all()
    return tasks

@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=schemas.TaskResponse)
def get_tasks(id:int,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    task = db.query(models.Task).filter(models.Task.id == id).first()
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'task with id {id} not found')
    return task



@router.post('/',status_code=status.HTTP_201_CREATED,response_model=schemas.TaskResponse)
def create_task(task:schemas.TaskCreate,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    task_data = models.Task(**task.dict())
    db.add(task_data)
    db.commit()
    db.refresh(task_data)
    return task_data


@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED,response_model=schemas.TaskResponse)
def update_task(id:int,task:schemas.TaskCreate,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    db_task = db.query(models.Task).filter(models.Task.id == id)
    if db_task.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'task with id {id} not found')
    db_task.update(task.dict(),synchronize_session=False)
    db.commit()
    return db_task.first()

@router.patch('/{id}',status_code=status.HTTP_202_ACCEPTED,response_model=schemas.TaskResponse)
def update_task(id:int,task:schemas.TaskUpdate,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    db_task = db.query(models.Task).filter(models.Task.id == id)
    if db_task.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'task with id { id} not found')
    db_task.update(task.dict(exclude_unset=True),synchronize_session=False)
    db.commit()
    return db_task.first()

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_task(id:int,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    db_task = db.query(models.Task).filter(models.Task.id == id).first()
    if db_task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'task with id {id} not found')
    db.delete(db_task)
    db.commit()
    return None