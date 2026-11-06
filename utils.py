from datetime import datetime, date

DATE_FORMAT = "%d.%m.%Y"

def parse_date(text):
    return datetime.strptime(text.strip(), DATE_FORMAT).date()

def format_date(d):
    return d.strftime(DATE_FORMAT)

def days_between(start, end):
    return (end - start).days

def is_valid_date(text):
    try:
        parse_date(text)
        return True
    except ValueError:
        return False

def add_days(start, days):
    from datetime import timedelta
    return start + timedelta(days=days)