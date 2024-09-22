from tkinter import *

from dateutil.tz import win


class UserView:
    def __init__(self):















        self.win = Tk()
        win.geometry("400x400")
        Label.(win, text="Id").place(x=20, y=20)
        label.(win, text="Name").place(x=20, y=50)
        label.(win, text="Family").place(x=20, y=80)
        label.(win, text="Birth_Date").place(x=20, y=110)
        label.(win, text="username").place(x=20, y=140)
        Label.(win, text="password").place(x=20, y=160)
        label.(win, text="active").place(x=20, y=160)


        self.id = IntVar()
        self.name = StringVar()
        self.family = StringVar()
        self.birth_date = StringVar()
        self.username = StringVar()
        self.password = StringVar()

        Entry(win, textvariable=self.id,state="readonly", width=20).place(x=20, y=40)
        Entry(win, textvariable=self.name, width=20).place(x=20, y=80)
        Entry(win, textvariable=self.family, width=20).place(x=20, y=120)
        Entry(win, textvariable=self.birth_date, width=20).place(x=20, y=160)
        Entry(win, textvariable=self.username, width=20).place(x=20, y=200)
        Entry(win, textvariable=self.password, width=20).place(x=20, y=240)
        Radiobutton.(win, text="is_active").place(x=20, y=200)
        Radiobutton.(win, text="is_not_active").place(x=60, y=200)

        self.table = ttk.Treeview(win, columns=(1, 2, 3, 4), show="headings")
        self.table.place(x=250, y=20)

        self.table.heading(1, text="Id")
        self.table.heading(2, text="Name")
        self.table.heading(3, text="Family")
        self.table.heading(4, text="Birth_Date")
        self.table.heading(5, text="username")
        self.table.heading(6, text="password")
        self.table.heading(7, text="active")







        self.table.column(1, width=60)
        self.table.column(2, width=100)
        self.table.column(3, width=100)
        self.table.column(4, width=60)

        Button(win, text="Save", width=10, command=self.save_click).place(x=100, y=180)
        Button(win, text="Edit", width=10, command=self.edit_click).place(x=100, y=210)
        Button(win, text="Remove", width=10, command=self.remove_click).place(x=100, y=240)












        self.win.mainloop()


