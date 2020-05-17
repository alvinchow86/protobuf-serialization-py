from dateutil.tz import UTC


def proto_timestamp_to_datetime(timestamp):
    datetime = timestamp.ToDatetime().replace(tzinfo=UTC)
    return datetime
