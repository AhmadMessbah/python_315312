from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg

from controller.payment_controller import PaymentController
from view.component import LabelWithEntry, Table

class PaymentView:

    def reset_form(self):
        self.id.set(0)
        self.account.set("")
        self.amount.set(0)
        self.date.set("")
        self.person.set("")

    @staticmethod
    def table_click(selected_item):
        print(selected_item)

    def save_record(self):
        status, message = PaymentController.save(self.account.get(), self.amount.get(), self.person.get())
        if status:
            msg.showinfo("Saved.", message)
            self.reset_form()
        else:
            msg.showerror("Save Error!", message)

    def remove_record(self):
        if msg.askyesno("Remove Payment!", "Are you sure?"):
            status, message = PaymentController.remove(self.id.get())
            if status:
                msg.showinfo("Removed.", message)
                self.reset_form()
            else:
                msg.showerror("Remove Error!", message)

    def edit_record(self):
        status, message = PaymentController.edit(self.id.get(), self.account.get(), self.amount.get(), self.person.get())
        if status:
            msg.showinfo("Edited.", message)
            self.reset_form()
        else:
            msg.showerror("Edit Error!", message)


    def __init__(self):
        win = Tk()
        win.geometry("650x400")

        Label(win, text="account").place(x=20, y=20)
        Label(win, text="amount").place(x=20, y=60)
        Label(win, text="id").place(x=20, y=100)
        Label(win, text="date").place(x=20, y=140)
        Label(win, text="person").place(x=20, y=180)

        self.account = StringVar()
        self.amount = IntVar()
        self.id = IntVar()
        self.date = StringVar()
        self.person = StringVar()

        Entry(win, textvariable=self.account).place(x=80, y=20)
        Entry(win, textvariable=self.amount).place(x=80, y=60)
        Entry(win, textvariable=self.id).place(x=80, y=100)
        Entry(win, textvariable=self.date).place(x=80, y=140)
        Entry(win, textvariable=self.person).place(x=80, y=180)

        self.table = ttk.Treeview(win, columns=(1, 2, 3, 4, 5), show="headings")
        self.table.place(x=250, y=20)

        self.table.heading(1, text="Id")
        self.table.heading(2, text="account")
        self.table.heading(3, text="amount")
        self.table.heading(4, text="person")
        self.table.heading(5, text="dete")

        self.table.column(1, width=60)
        self.table.column(2, width=100)
        self.table.column(3, width=100)
        self.table.column(4, width=60)
        self.table.column(5, width=60)

        self.table.bind("<ButtonRelease-1>", self.table_focus)

        Button(win, text="Save", command=self.save_record).place(x=100, y=220)
        Button(win, text="Remove", command=self.remove_record).place(x=100, y=250)
        Button(win, text="Edit", command=self.edit_record).place(x=100, y=280)

        self.reset_form()

        win.mainloop()
