from datetime import datetime
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

        self.id = LabelWithEntry(win, text="Id", x=20, y=100, data_type="int", state= "readonly")
        self.account = LabelWithEntry(win, text="Account", x=20, y=20, data_type= "str")
        self.amount = LabelWithEntry(win, text="Amount", x=20, y=60, data_type= "int")
        self.date = LabelWithEntry(win, text="Date", x=20, y=140, data_type= "datetime", state= "readonly")
        self.person = LabelWithEntry(win, text="Person", x=20, y=180, data_type= "str")

        self.table = Table(win, ["Id", "Account", "Amount", "Date", "Person"],[60, 100, 100, 60, 60], 250, 20, self.table_click)
        self.table.refresh_table(PaymentController.find_all()[1])

        self.table = ttk.Treeview(win, columns=(1, 2, 3, 4, 5), show="headings")
        self.table.place(x=250, y=20)


        Button(win, text="Save", command=self.save_record).place(x=100, y=220)
        Button(win, text="Remove", command=self.remove_record).place(x=100, y=250)
        Button(win, text="Edit", command=self.edit_record).place(x=100, y=280)

        self.reset_form()

        win.mainloop()
