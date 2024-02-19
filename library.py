
import tkinter as tk
from tkinter import messagebox

class LibraryGUI:
    def __init__(self, master):
        self.master = master
        master.title("Kütüphane Uygulaması")

        self.lib = Library()

        self.label = tk.Label(master, text="*** MENÜ ***")
        self.label.pack()

        self.list_button = tk.Button(master, text="1) Kitapları Listele", command=self.list_books)
        self.list_button.pack()

        self.add_button = tk.Button(master, text="2) Kitap Ekle", command=self.add_book)
        self.add_button.pack()

        self.remove_button = tk.Button(master, text="3) Kitabı Kaldır", command=self.remove_book)
        self.remove_button.pack()

    def list_books(self):
        messagebox.showinfo("Kitaplar", self.lib.list_books())

    def add_book(self):
        title = input("Kitap Adı: ")
        author = input("Yazarı: ")
        year = input("Yayın Tarihi: ")
        pages = input("Sayfa Sayısı: ")
        self.lib.add_book(title, author, year, pages)
        messagebox.showinfo("Kitap Eklendi", "Kitap başarıyla eklendi.")

    def remove_book(self):
        title = input("Kaldırılacak Kitabın Adı: ")
        self.lib.remove_book(title)
        messagebox.showinfo("Kitap Kaldırıldı", "Kitap başarıyla kaldırıldı.")

class Library:
    def __init__(self):
        self.file_name = "kitaplar.txt"

    def open_file(self):
        self.file = open(self.file_name, "a+")

    def close_file(self):
        self.file.close()

    def list_books(self):
        self.open_file()
        self.file.seek(0)
        lines = self.file.readlines()
        book_list = []
        for line in lines:
            book_info = line.strip().split(',')
            book_list.append(f"Kitap Adı: {book_info[0]}, Yazarı: {book_info[1]}")
        self.close_file()
        return "\n".join(book_list)

    def add_book(self, title, author, year, pages):
        self.open_file()
        book_info = f"{title},{author},{year},{pages}\n"
        self.file.write(book_info)
        self.close_file()

    def remove_book(self, title):
        self.open_file()
        lines = self.file.readlines()
        new_lines = []
        for line in lines:
            if title not in line:
                new_lines.append(line)
        self.file.seek(0)
        self.file.truncate()
        self.file.writelines(new_lines)
        self.close_file()

def main():
    root = tk.Tk()
    app = LibraryGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
