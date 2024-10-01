from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg

from controller.product_controller import ProductController
from view.component import LabelWithEntry, Table

class ProductView:

    def reset_form(self):
        self.id.set(0)
        self.name.set("")
        self.brand.set("")
        self.model.set("")
        self.barcode.set(0)
        self.buy_price.set(0)
        self.sell_price.set(0)

    def table_click(self, event):
        item_id = self.table.focus()
        item = self.table.item(item_id)
        pro = item["values"]
        self.id.set(pro[0])
        self.name.set(pro[1])
        self.brand.set(pro[2])
        self.model.set(pro[3])
        self.barcode.set(pro[4])
        self.buy_price.set(pro[5])
        self.sell_price.set(pro[6])

    def save_click(self):
        status, message =
        if status:
            msg.showinfo("Save", message)
            self.reset_form()
        else:
            msg.showerror("Save Error", message)

    def edit_click(self):
        status, message = self.controller.edit(
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
            status, message = self.controller.remove(self.id.get())
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
        self.brand = LabelWithEntry(win, "Brand", 20, 100)
        self.model = LabelWithEntry(win, "Model", 20, 140, data_type="int")
        self.barcode = LabelWithEntry(win, "barcode", 20, 180, data_type="int")
        self.buy_price = LabelWithEntry(win, "buy_price", 20, 220, data_type="int")
        self.sell_price = LabelWithEntry(win, "sell_price", 20, 260, data_type="int")


        Button(win, text="Save", width=10, command=self.save_click).place(x=100, y=180)
        Button(win, text="Edit", width=10, command=self.edit_click).place(x=100, y=210)
        Button(win, text="Remove", width=10, command=self.remove_click).place(x=100, y=240)

        self.reset_form()

        win.mainloop()


ui = ProductView()