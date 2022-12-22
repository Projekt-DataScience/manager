import os
import time
import random
import sqlalchemy

from backend_db_lib.models import base, LPAQuestion, LPAQuestionCategory
from backend_db_lib.manager import DatabaseManager

DATABASE_URL = f"postgresql://{os.environ.get('DB_USER')}:{os.environ.get('DB_PASSWORD')}@{os.environ.get('DB_HOSTNAME')}:{os.environ.get('DB_PORT')}/{os.environ.get('DB_NAME')}"

	
db = DatabaseManager(base, DATABASE_URL)
def database_is_empty():
    table_names = sqlalchemy.inspect(db._db).get_table_names()
    return len(table_names) == 0
	
if not database_is_empty():
    print("DB already created")
    exit(0)
	
db.drop_all()
print("Tables dropped.")

db.create_all()
print("Tables created.")

CREATE_INITIAL_DATA = int(os.environ.get('CREATE_INITIAL_DATA', 0))
print("CREATE_INITIAL_DATA", CREATE_INITIAL_DATA, type(CREATE_INITIAL_DATA))
if CREATE_INITIAL_DATA == 1:
    db.create_initial_data()
    print("Data created.")