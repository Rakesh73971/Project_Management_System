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

