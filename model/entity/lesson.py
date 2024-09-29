import re
from model.tools.lesson_validation import Validation


# if re.match(r"^[a-zA-z\s]{2,20}$", title) and re.match(r"^[a-zA-z0-9\s]{2,20}$", start_date):
#
class Lesson:
    def __init__(self, id, title, week_day, start_date, start_time, end_time):

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

        @property
        def end_time(self):
            return self._end_time

        @end_time.setter
        def end_time(self, end_time):
            self._end_time
        # self.id = id
        # def get_id(self):
        #     print("GET")
        #     return self.__id
        #
        # def set_id(self, id):
        #     print("SET")
        #     self.__id = id
        #
        #
        # # self.title = title
        # def get_title(self):
        #     print("GET")
        #     return self.__title
        #
        # def set_title(self, title):
        #     print("SET")
        #     if type(title) == str and re.match(r"^[a-zA-Z\s]{2,30}$", title):
        #         self.__title = title
        #     else:
        #         print("Invalid Title")
        #
        #
        # def get_week_day(self, week_day):
        #     print("GET")
        #     return self.__week_day
        #
        # def set_week_day(self, week_day):
        #     print("SET")
        #     # if type(week_day) == date:
        #     self.__week_day = week_day
        #     # else:
        #     #     print("Invalid Week_day")
        #
        # # self.start_date = start_date
        # def get_start_date(self, start_date):
        #     print("GET")
        #     return self.__start_date
        #
        # def set_start_date(self, start_date):
        #     print("SET")
        #     # if type(start_date) == date:
        #     self.__start_date = start_date
        #     # else:
        #     #     print("Invalid Start_date")
        #
        # # self.start_time = start_time
        # def get_start_time(self, start_time):
        #     print("GET")
        #     return start_time
        #
        # def set_start_time(self, start_time):
        #     print("SET")
        #     # if type(start_time) == time:
        #     self.__start_time = start_time
        #     # else:
        #     #     print("Invalid Strat_time")
        #
        # # self.end_time = end_time
        # def get_end_time(selfself, end_time):
        #     print("GET")
        #     return end_time
        #
        # def set_end_time(self, end_time):
        #     print("SET")
        #     # if type(end_time) == time:
        #     self.__end_time = end_time
        # #     # else:
        # #         print("Invalid End_time")

    def __repr__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        return tuple(self.__dict__.values())

