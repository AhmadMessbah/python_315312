from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg

class LessonView:
    def clear_table(self):
        for item in self.table.get_id():
            self.table.delete(item)




            def reset_form(self):
                self.id.set(0)
                self.title.set("")
                self.week_day.set("")
                self.start_date.set(0)
                self.start_time.set(0)
                self.end_time.set(0)
                self.clear_table()
                self.show_on_table()