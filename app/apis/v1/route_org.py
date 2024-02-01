from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.organizations import OrganizationCreate, ShowOrganization, OrganizationUpdate
from app.database.session import get_db
from app.database.repository.organization import create_new_org, retreive_org, list_orgs, update_org, delete_org


router = APIRouter()


@router.post("/org",response_model = ShowOrganization, status_code=status.HTTP_201_CREATED)
def create_organization(organization: OrganizationCreate, database: Session= Depends(get_db)):
    organization = create_new_org(organization=organization, database=database)
    return organization


@router.get("/org/{id}", response_model=ShowOrganization)
def get_org(id: int, database: Session= Depends(get_db)):
    org = retreive_org(id=id, database=database)
    if not org:
        raise HTTPException(detail=f"Org with ID {id} does not exist.", status_code=status.HTTP_404_NOT_FOUND)
    return org 


@router.get("/orgs", response_model=List[ShowOrganization])
def get_all_orgs(database: Session = Depends(get_db)):
    orgs = list_orgs(database=database)
    return orgs
    

@router.put("/org/{id}", response_model=ShowOrganization)
def update_a_org(id: int, organization: OrganizationUpdate, database: Session = Depends(get_db)):
    organization = update_org(id=id, organization=organization, database=database)
    if not organization:
        raise HTTPException(detail=f"Blog with id {id} does not exist")
    return organization


@router.delete("/org/{id}")
def delete_a_org(id: int, database: Session = Depends(get_db)):
    message = delete_org(id=id, database=database)
    if message.get('error'):
        raise HTTPException(detail=message.get('error'), status_code=status.HTTP_400_BAD_REQUEST)
    
    return {"msg":f"Successfully deleted blog with id {id}"}