import tkinter
from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg

from controller.lesson_controller import LessonController
from view.component import LabelWithEntry, Table


class LessonView:


    def reset_form(self):
        self.id.set(0)
        self.title.set("")
        self.week_day.set("")
        self.start_date.set(0)
        self.start_time.set("")
        self.end_time.set("")
        #self.clear_table()
        #self.show_on_table()

    @staticmethod

    def table_click(self, selected_item):
     print(selected_item)


     def save_click(self):
        status, message = LessonController.save(self.title.get(), self.week_day.get(), self.start_date.get())
        if status:
            msg.showinfo("Save",message)
            self.reset_form()
        else:
            msg.showerror("Save Error",message)



    def edit_click(self):
        status, message =LessonController.edit(self.id.get(),self.title.get(), self.week_day.get(), self.start_date.get(), self.age.get())
        if status:
            msg.showinfo("Edit", message)
            self.reset_form()
        else:
            msg.showerror("edit Error",message)



    def remove_click(self):
        if msg.askyesno("Remove Employee","are you sure?"):
            status, message =LessonController.remove(self.id.get())
            if status:
                msg.showinfo("Remove", message)
                self.reset_form()
            else:
                msg.showerror("Remove Error", message)


    def __init__(self):
        self.window = Tk()
        self.window.geometry('500x500')
        self.window.title("Lesson")


        self.id = LabelWithEntry(self.window, "Id", 20, 20, data_type="int", state="readonly")
        self.title = LabelWithEntry(self.window, "title", 20, 60)
        self.week_day = LabelWithEntry(self.window, "week day", 20, 100)
        self.start_time= LabelWithEntry(self.window, "start time", 20, 140, data_type="int")
        self.start_date= LabelWithEntry(self.window,"Start Date", 20, 180, data_type="int")
        self.end_time= LabelWithEntry(self.window, "End Date", 20, 200, data_type="int")


        self.table = Table(self.window, ["Id", "title", "week_day", "start_date","end_time"], [60, 100, 100, 60], 250, 20,self.table_click)
        self.table.refresh_table(LessonController.find_all()[1])


        Button(self.window, text="Save", width=10, command=self.save_click).place(x=100, y=180)
        Button(self.window, text="Edit", width=10, command=self.edit_click).place(x=100, y=210)
        Button(self.window, text="Remove", width=10, command=self.remove_click).place(x=100, y=240)

        self.reset_form()

        self.window.mainloop()

ui = LessonView()

