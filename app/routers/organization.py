from fastapi import APIRouter,status,HTTPException,Depends
from .. import schemas,models
from sqlalchemy.orm import Session
from ..database import get_db
from typing import List

router = APIRouter(prefix='/organizations',tags=['Organizations'])

@router.get('/',status_code=status.HTTP_200_OK,response_class=List[schemas.OrganizationResponse])
def get_organizations(db:Session=Depends(get_db)):
    organizations = db.query(models.Organization).all()
    return organizations

@router.get('/{id}',response_model=schemas.OrganizationResponse)
def get_organization(id:int,db:Session=Depends(get_db)):
    organization = db.query(models.Organization).filter(models.Organization.id == id).first()
    if organization is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'organization with id {id} not found')
    return organization

@router.post('/',status_code=status.HTTP_201_CREATED,response_model=schemas.OrganizationResponse)
def create_organization(organization:schemas.OrganizationCreate,db:Session=Depends(get_db)):
    organization_data = models.Organization(**organization.dict())
    db.add(organization_data)
    db.commit()
    db.refresh(organization_data)
    return organization_data

@router.patch('/{id}',status_code=status.HTTP_202_ACCEPTED,response_model=schemas.OrganizationResponse)
def update_organization(organization:schemas.OrganizationUpdate,db:Session=Depends(get_db)):
    organization_db = db.query(models.Organization).filter(models.Organization.id == id)
    if organization_db.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'organization with id {id} not found')
    organization_db.update(organization.dict(exclude_unset=True),synchronize_session=False)
    db.commit()
    return organization_db.first()
