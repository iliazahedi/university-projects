import tkinter as tk
from tkinter import messagebox, simpledialog

# bread-ha va gheymat
breads = {
    "sangak": 10000,
    "barbari": 8000,
    "lavash": 2000,
    "taftoon": 3000
}


class BakeryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Nanvaei")
        self.total_cost = 0
        self.shopping_list = []

        self.name = ""
        self.create_widgets()

    def create_widgets(self):
        # name
        tk.Label(self.root, text="Esme to chie:", font=(
            "Tahoma", 12)).grid(row=0, column=0, sticky="e")
        self.name_entry = tk.Entry(self.root, font=("Tahoma", 12))
        self.name_entry.grid(row=0, column=1)

        # shomare kart
        tk.Label(self.root, text="Shomare kart (16 ragham):", font=(
            "Tahoma", 12)).grid(row=1, column=0, sticky="e")
        self.card_entry = tk.Entry(self.root, font=("Tahoma", 12))
        self.card_entry.grid(row=1, column=1)

        # ramz
        self.password_btn = tk.Button(self.root, text="Ramz ro vared kon", font=(
            "Tahoma", 12), command=self.get_passwords)
        self.password_btn.grid(row=2, columnspan=2, pady=5)

        # noe nan
        tk.Label(self.root, text="Kodoom nan ro mikhay?", font=(
            "Tahoma", 12)).grid(row=3, column=0, sticky="e")
        self.bread_var = tk.StringVar(self.root)
        self.bread_var.set("sangak")
        tk.OptionMenu(self.root, self.bread_var, *
                      breads.keys()).grid(row=3, column=1)

        # tedad
        tk.Label(self.root, text="Tedad nan:", font=(
            "Tahoma", 12)).grid(row=4, column=0, sticky="e")
        self.count_entry = tk.Entry(self.root, font=("Tahoma", 12))
        self.count_entry.grid(row=4, column=1)

        # button ezafe kardan
        tk.Button(self.root, text="Ezafe be sabad", font=("Tahoma", 12),
                  command=self.add_to_cart).grid(row=5, columnspan=2, pady=5)

        # button payan
        tk.Button(self.root, text="Tamam shod, resido neshon bede", font=(
            "Tahoma", 12), command=self.show_receipt).grid(row=6, columnspan=2, pady=10)

    def get_passwords(self):
        self.name = self.name_entry.get().strip()
        card = self.card_entry.get().strip()

        if not self.name or not card or len(card) != 16 or not card.isdigit():
            messagebox.showerror(
                "Eshtebah", "Esm va shomare kart ro dorost vared kon!")
            return

        while True:
            pwd1 = simpledialog.askstring(
                "Ramz kart", "Ramz ro vared kon:", show="*")
            pwd2 = simpledialog.askstring(
                "Taeed ramz", "Dobare ramz ro vared kon:", show="*")
            if pwd1 == pwd2:
                messagebox.showinfo("Movafagh", "Ramz dorost bood.")
                break
            else:
                retry = messagebox.askretrycancel(
                    "Eshtebah", "Ramz ha yeki nistan! Dobare talash mikoni?")
                if not retry:
                    self.root.destroy()
                    return

    def add_to_cart(self):
        bread = self.bread_var.get()
        try:
            count = int(self.count_entry.get())
            if count <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Eshtebah", "Tedad bayad adade mosbat bashe.")
            return

        cost = count * breads[bread]
        self.total_cost += cost
        self.shopping_list.append((bread, count, cost))

        messagebox.showinfo(
            "Ezafe shod", f"{count} ta nan {bread} be gheymat {cost} toman ezafe shod.")
        self.count_entry.delete(0, tk.END)

        again = messagebox.askyesno("Edame?", "Baz ham nan mikhay?")
        if not again:
            self.show_receipt()

    def show_receipt(self):
        if not self.shopping_list:
            messagebox.showwarning("Kharid khaliye", "Hanooz chizi nakharidi!")
            return

        receipt = f"Reside kharid baraye {self.name}:\n\n"
        for item in self.shopping_list:
            receipt += f"{item[1]} ta nan {item[0]} = {item[2]} toman\n"
        receipt += f"\nMajmoo': {self.total_cost} toman"

        messagebox.showinfo("Reside", receipt)

        # zakhire dar file
        try:
            with open("receipt.txt", "w", encoding="utf-8") as f:
                f.write(receipt)
            messagebox.showinfo(
                "Zakhire shod", "Reside dar file 'receipt.txt' zakhire shod.")
        except Exception as e:
            messagebox.showerror("Error", f"File ro nashod zakhire konim: {e}")


# run barname
root = tk.Tk()
app = BakeryApp(root)
root.mainloop()
