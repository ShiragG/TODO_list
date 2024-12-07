from sqlalchemy.sql.sqltypes import Integer, String, Boolean, Date
from db.database import Base
from sqlalchemy import Column

class DBTask(Base):
    __tablename__ = 'tasks'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(length=200))
    description=Column(String)
    is_completed=Column(Boolean)
    created_at=Column(Date)
    updated_at=Column(Date)