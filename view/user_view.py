from tkinter import *
import tkinter as ttk
import tkinter.messagebox as msg

from controller.user_controller import UserController


class UserView:
    def clear_table(self):
        for item in self.table.get_id():
            self.table.delete(item)

    def show_on_table(self):
        for user in self.controller.find_all():
            self.table.insert("", END, values=user.to_tuple())

    def reset_form(self):
        self.id.set(0)
        self.name.set("")
        self.family.set("")
        self.birth_date.set(0)
        self.username.set("")
        self.password.set("")
        self.clear_table()
        self.show_on_table()

    def table_click(self, event):
        item_id = self.table.focus()
        item = self.table.item(item_id)
        emp = item["values"]
        self.id.set()
        self.name.set()
        self.family.set()
        self.birth_date.set()
        self.username.set()
        self.password.set()

    def save_click(self):
        status, message = self.controller.save(self.name.get(), self.family.get(), self.birth_date.get(),
                                               self.username.get(), self.password.get())
        if status:
            msg.showinfo("Save", message)
            self.reset_form()
        else:
            msg.showerror("Save Error", message)

    def edit_click(self):
        status, message = self.controller.edit(self.id.get(), self.name.get(), self.family.get(), self.birth_date.get(),
                                               self.username.get(), self.password.get())
        if status:
            msg.showinfo("Edit", message)
            self.reset_form()
        else:
            msg.showerror("Edit Error", message)

    def remove_click(self):
        if msg.askyesno("Remove user", "Are you sure?"):
            status, message = self.controller.remove(self.id.get())
            if status:
                msg.showinfo("Remove", message)
                self.reset_form()
            else:
                msg.showerror("Remove Error", message)

    def __init__(self):
        self.controller = UserController()

        self.win = Tk()
        self.win.geometry("400x400")
        Label(self.win, text="Id").place(x=20, y=20)
        Label(self.win, text="Name").place(x=80, y=20)
        Label(self.win, text="Family").place(x=140, y=20)
        Label(self.win, text="Birth_Date").place(x=200, y=20)
        Label(self.win, text="username").place(x=260, y=20)
        Label(self.win, text="password").place(x=320, y=20)

        self.id = IntVar()
        self.name = StringVar()
        self.family = StringVar()
        self.birth_date = StringVar()
        self.username = StringVar()
        self.password = StringVar()

        Entry(self.win, textvariable=self.id, state="readonly", width=20).place(x=20, y=40)
        Entry(self.win, textvariable=self.name, width=20).place(x=20, y=80)
        Entry(self.win, textvariable=self.family, width=20).place(x=20, y=120)
        Entry(self.win, textvariable=self.birth_date, width=20).place(x=20, y=160)
        Entry(self.win, textvariable=self.username, width=20).place(x=20, y=200)
        Entry(self.win, textvariable=self.password, width=20).place(x=20, y=240)

        self.table = ttk.Treeview(self.win, columns=(1, 2, 3, 4), show="headings")
        self.table.place(x=250, y=20)

        self.table.heading(1, text="Id")
        self.table.heading(2, text="Name")
        self.table.heading(3, text="Family")
        self.table.heading(4, text="Birth_Date")
        self.table.heading(5, text="username")
        self.table.heading(6, text="password")

        self.table.column(1, width=40)
        self.table.column(2, width=80)
        self.table.column(3, width=80)
        self.table.column(4, width=40)
        self.table.column(5, width=50)
        self.table.column(6, width=110)

        self.table.bind("<ButtonRelease-1>", self.table_click)
        self.table.bind("<KeyRelease>", self.table_click)

        Button(self.win, text="Save", width=10, command=self.save_click).place(x=20, y=250)
        Button(self.win, text="Edit", width=10, command=self.edit_click).place(x=60, y=250)
        Button(self.win, text="Remove", width=10, command=self.remove_click).place(x=100, y=250)

        self.win.mainloop()
