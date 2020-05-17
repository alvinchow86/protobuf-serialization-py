from datetime import datetime

from dateutil.tz import UTC


def utcnow():
    return datetime.utcnow().replace(tzinfo=UTC)
