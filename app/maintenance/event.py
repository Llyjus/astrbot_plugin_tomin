
from app.data_management import Repository, connection
from time import time

def event_creater(message_id, conn = None):

    if conn is None:
        conn = connection()
    with conn as c:
        repo = Repository(c)
        if message_id != None:
            repo.add_event(message_id, int(time()))