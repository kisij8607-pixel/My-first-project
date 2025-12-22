import tarfile
import gzip
import os
import shutil
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import zipfile
root = tk.Tk()
root.title("Расшифратор")
root.geometry("800x600")
root.resizable(True, False)
tk.Label(root, text="Архиватор шпала").pack()
selectedfile = None
def open_file():
    filename = filedialog.askopenfilename(
        filetypes=[
            ("Изображение", "*.jpg *.jpeg *.png *.gif"),
            ("PDF файлы", "*.pdf"),
            ("Все файлы", "*.*")
        ]
    )
    global selectedfile
    if filename:
        selectedfile = filename
        print(f"Пользователь выбрал: {filename}")
        fileukaz.config(text=f"Выбран: {filename}")

tk.Button(root, text="архивируй свой пакет", command=open_file).pack()

fileukaz = tk.Label(root, text="Файл не выбран")
fileukaz.pack()
def zakryvashka():
    with zipfile.ZipFile(selectedfile + ".zip", 'w') as zipf:
        zipf.write(selectedfile)
tk.Button(root, text="НАЧАТЬ", command=zakryvashka).pack(pady=30)
root.mainloop()
