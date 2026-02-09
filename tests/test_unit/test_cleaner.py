import pytest
<<<<<<< HEAD
from pytest_mock import MockerFixture
=======
>>>>>>> origin/develop

from app.maintenance import Cleaner



<<<<<<< HEAD
def test_cleaner(mocker: MockerFixture):

    fake_connection = mocker.Mock()
    
    fake_cleaning = mocker.patch.object(Cleaner, 'do_cleaning')
=======
def test_cleaner(mocker):

    def fake_cleaning(time_now, conn):
        pass

    fake_connection = mocker.Mock()
    
    fake_cleaning = mocker.patch.object(Cleaner, '_do_cleaning')
>>>>>>> origin/develop

    cleaner = Cleaner()


    cleaner.cleaning_check(conn=fake_connection)

    assert fake_cleaning.call_count == 0


    cleaner.last_cleaning_timestamp = 0

    cleaner.cleaning_check(conn=fake_connection)

    assert fake_cleaning.call_count == 1