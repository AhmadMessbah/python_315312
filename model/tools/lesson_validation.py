import re


class Validation:
    @staticmethod
    def title_validator(title, message):
        if type(title) == str and re.match(r"^[a-zA-Z\s]{2,20}$", title):
            return title
        else:
            raise ValueError(message)

   #  , start_time, end_time
    @staticmethod
    def week_day_validator(weekday, message):
        if type(weekday) == str and re.match(r"^[a-zA-Z\s]{2,20}$", weekday):
            return weekday
        else:
            raise ValueError(message)

    @staticmethod
    def start_date_validator(start_date, message):
        if type(start_date) == str and re.match(r"^[a-zA-Z\s]{2,20}$", start_date):
            return start_date
        else:
            raise ValueError(message)

    @staticmethod
    def end_time_validator(end_time, message):
        if type(end_time) == str and re.match(r"^[0-9]{2}:[0-9]{2}$", end_time):
            return end_time
        else:
            raise ValueError(message)

    @staticmethod
    def start_time_validator(start_time, message):
        if type(start_time) == str and re.match(r"^[0-9]{2}:[0-9]{2}$", start_time):
            return start_time
        else:
            raise ValueError(message)



