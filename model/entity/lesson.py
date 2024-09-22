class Lesson:
    def __init__(self, id, title, week_day, start_date, start_time, end_time):
        self.id = id
        self.title = title
        self.week_day = week_day
        self.start_date = start_date
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        return tuple(self.__dict__.values())