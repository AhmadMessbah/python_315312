from model.entity.lesson import Lesson
from model.repository.crud_repository import CrudRepository


class LessonService:
    repo = CrudRepository(Lesson)

    @classmethod
    def save(self, lesson):
        if lesson.start_time < lesson.end_time:
            self.repo.save(lesson)
        else:
            return "start time should be less than end time!!!"

    @classmethod
    def edit(self, lesson):
        if lesson.start_time < lesson.end_time:
            self.repo.edit(lesson)
        else:
            return "start time should be less than end time!!! !!!"

    @classmethod
    def remove(self, id):
        self.repo.remove(id)

    @classmethod
    def find_all(self):
        return self.repo.find_all()

    @classmethod
    def find_by_id(self, id):
        return self.repo.find_by_id(id)

    @classmethod
    def find_by(cls, by):
        return cls.repo.find_by(by)