from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from ..database import Base

class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    owner_name = Column(String, index=True)
    description = Column(String)
    creation_date = Column(DateTime, default=datetime.utcnow)