from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from app.db.database import Base


class Plan(Base):
    __tablename__ = "plans"

    id = Column(Integer, primary_key=True, index=True)

    user_input = Column(Text, nullable=False)

    tasks = Column(Text, nullable=False)

    schedule = Column(Text, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)