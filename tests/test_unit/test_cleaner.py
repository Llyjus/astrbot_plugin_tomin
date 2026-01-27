import pytest

from app.maintenance import Cleaner

def fake_cleaning(time_now, conn):
    pass

def test_cleaner(mocker):
    fake_connection = mocker.Mock()
    
    fake_cleaning = mocker.patch.object(Cleaner, '_do_cleaning')

    cleaner = Cleaner()


    cleaner.cleaning_check(conn=fake_connection)

    assert fake_cleaning.call_count == 0


    cleaner.last_cleaning_timestamp = 0

    cleaner.cleaning_check(conn=fake_connection)

    assert fake_cleaning.call_count == 1