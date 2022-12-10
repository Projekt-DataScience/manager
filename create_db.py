import os
import time

from backend_db_lib.models import base
from backend_db_lib.manager import DatabaseManager

if os.path.exists("/root/db_created.txt"):
    print("DB already created")
    exit(0)

DATABASE_URL = f"postgresql://{os.environ.get('DB_USER')}:{os.environ.get('DB_PASSWORD')}@{os.environ.get('DB_HOSTNAME')}:{os.environ.get('DB_PORT')}/{os.environ.get('DB_NAME')}"

db = DatabaseManager(base, DATABASE_URL)
db.drop_all()
db.create_all()

CREATE_INITIAL_DATA = int(os.environ.get('CREATE_INITIAL_DATA', 0))
print("CREATE_INITIAL_DATA", CREATE_INITIAL_DATA, type(CREATE_INITIAL_DATA))
if CREATE_INITIAL_DATA == 1:
    db.create_initial_data()

with open("/root/db_created.txt", "w") as f:
    f.write("1")