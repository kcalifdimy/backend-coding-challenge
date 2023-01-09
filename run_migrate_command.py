from commands import planning
from sqlalchemy.orm import Session 
from config import base

#from conftest import Base, engine

#planning.migrate_database_planning(base.FIXTURE_DIR_PATH)

#print("status: database migrated successfully")



from commands import planning 
from config.base import FILE_TEST_DIR_PATH

engine = engine
get_db = get_db() 
db:Session = next(get_db)

def migrate_database(FILE_TEST_DIR_PATH):
    Base.metadata.create_all(bind=engine)
    db.add_all(setupMigrationData(FILE_TEST_DIR_PATH))
    db.commit()
