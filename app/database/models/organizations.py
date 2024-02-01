from app.database.base_class import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, text, JSON, BigInteger

class Organizations(Base):
    # __tablename__ = "organizations"
    
    org_id = Column(Integer, primary_key=True,nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    website = Column(String, nullable=True)
    phone = Column(BigInteger, nullable=True)
    address = Column(String, nullable=True)
    status = Column(String, default='Active')
    status_updated_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
    updated_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))