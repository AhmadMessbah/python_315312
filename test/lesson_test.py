from controller.lesson_controller import LessonController
from model.entity.lesson import Lesson

lesson1 = Lesson(2, "riazi", "shanbeh","22","23")
print(lesson1)
print(lesson1.to_tuple())

print(LessonController.save("olom", "yekshanbeh", "20","27","29"))