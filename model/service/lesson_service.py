from model.entity.lesson import Lesson
from model.repository.crud_repository import CrudRepository


class LessonService:
    def __init__(self):
        self.repo = CrudRepository(Lesson)

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

    @classmethod
    def find_by(cls, by):
        return cls.repo.find_by(by)