import tkinter
import tkinter.constants
import tkinter.ttk as ttk


class PaymentView:

    def reset_form(self):
        self.account.set("")
        self.amount.set(0)
        self.id.set(0)
        self.date.set("")
        self.person.set("")

    def save_record(self):
        id_value = self.id.get()
        account_value = self.account.get()
        amount_value = self.amount.get()
        date_value = self.date.get()
        person_value = self.person.get()

        if id_value and account_value:
            self.table.insert('', 'end', values=(id_value, account_value, amount_value, person_value, date_value))
            self.reset_form()

    def table_focuse(self, event):
        selected = self.table.focus()
        values = self.table.item(selected, 'values')
        if values:
            self.id.set(values[0])
            self.account.set(values[1])
            self.amount.set(values[2])
            self.person.set(values[3])
            self.date.set(values[4])

    def remove_record(self):
        selected = self.table.focus()
        if selected:
            self.table.delete(selected)
            self.reset_form()

    def edit_record(self):
        selected = self.table.focus()
        if selected:
            self.table.delete(selected)

            id_value = self.id.get()
            account_value = self.account.get()
            amount_value = self.amount.get()
            date_value = self.date.get()
            person_value = self.person.get()

            if id_value and account_value:
                self.table.insert('', 'end', values=(id_value, account_value, amount_value, person_value, date_value))
                self.reset_form()

    def __init__(self):

        win = tkinter.Tk()
        win.geometry("550x300")

        tkinter.Label(win, text="account").place(x=20, y=20)
        tkinter.Label(win, text="amount").place(x=20, y=60)
        tkinter.Label(win, text="id").place(x=20, y=100)
        tkinter.Label(win, text="date").place(x=20, y=140)
        tkinter.Label(win, text="person").place(x=20, y=180)

        self.account = tkinter.StringVar()
        self.amount = tkinter.IntVar()
        self.id = tkinter.IntVar()
        self.date = tkinter.StringVar()
        self.person = tkinter.StringVar()

        tkinter.Entry(win, textvariable=self.account).place(x=80, y=20)
        tkinter.Entry(win, textvariable=self.amount).place(x=80, y=60)
        tkinter.Entry(win, textvariable=self.id).place(x=80, y=100)
        tkinter.Entry(win, textvariable=self.date).place(x=80, y=140)
        tkinter.Entry(win, textvariable=self.person).place(x=80, y=180)

        self.table = ttk.Treeview(win, columns=(1, 2, 3, 4, 5), show="headings")
        self.table.place(x=250, y=20)

        self.table.heading(1, text="Id")
        self.table.heading(2, text="account")
        self.table.heading(3, text="amount")
        self.table.heading(4, text="person")
        self.table.heading(4, text="dete")

        self.table.column(1, width=60)
        self.table.column(2, width=100)
        self.table.column(3, width=100)
        self.table.column(4, width=60)
        self.table.column(5, width=60)

        self.table.bind("<ButtonRelease-1>", self.table_focuse)

        tkinter.Button(win, text="Save", command=self.save_record).place(x=100, y=180)
        tkinter.Button(win, text="Remove", command=self.remove_record).place(x=100, y=210)
        tkinter.Button(win, text="Edit", command=self.edit_record).place(x=100, y=240)

        self.reset_form()

        win.mainloop()  #
