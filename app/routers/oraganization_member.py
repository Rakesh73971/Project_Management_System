from fastapi import APIRouter,status,HTTPException,Depends
from sqlalchemy.orm import Session
from .. import schemas,models
from typing import List
from ..database import get_db
from ..oauth2 import get_current_user


router = APIRouter(
    prefix='/organizationmembers',
    tags=['Oranization Members']
)

@router.get('/',status_code=status.HTTP_200_OK,response_model=List[schemas.OrganizationMemberResponse])
def get_organization_members(db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    organization_members = db.query(models.OrganizationMember).all()
    return organization_members

@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=schemas.OrganizationMemberResponse)
def get_organizaton_member(id:int,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    db_organization_member = db.query(models.OrganizationMember).filter(models.OrganizationMember.id == id).first()
    if db_organization_member is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'organization member with id {id} not found')
    return db_organization_member

@router.post('/',status_code=status.HTTP_201_CREATED,response_model=schemas.OrganizationMemberResponse)
def create_organization_member(member:schemas.OrganizationMemberCreate,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    member_data = models.OrganizationMember(**member.dict())
    db.add(member_data)
    db.commit()
    db.refresh(member_data)
    return member_data

@router.patch('/{id}',status_code=status.HTTP_202_ACCEPTED,response_model=schemas.OrganizationMemberResponse)
def update_organization_member(id:int,member:schemas.OrganizationMemberUpdate,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    db_memeber = db.query(models.OrganizationMember).filter(models.OrganizationMember.id == id)
    existing_db = db_memeber.first()
    if existing_db is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'organization member with id {id} not found')
    db_memeber.update(member.dict(exclude_unset=True),synchronize_session=False)
    db.commit()
    return db_memeber.first()

@router.put('/{id}',status_code=status.HTTP_200_OK,response_model=schemas.OrganizationMemberResponse)
def update_organization_member(id:int,member:schemas.OrganizationMemberCreate,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    db_member = db.query(models.OrganizationMember).filter(models.OrganizationMember.id == id)
    if db_member.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'organization memeber with id {id} not found')
    db_member.update(member.dict(),synchronize_session=False)
    db.commit()
    return db_member.first()

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_organization_member(id:int,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    db_memeber = db.query(models.OrganizationMember).filter(models.OrganizationMember.id == id).first()
    if db_memeber is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'organization member with {id} not found')
    db.delete(db_memeber)
    db.commit()
    return None