from sqlalchemy import BigInteger
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import text
from sqlalchemy import TIMESTAMP

from app.database.base_class import Base


class Organizations(Base):
    # __tablename__ = "organizations"

    org_id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    website = Column(String, nullable=True)
    phone = Column(BigInteger, nullable=True)
    address = Column(String, nullable=True)
    status = Column(String, default="Active")
    status_updated_at = Column(TIMESTAMP(timezone=True), server_default=text("CURRENT_TIMESTAMP"))
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP(timezone=True), server_default=text("CURRENT_TIMESTAMP"))
