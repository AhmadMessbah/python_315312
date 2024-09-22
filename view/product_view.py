from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg

from controller.product_controller import productController

class productView:
    def clear_table(self):
        for item in self.table.get_children():
            self.table.delete(item)

    def show_on_table(self):
        for product in self.controller.find_all():
            self.table.insert("", END, values=product.to_tuple())

    def reset_form(self):
        self.id.set(0)
        self.name.set("")
        self.brand.set("")
        self.model.set("")
        self.barcode.set(0)
        self.buy_price.set(0)
        self.sell_price.set(0)
        self.clear_table()
        self.show_on_table()

    def table_click(self, event):
        item_id = self.table.focus()
        item = self.table.item(item_id)
        emp = item["values"]
        self.id.set(pro[0])
        self.name.set(pro[1])
        self.brand.set(pro[2])
        self.model.set(pro[3])
        self.barcode.set(pro[2])
        self.sell_price.set(pro[2])
        self.buy_price.set(pro[2])

    def save_click(self):
        status, message = self.controller.save(
            self.id.get(pro[0]),
            self.name.get(pro[1]),
            self.brand.get(pro[2]),
            self.model.get(pro[3]),
            self.barcode.get(pro[2]),
            self.sell_price.get(pro[2]),
            self.buy_price.get(pro[2]),
        )
        if status:
            msg.showinfo("Save", message)
            self.reset_form()
        else:
            msg.showerror("Save Error", message)

    def edit_click(self):
        status, message = self.controller.edit(
            self.id.get(pro[0]),
            self.name.get(pro[1]),
            self.brand.get(pro[2]),
            self.model.get(pro[3]),
            self.barcode.get(pro[2]),
            self.sell_price.get(pro[2]),
            self.buy_price.get(pro[2]),)
        if status:
            msg.showinfo("Edit", message)
            self.reset_form()
        else:
            msg.showerror("Edit Error", message)


    def remove_click(self):
        if msg.askyesno("Remove product", "Are you sure?"):
            status, message = self.controller.remove(self.id.get())
            if status:
                msg.showinfo("Remove", message)
                self.reset_form()
            else:
                msg.showerror("Remove Error", message)

    def __init__(self):
        self.controller = productController()

        win = Tk()
        win.geometry("600x300")

        Label(win, text="Id").place(x=20, y=20)
        Label(win, text="Name").place(x=20, y=60)
        Label(win, text="brand").place(x=20, y=100)
        Label(win, text="model").place(x=20, y=140)
        Label(win, text="barcode").place(x=20, y=180)
        Label(win, text="buy_price").place(x=20, y=220)
        Label(win, text="sell_price").place(x=20, y=10)


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