from datetime import datetime


def dateformat(timestamp_str, format='%A, %B %d, %Y'):
    """
    Helper utility to be used in jinja to format timestamps into dates

    :param timestamp_str: Timestamp string
    :param format: Date format to convert the string into
    :return: Formatted date string
    """
    if not timestamp_str:
        return ''
    return datetime.strptime(timestamp_str, "%Y-%m-%dT%H:%M:%SZ").strftime(format)
