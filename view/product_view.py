from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg

from controller.product_controller import ProductController
from view.component import LabelWithEntry, Table

class ProductView:
    def resat_form(self):
        self.id.set(0)
        self.name.set("")
        self.brand.set("")
        self.model.set("")
        self.barcode.set(0)
        self.buy_price.set(0)
        self.sell_price.set(0)


    def table_click(self, selected_item):
        print(selected_item)

    def save_click(self):
        status, message =  ProductController.save(
            self.id.get(),
            self.name.get(),
            self.brand.get(),
            self.model.get(),
            self.barcode.get(),
            self.buy_price.get(),
            self.sell_price.get())
        if status:
            msg.showinfo("Save", message)
            self.reset_form()
        else:
            msg.showerror("Save Error", message)

    def edit_click(self):
        status, message = ProductController.edit(
            self.id.get(),
            self.name.get(),
            self.brand.get(),
            self.model.get(),
            self.barcode.get(),
            self.buy_price.get(),
            self.sell_price.get())
        if status:
            msg.showinfo("Edit", message)
            self.reset_form()
        else:
            msg.showerror("Edit Error", message)


    def remove_click(self):
        if msg.askyesno("Remove product", "Are you sure?"):
            status, message = ProductController.remove(self.id.get())
            if status:
                msg.showinfo("Remove", message)
                self.reset_form()
            else:
                msg.showerror("Remove Error", message)

    def __init__(self):
        self.controller = ProductController()

        win = Tk()
        win.geometry("600x300")

        Label(win, text="Id").place(x=20, y=20)
        Label(win, text="Name").place(x=20, y=60)
        Label(win, text="brand").place(x=20, y=100)
        Label(win, text="model").place(x=20, y=140)
        Label(win, text="barcode").place(x=20, y=180)
        Label(win, text="buy_price").place(x=20, y=220)
        Label(win, text="sell_price").place(x=20, y=260)


        self.id = IntVar()
        self.name = StringVar()
        self.brand = StringVar()
        self.model = StringVar()
        self.barcode = IntVar()
        self.buy_price = IntVar()
        self.sell_price = IntVar()

        Entry(win, textvariable=self.id, state="readonly").place(x=80, y=20)
        Entry(win, textvariable=self.name).place(x=80, y=60)
        Entry(win, textvariable=self.brand).place(x=80, y=100)
        Entry(win, textvariable=self.model).place(x=80, y=140)
        Entry(win, textvariable=self.barcode).place(x=80, y=140)
        Entry(win, textvariable=self.buy_price).place(x=80, y=140)
        Entry(win, textvariable=self.sell_price).place(x=80, y=140)


        self.table = ttk.Treeview(win, columns=(1, 2, 3, 4), show="headings")
        self.table.place(x=250, y=20)

        self.table.heading(1, text="Id")
        self.table.heading(2, text="Name")
        self.table.heading(3, text="Brand")
        self.table.heading(4, text="Model")
        self.table.heading(1, text="Barcode")
        self.table.heading(2, text="buy_price")
        self.table.heading(3, text="sell_price")


        self.table.column(1, width=60)
        self.table.column(2, width=100)
        self.table.column(3, width=100)
        self.table.column(4, width=60)
        self.table.column(1, width=60)
        self.table.column(2, width=100)
        self.table.column(3, width=100)


        self.table.bind("<ButtonRelease-1>", self.table_click)
        self.table.bind("<KeyRelease>", self.table_click)

        Button(win, text="Save", width=10, command=self.save_click).place(x=100, y=180)
        Button(win, text="Edit", width=10, command=self.edit_click).place(x=100, y=210)
        Button(win, text="Remove", width=10, command=self.remove_click).place(x=100, y=240)

        self.reset_form()

        win.mainloop()

    def reset_form(self):
        pass


ui = ProductView()