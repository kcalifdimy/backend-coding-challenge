from sqlalchemy import (
    Column, 
    Integer, 
    String, 
    Float, 
    DateTime,
    Boolean, 
    ForeignKey
)
from sqlalchemy.orm import relationship
from config.base import Base

# Model for each individual Isrequired and Optional skills
class Skills(Base):

    __tablename__ = 'skills'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    category = Column(String)

# Model for Isrequired and Optional skills
class PlanSkills(Base):

    __tablename__ = 'plan_skills'

    id = Column(Integer, primary_key=True, index=True)
   
    planning_id = Column(Integer, ForeignKey('plannings.id'))
    skill_id = Column(Integer, ForeignKey('skills.id'))
    is_required = Column(Boolean, default=True)
    skills = relationship("Skills",  backref="plan_skills")


#Model for Planning
class Planning(Base):

    __tablename__ = 'plannings'

    id = Column(Integer, primary_key=True, index=True)
    originalId = Column(String, unique=True)
    talentId = Column(String,  nullable=True)
    talentName = Column(String,  nullable=True)
    talentGrade = Column(String, nullable=True)
    bookingGrade = Column(String, nullable=True)
    operatingUnit = Column(String)
    officeCity = Column(String, nullable=True)
    officePostalCode = Column(String)
    jobManagerId = Column(String, nullable=True)
    jobManagerName = Column(String, nullable=True)
    totalHours = Column(Float)
    startDate = Column(DateTime)
    endDate = Column(DateTime)
    clientId = Column(String)
    clientName = Column(String)
    clientId = Column(String)
    industry = Column(String)
    isUnassigned = Column(Boolean)
    requiredSkills = relationship("PlanSkills",  backref="plannings")
