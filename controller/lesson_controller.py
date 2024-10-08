from model.entity.lesson import Lesson
from model.service.lesson_service import LessonService


class LessonController:

    @classmethod
    def save(cls, title, week_day, start_date, end_date):
        try:

            lesson = Lesson(title, week_day, start_date, end_date)
            LessonService.save(lesson)
            return True, "lesson saved"
        except Exception as e:
            return False, str(e)

    @classmethod
    def edit(cls, id, title, week_day, start_date, end_date):
        try:
            lesson = Lesson(id, title, week_day, start_date, end_date)
            LessonService.edit(lesson)
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
            return True, LessonService.find_all()
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_id(cls, id):
        try:
            return True, LessonService.find_by_id(id)
        except Exception as e:
            return False, str(e)


