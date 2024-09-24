from model.entity.lesson import Lesson
from model.repository.lesson_repository import LessonRepository


class LessonService
    def __init__(self):
        self.repo = LessonRepository()

    def save(self, lesson):
        if lesson.start_time < lesson.end_time:
            self.repo.save(lesson)
        else:
            return "start time should be less than end time!!!"

    def edit(self, lesson):
        if lesson.start_time < lesson.end_time:
            self.repo.edit(lesson)
        else:
            return "start time should be less than end time!!! !!!"


    def remove(self, id):
        self.repo.remove(id)


    def find_all(self):
        return self.repo.find_all()


    def find_by_id(self, id):
        return self.repo.find_by_id(id)
