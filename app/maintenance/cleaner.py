from time import time

from app.data_management import Repository, connection

class Cleaner:
    def __init__(self, 
                 time_record = int(time()), 
                 duration = 3600 * 4,
                 retention_seconds = 60):

        self.last_cleaning_timestamp = time_record
        self.duration = duration
        self.retention_seconds = retention_seconds

    def cleaning_check(self, 
                       conn = None):
         

        time_now = int(time())



        if time_now - self.last_cleaning_timestamp >= self.duration:
            self.last_cleaning_timestamp = time_now
            self.do_cleaning(time_now, conn)

        

    def do_cleaning(self, time_now, conn=None):
        if conn is None:
            conn = connection()
        with conn as c:
                repo = Repository(c)
                repo.delete_events(time_now - self.retention_seconds)

        