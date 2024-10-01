import tkinter
from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg

from controller.lesson_controller import LessonController
from view.component import LabelWithEntry, Table


class LessonView:
    def table_select(self):
        pass

    def reset_form(self):
        self.id.set(0)
        self.title.set("")
        self.week_day.set("")
        self.start_date.set(0)
        self.start_time.set("")
        self.end_time.set("")
        #self.clear_table()
        #self.show_on_table()

    def table_click(self, selected_item):
                print(selected_item)


    def save_click(self):
        status, message = LessonController.save(self.title.get(), self.week_day.get(), self.start_date.get())
        if status:
            msg.showinfo("Save", f"new lesson save")
            self.reset_form()
        else:
            msg.showerror("Save Error", f"we can't save the lesson")



    def edit_click(self):
        status, message = self.controller.edit(self.title.get(), self.week_day.get(), self.start_date.get(), self.age.get())
        if status:
            msg.showinfo("Edit", message)
            self.reset_form()
        else:
            msg.showerror("edit Error", f"we can't edit the lesson")



    def remove_click(self):
        if msg.askyesno("Remove Employee", "Are you sure?"):
            status, message = self.controller.remove(self.id.get())
            if status:
                msg.showinfo("Remove", message)
                self.reset_form()
            else:
                msg.showerror("Remove Error", message)


    def __init__(self):
        self.window = Tk()
        self.window.geometry('500x500')
        self.window.title("Lesson")

        tkinter.Label(self.window, text="Id").place(x=20, y=10)
        tkinter.Entry(self.window).place(x=80, y=10)

        tkinter.Label(self.window, text="Title").place(x=20, y=50)
        tkinter.Entry(self.window).place(x=80, y=50)

        tkinter.Label(self.window, text="week_day").place(x=20, y=90)
        tkinter.Entry(self.window).place(x=80, y=90)
        ttk.Combobox(self.window, values=["shanbeh","yek shanbeh" , "do shanbeh" , "se shanbeh","chahar shanbeh","panj shanbeh"]).place(x=80, y=90)

        tkinter.Label(self.window, text="start_date").place(x=20, y=130)
        tkinter.Entry(self.window).place(x=80, y=130)

        tkinter.Label(self.window, text="start_time").place(x=20, y=170)
        tkinter.Entry(self.window).place(x=80, y=170)

        tkinter.Label(self.window, text="end_time").place(x=20, y=210)
        tkinter.Entry(self.window).place(x=80, y=210)

       # self.table = Table(window, ["Id", "Name", "Family", "Age"], [60, 100, 100, 60], x=250, y=20,self.table_click)

        save_btn = tkinter.Button(self.window,
                             text="save",
                             bg="green",
                             fg="black",
                             font=("B titr", 10),
                             width=10, command=self.save_click)
        save_btn.place(x=50,y=400)

        edit_btn = tkinter.Button(self.window,
                             text="edit",
                             bg="yellow",
                             fg="black",
                             font=("B titr", 10),
                             width=10, command=self.edit_click)
        edit_btn.place(x=180, y=400)

        remove_btn = tkinter.Button(self.window,
                             text="remove",
                             bg="red",
                             fg="black",
                             font=("B titr", 10) ,
                             width=10, command=self.remove_click)
        remove_btn.place(x=300, y=400)






        self.window.mainloop()


ui = LessonView()