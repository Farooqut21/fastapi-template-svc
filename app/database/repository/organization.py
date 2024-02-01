from sqlalchemy.orm import Session

from app.database.models.organizations import Organizations
from app.schemas.organizations import OrganizationCreate
from app.schemas.organizations import OrganizationUpdate


def create_new_org(organization: OrganizationCreate, database: Session):
    organization = Organizations(name=organization.name)
    database.add(organization)
    database.commit()
    database.refresh(organization)
    return organization


def retreive_org(id: int, database: Session):
    org = database.query(Organizations).filter(Organizations.org_id == id).first()
    return org


def list_orgs(database: Session):
    orgs = database.query(Organizations).all()
    return orgs


def update_org(id: int, organization: OrganizationUpdate, database: Session):
    org_in_database = (
        database.query(Organizations).filter(Organizations.org_id == id).first()
    )
    if not org_in_database:
        return

    org_in_database.name = organization.name
    database.add(org_in_database)
    database.commit()

    return org_in_database


def delete_org(id: int, database: Session):
    org_in_database = (
        database.query(Organizations).filter(Organizations.org_id == id)
    )
    if not org_in_database:
        return {"error": f"Could not find blog with id {id}"}

    org_in_database.delete()
    database.commit()
    return {"msg": f"deleted blog with id {id}"}
