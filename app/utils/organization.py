from sqlalchemy.orm import Session
from app.database.repository.organization import create_new_org
from app.schemas.organizations import OrganizationCreate


def create_random_org(database: Session):
    organization = OrganizationCreate(name="randomOrganization")
    organization = create_new_org(organization=organization, database=database)
    return organization