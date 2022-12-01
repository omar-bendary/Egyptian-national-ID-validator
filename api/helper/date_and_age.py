from datetime import datetime, date


def str_to_date(date_string):
    date_object = datetime.strptime(date_string, "%Y%m%d")
    return date_object


def age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - \
        ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age
