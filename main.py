import tkinter as tk
from tkinter import ttk, messagebox
from ttkbootstrap import Style

class KasirRestoranGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Kasir Restoran Sederhana")

        style = Style(theme="vapor")  # Ganti tema sesuai keinginan (cth: vapor, flatly, dll.)

        # Ganti ukuran teks
        style.configure('.', font_size=12) 
        root.geometry('300x250')
        root.resizable(False, False)

        self.total_harga = 0

        # Membuat label
        self.label_menu = ttk.Label(root, text="Pilih Menu:")
        self.label_menu.grid(row=0, column=0, padx=10, pady=10)

        # Membuat opsi menu dengan varian Burger, Kebab, dan Kentang
        self.var_menu = tk.StringVar()
        self.var_menu.set("Burger")
        self.option_menu = ttk.Combobox(root, textvariable=self.var_menu, values=["Burger", "Kebab", "Kentang"])
        self.option_menu.grid(row=0, column=1, padx=10, pady=10)

        # Membuat label dan entry untuk jumlah pesanan
        self.label_jumlah = ttk.Label(root, text="Jumlah:")
        self.label_jumlah.grid(row=1, column=0, padx=10, pady=10)
        self.entry_jumlah = ttk.Entry(root)
        self.entry_jumlah.grid(row=1, column=1, padx=10, pady=10)

        # Membuat tombol untuk menambahkan pesanan
        self.btn_tambah = ttk.Button(root, text="Tambah Pesanan", command=self.tambah_pesanan)
        self.btn_tambah.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Membuat label untuk total harga
        self.label_total = ttk.Label(root, text="Total Harga: Rp 0")
        self.label_total.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def tambah_pesanan(self):
        try:
            jumlah_pesanan = int(self.entry_jumlah.get())
            menu_terpilih = self.var_menu.get()

            # Harga masing-masing menu
            harga_burger = 15000
            harga_kebab = 20000
            harga_kentang = 10000

            if menu_terpilih == "Burger":
                harga_pesanan = harga_burger * jumlah_pesanan
            elif menu_terpilih == "Kebab":
                harga_pesanan = harga_kebab * jumlah_pesanan
            elif menu_terpilih == "Kentang":
                harga_pesanan = harga_kentang * jumlah_pesanan
            else:
                messagebox.showerror("Error", "Menu tidak valid!")
                return

            self.total_harga += harga_pesanan
            self.label_total.config(text=f"Total Harga: Rp {self.total_harga}")

        except ValueError:
            messagebox.showerror("Error", "Masukkan jumlah pesanan dengan angka!")

if __name__ == "__main__":
    root = tk.Tk()
    app = KasirRestoranGUI(root)
    root.mainloop()
