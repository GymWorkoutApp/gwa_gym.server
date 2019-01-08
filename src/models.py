from uuid import uuid4

from gwa_framework.models.base import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID


class GymModel(BaseModel):
    __tablename__ = 'gyms'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    logo_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String(100), nullable=False)
    cnpj = Column(String(20), nullable=False)
    phone = Column(String(20), nullable=False)
