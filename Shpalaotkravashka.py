import tarfile
import gzip
import os
import shutil
import tkinter as tk
import zipfile
from random import choice
from tkinter import ttk, messagebox, filedialog
root = tk.Tk()
root.title("Расшифратор")
root.geometry("800x600")
root.resizable(True, False)
tk.Label(root, text="Архиватор шпала").pack()
try:
    from PIL import Image, ImageTk
    try:
        img = Image.open("icon.png")
        photo = ImageTk.PhotoImage(img)
        root.iconphoto(False, photo)
        print("получилось с иконкой")
    except Exception as e:
        messagebox.showerror("ошибка","скачайте pillow")
except ImportError as e:
    print("скачай pip")
selectedfile = None
sap = None
def open_file():
    global selectedfile
    filename = filedialog.askopenfilename(
        filetypes=[
            ("Изображение", "*.jpg *.jpeg *.png *.gif"),
            ("PDF файлы", "*.pdf"),
            ("Все файлы", "*.*")
        ]
    )
    if filename:
        selectedfile = filename
        print(f"Пользователь выбрал: {filename}")
        fileukaz.config(text=f"Выбран: {filename}")
def ssf():
    global sap
    choice = messagebox.askquestion(
        "Куда сохранить файл?",
        "Сохранить рядом с исходным файлом\n(Нет в другую папку)"
    )
    if not selectedfile:
        messagebox.showwarning("Выбери сначало файл", "Файл Выбери")
        return
    if choice == "yes":
        sap = os.path.dirname(selectedfile)
    else:
        sap = filedialog.askdirectory()
tk.Button(root, text="архивируй свой пакет", command=open_file).pack()
tk.Button(root, text="Выбери куда надо", command=ssf,)
fileukaz = tk.Label(root, text="Файл не выбран")
fileukaz.pack()
def zakryvashka():
    global sap
    if not selectedfile:
        messagebox.showerror('Ошибка', 'Выбери файл')
        return
    try:
        print("архивация началась")
        if sap:
            folder = sap
        else:
            folder = os.path.dirname(selectedfile)
        sostoyanie['value'] = 0
        root.update()
        imya = os.path.basename(selectedfile)
        imyp = os.path.splitext(imya)[0]
        arch =os.path.join(folder, imyp + ".zip")
        with zipfile.ZipFile(arch, 'w', zipfile.ZIP_DEFLATED) as zip_ref:
            sostoyanie['value'] = 50
            root.update()
            zip_ref.write(selectedfile, imya)
            sostoyanie['value'] = 100
            root.update()
            messagebox.showinfo("Ура получилось,", f"Архив создан!\n{arch}")
            print(f"создан архив {selectedfile}")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось:\n{str(e)}")
        sostoyanie['value'] = 0
tk.Button(root, text="НАЧАТЬ", command=zakryvashka).pack(pady=30)
sostoyanie = ttk.Progressbar(root, length=300, mode="determinate")
sostoyanie.pack(pady=30)
sostoyanie['value'] = 0
root.mainloop()
