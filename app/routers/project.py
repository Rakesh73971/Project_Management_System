from fastapi import APIRouter,status,HTTPException,Depends
from sqlalchemy.orm import Session
from .. import schemas,models
from ..database import get_db
from typing import List
from ..oauth2 import get_current_user

router = APIRouter(
    prefix='/projects',
    tags=['Projects']
)

@router.get('/',status_code=status.HTTP_200_OK,response_model=List[schemas.ProjectResponse])
def get_projects(db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    projects = db.query(models.Project).all()
    return projects

@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=schemas.ProjectResponse)
def get_project(id:int,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    db_project = db.query(models.Project).filter(models.Project.id == id).first()
    if db_project is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'project with id {id} not found')
    return db_project


@router.post('/',status_code=status.HTTP_201_CREATED,response_model=schemas.ProjectResponse)
def create_project(project:schemas.ProjectCreate,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    project=models.Project(**project.dict())
    db.add(project)
    db.commit()
    db.refresh(project)
    return project


@router.patch('/{id}',status_code=status.HTTP_202_ACCEPTED,response_model=schemas.ProjectResponse)
def update_project(id:int,project:schemas.ProjectUpdate,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    db_project = db.query(models.Project).filter(models.Project.id == id)
    if db_project.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'project with id {id} not found')
    db_project.update(project.dict(exclude_unset=True),synchronize_session=False)
    db.commit()
    return db_project.first()



@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED,response_model=schemas.ProjectResponse)
def update_project(id:int,project:schemas.ProjectCreate,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    db_project = db.query(models.Project).filter(models.Project.id == id)
    if db_project.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'project with id {id} not found')
    db_project.update(project.dict(),synchronize_session=False)
    db.commit()
    return db_project.first()

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_project(id:int,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    db_project = db.query(models.Project).filter(models.Project.id == id).first()
    if db_project is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'project with id {id} not found')
    db.delete(db_project)
    db.commit()
    return None
