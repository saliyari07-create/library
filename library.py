import tkinter as tk
from tkinter import messagebox
import csv
import os

FILENAME = "books.csv"

if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "author", "count"])


def load_data():
    listbox.delete(0, tk.END)
    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            listbox.insert(
                tk.END,
                f"{row['name']} | {row['author']} | {row['count']}"
            )

def add_book():
    name = entry_name.get()
    author = entry_author.get()
    count = entry_count.get()

    if not name or not author or not count:
        messagebox.showerror("خطا", "همه فیلدها را پر کنید")
        return

    listbox.insert(tk.END, f"{name} | {author} | {count}")

    entry_name.delete(0, tk.END)
    entry_author.delete(0, tk.END)
    entry_count.delete(0, tk.END)

def delete_book():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
    except:
        messagebox.showwarning("خطا", "یک مورد را انتخاب کنید")

def save_data():
    with open(FILENAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "author", "count"])

        for i in range(listbox.size()):
            item = listbox.get(i)
            name, author, count = item.split(" | ")
            writer.writerow([name, author, count])

    messagebox.showinfo("موفق", "اطلاعات با موفقیت ذخیره شد")



root = tk.Tk()
root.title("فرم مدیریت کتاب")
root.geometry("500x400")

tk.Label(root, text="نام کتاب").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="نویسنده کتاب").pack()
entry_author = tk.Entry(root)
entry_author.pack()

tk.Label(root, text="تعداد کتاب").pack()
entry_count = tk.Entry(root)
entry_count.pack()

listbox = tk.Listbox(root, width=60)
listbox.pack(pady=10)

frame = tk.Frame(root)
frame.pack()

tk.Button(frame, text="Add", width=10, command=add_book).grid(row=0, column=0, padx=5)
tk.Button(frame, text="Delete", width=10, command=delete_book).grid(row=0, column=1, padx=5)
tk.Button(frame, text="Save", width=10, command=save_data).grid(row=0, column=2, padx=5)

load_data()
root.mainloop()