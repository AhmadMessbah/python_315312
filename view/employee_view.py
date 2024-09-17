from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg

from controller.employee_controller import EmployeeController


class EmployeeView:
    def clear_table(self):
        for item in self.table.get_children():
            self.table.delete(item)

    def show_on_table(self):
        for employee in self.controller.find_all():
            self.table.insert("", END, values=employee.to_tuple())

    def reset_form(self):
        self.id.set(0)
        self.name.set("")
        self.family.set("")
        self.age.set(0)
        self.clear_table()
        self.show_on_table()

    def table_click(self, event):
        item_id = self.table.focus()
        item = self.table.item(item_id)
        emp = item["values"]
        self.id.set(emp[0])
        self.name.set(emp[1])
        self.family.set(emp[2])
        self.age.set(emp[3])

    def save_click(self):
        status, message = self.controller.save(self.name.get(), self.family.get(), self.age.get())
        if status:
            msg.showinfo("Save", message)
            self.reset_form()
        else:
            msg.showerror("Save Error", message)

    def edit_click(self):
        status, message = self.controller.edit(self.id.get(), self.name.get(), self.family.get(), self.age.get())
        if status:
            msg.showinfo("Edit", message)
            self.reset_form()
        else:
            msg.showerror("Edit Error", message)


    def remove_click(self):
        if msg.askyesno("Remove Employee", "Are you sure?"):
            status, message = self.controller.remove(self.id.get())
            if status:
                msg.showinfo("Remove", message)
                self.reset_form()
            else:
                msg.showerror("Remove Error", message)

    def __init__(self):
        self.controller = EmployeeController()

        win = Tk()
        win.geometry("600x300")

        Label(win, text="Id").place(x=20, y=20)
        Label(win, text="Name").place(x=20, y=60)
        Label(win, text="Family").place(x=20, y=100)
        Label(win, text="Age").place(x=20, y=140)

        self.id = IntVar()
        self.name = StringVar()
        self.family = StringVar()
        self.age = IntVar()

        Entry(win, textvariable=self.id, state="readonly").place(x=80, y=20)
        Entry(win, textvariable=self.name).place(x=80, y=60)
        Entry(win, textvariable=self.family).place(x=80, y=100)
        Entry(win, textvariable=self.age).place(x=80, y=140)

        self.table = ttk.Treeview(win, columns=(1, 2, 3, 4), show="headings")
        self.table.place(x=250, y=20)

        self.table.heading(1, text="Id")
        self.table.heading(2, text="Name")
        self.table.heading(3, text="Family")
        self.table.heading(4, text="Age")

        self.table.column(1, width=60)
        self.table.column(2, width=100)
        self.table.column(3, width=100)
        self.table.column(4, width=60)

        self.table.bind("<ButtonRelease-1>", self.table_click)
        self.table.bind("<KeyRelease>", self.table_click)

        Button(win, text="Save", width=10, command=self.save_click).place(x=100, y=180)
        Button(win, text="Edit", width=10, command=self.edit_click).place(x=100, y=210)
        Button(win, text="Remove", width=10, command=self.remove_click).place(x=100, y=240)

        self.reset_form()

        win.mainloop()
