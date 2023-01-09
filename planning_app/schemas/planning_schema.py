from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


# Pydantic schemas used to validate datas
class Skills(BaseModel):
    name:str
    category:str

    class Config():
        orm_mode=True

class PlanSkills(BaseModel):
    is_required:bool
    skills:Skills
    class Config():
        orm_mode=True

        
class Planning(BaseModel):
    id:int
    originalId:str
    talentId:Optional[str]=None
    talentName:Optional[str]=None
    talentGrade:Optional[str]=None
    bookingGrade:Optional[str]=None
    operatingUnit: str
    officeCity:Optional[str]=None
    officePostalCode:str
    jobManagerId:Optional[str]=None
    jobManagerName:Optional[str]=None
    totalHours:float
    startDate:datetime=None
    endDate:datetime=None
    clientId:str
    clientName:str
    industry:str
    isUnassigned:bool
    requiredSkills:List[PlanSkills]=[]
    class Config():
        orm_mode=True

