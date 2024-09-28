import re

from model.entity.lesson import Lesson
from model.service.lesson_service import LessonService


class LessonController:
    def __init__(self):
        self.service = LessonService()

    def save(self, title, week_day, start_date,start_time,end_time):

        if re.match(r"^[a-zA-z\s]{2,20}$", title) and re.match(r"^[a-zA-z0-9\s]{2,20}$", start_date):
            lessn = Lesson(None, week_day, start_date,start_time,end_time)
            error = self.service.save(lessn)
            if not error:
                return True, "Info : Lesson Saved"
            else:
                return False, error
        else:
            return False, "Error : Invalid Data"

    def edit(self, week_day, start_date,start_time,end_time):
        if re.match(r"^[a-zA-z\s]{2,20}$", title) and re.match(r"^[a-zA-z0-9\s]{2,20}$", start_date):
            lessn = Lesson(id, week_day, start_date,start_time,end_time)
            error = self.service.edit(lessn)
            if not error:
                return True, "Lesson Edited"
            else:
                return False, error
        else:
            return False, "Invalid Data"

    def remove(self, id):
        error = self.service.remove(id)
        if not error:
            return True, "Lesson Removed"
        else:
            return False, error

    def find_all(self):
        return self.service.find_all()
