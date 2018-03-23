import os
import pytest

from django.core.management import call_command


@pytest.fixture(scope='session')
def testdata():
    """
    Simple fixture to return reference data
    :return:
    """

    class TestData():
        def __init__(self):
            self.datadir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data')

        def fn(self, fn):
            return os.path.join(self.datadir, fn)

        def uri(self, fn):
            udd = '/'.join(self.datadir.split('\\'))
            return 'file:///{}/{}'.format(udd, fn)

        def textdata(self, fn):
            with open(self.fn(fn), encoding='utf8') as f:
                return f.read()

    return TestData()


@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker, testdata):
    with django_db_blocker.unblock():
        call_command('loaddata', testdata.fn('initial_db.json'))
