from typing import List, Optional
from fastapi import APIRouter, Depends, FastAPI
from sqlalchemy.orm import Session
from sqlalchemy import text
from fastapi_pagination import Page, Params
from fastapi_pagination.ext.sqlalchemy import paginate
from config import base
from .controllers import show_single_planning, show_all_plannings
from .schemas.planning_schema import Planning
from  .import models

router = APIRouter()
get_db = base.get_db
app = FastAPI()


#The get single planning route endpoint
@router.get('/planning/{id}', response_model=Planning)
def get_single_planning(
    id:int,
    db: Session=Depends(get_db)
):
    return show_single_planning(id, db)


#The get all planning route endpoint
@router.get('/plannings', response_model=Page[Planning]) 
def get_all_plannings(
    db:Session=Depends(get_db), 
    pagination:Params = Depends()
):
    return show_all_plannings(db, pagination)

#The search planning route endpoint
@router.get('/plannings/search', response_model=Page[Planning])
def get_search(
    db:Session=Depends(get_db),
    pagination:Params = Depends(),
    field:str="talentName",
    query:str=""
):
    if not query:
        return []
    plannings = (
        db.query(models.Planning)
        .filter(getattr(models.Planning, field)
        .like(f"%{query}%"))
    )
    return paginate(plannings, pagination)

#The sort planning route endpoint
@router.get('/plannings/sort', response_model=Page[Planning]) 
def sort_all_plannings(
    db:Session=Depends(get_db), 
    pagination:Params=Depends(),
    field: Optional[str] = "startDate"
):
    
    if field:
        plannings = db.query(models.Planning).order_by(text(field))
        return paginate(plannings, pagination)
      