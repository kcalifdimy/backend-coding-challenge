from commands import planning
from sqlalchemy.orm import Session 
from config import base

#from conftest import Base, engine

planning.migrate_database_planning(base.FIXTURE_DIR_PATH)

print("status: database migrated successfully")

