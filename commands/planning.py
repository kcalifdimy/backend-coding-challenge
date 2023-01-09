from datetime import datetime
import json
from pathlib import Path
from sqlalchemy.orm import Session 
from config import base
from sqlalchemy import DateTime
from importlib import import_module


engine = base.engine
get_db = base.get_db() 
db:Session = next(get_db)

# This function  is used to set up migration of the three splitted json file
# from planning.json, the files are imported dynamically to make the design 
# architecture to be loosely coupled, where each file is not tied to another. 
def setupMigrationData(fixturePath):
    p = Path(fixturePath)
    for fixture_Path in p.iterdir():
        with open(fixture_Path, "r") as fixture_data_file:
            model_data = json.load(fixture_data_file)
        model = getattr(import_module(f'planning_app.models'), fixture_Path.name.split('.')[0])        
        for row in model_data:
            for column in model.__table__.columns:
                if isinstance(column.type, DateTime):
                    row[column.key] = datetime.strptime(row[column.key], '%m/%d/%Y %I:%M %p')
            yield model(**row)

#this function call the settupMigrationData function to add and commit the json file to
#  the database 
def migrate_database_planning(fixturePath):
    base.Base.metadata.create_all(bind=engine)
    db.add_all(setupMigrationData(fixturePath))
    db.commit()
    return {"status": " databse successfully migrated"}
