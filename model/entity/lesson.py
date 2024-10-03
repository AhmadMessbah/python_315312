from model.entity.base import Base
from sqlalchemy import Column, Integer, String, Date


class Lesson(Base):
    __tablename__ = "lesson_tbl"

    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _title = Column("title", String)
    _week_day = Column("week_day", String(10))
    _start_date = Column("start_date", Date)
    _end_date = Column("end_date", Date)

    def __init__(self, id, title, week_day, start_date, end_date):
        self.id = id
        self._title = title
        self._week_day = week_day
        self._start_date = start_date
        self.end_date = end_date

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def week_day(self):
        return self._week_day

    @week_day.setter
    def week_day(self, week_day):
        self._week_day = week_day

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        self._start_date = start_date

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        self._start_time = start_time
