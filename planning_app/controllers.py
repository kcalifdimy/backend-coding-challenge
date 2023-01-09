from typing import List, Optional
from fastapi import APIRouter, Depends, FastAPI,HTTPException,status
from sqlalchemy.orm import Session
from fastapi_pagination import Params
from fastapi_pagination.ext.sqlalchemy import paginate
from  .import models
from config import base
get_db = base.get_db

#The show single planning controller, where the business logic is done
def show_single_planning(
    id:int, db:Session
    ):
    planning=db.query(models.Planning).filter(models.Planning.id==id).first()
    if not planning:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Planning with the id {id} is not available")
    return planning

#The show all plannings controller, where the business logic is done
def show_all_plannings(
    db:Session, 
    pagination:Params 
):
    plannings = db.query(models.Planning)
    return paginate(plannings, pagination) 