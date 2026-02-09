
from app.data_management import Repository, connection
from time import time

<<<<<<< HEAD
def event_creater(message_id, conn=None, db_path=None):
=======
def event_creater(message_id, conn):
>>>>>>> origin/develop

    if message_id == None:
        return
    
    if conn is None:
<<<<<<< HEAD
        conn = connection(path=db_path)
=======
        conn = connection()
>>>>>>> origin/develop
    with conn as c:
        repo = Repository(c)
        if message_id != None:
            repo.add_event(message_id, int(time()))