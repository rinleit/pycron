from datetime import datetime, timedelta
from nose.tools import assert_raises
from pytz import utc
import pycron


def test_minutes():
    def run(since, now):
        assert pycron.has_been('* * * * *', since, now)
        assert pycron.has_been('0 * * * *', since, now) is False
        assert pycron.has_been('1 * * * *', since, now)
        assert pycron.has_been('2 * * * *', since, now)
        assert pycron.has_been('3 * * * *', since, now)
        assert pycron.has_been('4 * * * *', since, now) is False

    run(datetime(2015, 6, 18, 0, 1), datetime(2015, 6, 18, 0, 3))


def test_hours():
    def run(since, now):
        assert pycron.has_been('* * * * *', since, now)
        assert pycron.has_been('* 0 * * *', since, now) is False
        assert pycron.has_been('* 1 * * *', since, now)
        assert pycron.has_been('* 2 * * *', since, now)
        assert pycron.has_been('* 3 * * *', since, now)
        assert pycron.has_been('* 4 * * *', since, now) is False

    run(datetime(2015, 6, 18, 1, 0), datetime(2015, 6, 18, 3, 0))


def test_days():
    def run(since, now):
        assert pycron.has_been('* * * * *', since, now)
        assert pycron.has_been('* * 0 * *', since, now) is False
        assert pycron.has_been('* * 1 * *', since, now)
        assert pycron.has_been('* * 2 * *', since, now)
        assert pycron.has_been('* * 3 * *', since, now)
        assert pycron.has_been('* * 4 * *', since, now) is False

    run(datetime(2015, 6, 1, 0, 0), datetime(2015, 6, 3, 0, 0))


def test_raises():
    since = datetime(2016, 6, 1, 0, 0)
    now = datetime(2015, 6, 3, 0, 0)
    assert_raises(ValueError, pycron.has_been, '* * * * *', since, now)


def test_timezone():
    since = datetime.now(tz=utc) - timedelta(hours=1)
    now = datetime.now(tz=None)

    assert pycron.has_been('* * * * *', since)
    assert_raises(TypeError, pycron.has_been, '* * * * *', since, now)
