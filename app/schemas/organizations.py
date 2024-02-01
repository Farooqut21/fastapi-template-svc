from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field


class OrganizationCreate(BaseModel):
    name: str = Field(..., min_length=4)


class ShowOrganization(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    org_id: int
    name: str
    status: str

    # class Config():  #tells pydantic to convert even non dict obj to json
    #     from_attributes = True


class OrganizationUpdate(OrganizationCreate):
    pass
