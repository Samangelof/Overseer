# db/models.py
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float, ForeignKey, Date, Text
from datetime import datetime, date
from db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    reports = relationship("DailyReport", back_populates="user")


class DailyReport(Base):
    __tablename__ = "daily_reports"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    date = Column(Date, nullable=False)
    mood = Column(Integer, nullable=False)
    worked_hours = Column(Float, nullable=False)
    showers = Column(Integer, nullable=False)
    relapse = Column(Boolean, default=False)
    note = Column(Text, nullable=True)

    user = relationship("User", back_populates="reports")


class Violation(Base):
    __tablename__ = "violations"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    report_id = Column(Integer, ForeignKey("daily_reports.id"))
    reason = Column(String, nullable=False)
    date = Column(Date, default=date.today)

    user = relationship("User")
    report = relationship("DailyReport")