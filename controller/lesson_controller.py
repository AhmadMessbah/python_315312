import re

from model.entity.lesson import Lesson
from model.service.lesson_service import LessonService


class LessonController:

    @classmethod
    def save(cls, id, title, week_day, start_date, start_time, end_time):
        try:

            lesson = Lesson(id, title, week_day, start_date, start_time, end_time)
            LessonService.save(lesson)
            return True, "lesson saved"
        except Exception as e:
            return False, str(e)

    @classmethod
    def edit(cls, id, title, week_day, start_date, start_time, end_time):
        try:
            lessn = Lesson(id, title, week_day, start_date, start_time, end_time)
            LessonService.edit(lessn)
            return True, "lesson edited"
        except Exception as e:
            return False, str(e)

    @classmethod
    def remove(cls, id):
        try:
            LessonService.remove(id)
            return True, "lesson removed"
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_all(cls):
        try:
            return True, LessonService.find_all(cls)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_id(cls, id):
        try:
            return True, LessonService.find_by_id(id)
        except Exception as e:
            return False, str(e)
