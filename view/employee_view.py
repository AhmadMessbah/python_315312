from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg

from controller.employee_controller import EmployeeController
from view.component import LabelWithEntry, Table


class EmployeeView:
    def reset_form(self):
        self.id.set(0)
        self.name.set("")
        self.family.set("")
        self.age.set(0)
        # self.clear_table()
        # self.show_on_table()

    def table_click(self, selected_item):
        print(selected_item)

    def save_click(self):
        status, message = EmployeeController.save(self.name.get(), self.family.get(), self.age.get())
        if status:
            msg.showinfo("Save", message)
            self.reset_form()
        else:
            msg.showerror("Save Error", message)

    def edit_click(self):
        status, message = EmployeeController.edit(self.id.get(), self.name.get(), self.family.get(), self.age.get())
        if status:
            msg.showinfo("Edit", message)
            self.reset_form()
        else:
            msg.showerror("Edit Error", message)

    def remove_click(self):
        if msg.askyesno("Remove Employee", "Are you sure?"):
            status, message = EmployeeController.remove(self.id.get())
            if status:
                msg.showinfo("Remove", message)
                self.reset_form()
            else:
                msg.showerror("Remove Error", message)

    def __init__(self):
        win = Tk()
        win.geometry("600x300")

        self.id = LabelWithEntry(win, "Id", 20, 20, data_type="int", state="readonly")
        self.name = LabelWithEntry(win, "Name", 20, 60)
        self.family = LabelWithEntry(win, "Family", 20, 100)
        self.age = LabelWithEntry(win, "Age", 20, 140, data_type="int")

        self.table = Table(win, ["Id", "Name", "Family", "Age"], [60, 100, 100, 60], x=250, y=20, self.table_click)

        Button(win, text="Save", width=10, command=self.save_click).place(x=100, y=180)
        Button(win, text="Edit", width=10, command=self.edit_click).place(x=100, y=210)
        Button(win, text="Remove", width=10, command=self.remove_click).place(x=100, y=240)

        self.reset_form()

        win.mainloop()
