import mysql.connector

from model.entity.lesson import Lesson


# save, edit, remove, find_all(), find_by_id()
class LessonRepository:
    def connect(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root123",
            database="mft"
        )
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, lesson):
        self.connect()
        self.cursor.execute("insert into lesson_tbl (title,week_day,start_date,start_time,end_time) values (%s,%s,%s,%s,%s)",
                            [lesson.title, lesson.week_day, lesson.start_date, lesson.start_time, lesson.end_time])
        self.connection.commit()
        self.disconnect()

    def edit(self, lesson):
        self.connect()
        self.cursor.execute("update lesson_tbl set title=%s,week_day=%s,start_date=%s, start_time=%s, end_time = %s where id=%s",
                            [lesson.title,lesson.week_day,lesson.start_date,lesson.start_time,lesson.end_time, lesson.id])
        self.connection.commit()
        self.disconnect()

    def remove(self, id):
        self.connect()
        self.cursor.execute("delete from lesson_tbl where id=%s", [id])
        self.connection.commit()
        self.disconnect()


    def find_all(self):
        self.connect()
        self.cursor.execute("select * from lesson_tbl")
        lesson_list = self.cursor.fetchall()
        lesson_list = [Lesson(*lessn) for lessn in lesson_list]
        self.disconnect()
        if lesson_list:
            return lesson_list


    def find_by_id(self, id):
        self.connect()
        self.cursor.execute("select * from lesson_tbl where id=%s", [id])
        lesn = self.cursor.fetchone()
        self.disconnect()
        if lesn:
            lesn = Lesson(*lesn)
            return lesn
