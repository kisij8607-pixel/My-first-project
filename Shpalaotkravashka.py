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
    if not selectedfile:
        messagebox.showerror('Ошибка долбаеба', 'Ебанутый?Выбери файл')
        return
    try:
        print("архивация началась")
        sostoyanie['value'] = 0
        root.update()
        with zipfile.ZipFile(selectedfile + ".zip", 'w') as zipf:
            #50%
            sostoyanie['value'] = 50
            root.update()
            zipf.write(selectedfile)
            sostoyanie['value'] = 100
            root.update()
            messagebox.showinfo("Ура получилось,", f"Архив создан!\n{selectedfile}.zip")
            print(f"создан архив {selectedfile}.zip")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось:\n{str(e)}")
        sostoyanie['value'] = 0
tk.Button(root, text="НАЧАТЬ", command=zakryvashka).pack(pady=30)
sostoyanie = ttk.Progressbar(root, length=300, mode="determinate")
sostoyanie.pack(pady=30)
sostoyanie['value'] = 0
root.mainloop()
