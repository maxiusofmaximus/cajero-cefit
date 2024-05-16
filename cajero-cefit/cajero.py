from tkinter import *
from tkinter import messagebox
import os
import sqlite3
import asyncio
import time
from PyQt5 import QtWidgets
# from tkinter import ttk
# from PIL import Image, ImageTk

# Creando el directorio actual
def create_directory():
    directory = os.getcwd()
    list_directory = os.listdir('./cajero_venv/Lib/' + 'site-packages')
    return [directory, list_directory]

# Instalando PyQT
def know_installs():
    PyQt5_exist = False
    for listing in create_directory()[1]:
        if listing != 'PyQt5':
            PyQt5_exist = False
        else:
            PyQt5_exist = True
            break
    return PyQt5_exist

def install_PyQt5():
    os.system('pip install PyQt5')
    x = 1
    for i in range(x):
        time.sleep(1)
        if (know_installs() == False):
            x += 1
    return '\nPyQt5 Instalado\n'

# Conexión a la base de datos SQLite
# conn = sqlite3.connect('cajero.db')
# c = conn.cursor()

# Crear tabla de usuarios si no existe
# c.execute('''CREATE TABLE IF NOT EXISTS usuarios (username TEXT PRIMARY KEY, password TEXT, init_balance REAL)''')

class Cajero:
    def __init__(self, root):
        self.root = root
        
    def create_window(self):
        self.root.title("ATM New Horizons")
        self.root.iconbitmap(create_directory()[0] + "/cajero-cefit/img/favicon.ico")
        self.root.geometry("700x550")
        self.root.config(bg="white")
        self.root.resizable(False, False)
    
    def create_frame(self):
        self.marco = Frame(self.root)
        self.marco.grid(row=0, column=0)
        self.marco.config(width="700", height="85")
        self.marco.config(bg="#00278A")

    def create_label(self):
        self.label = Label(self.root)
        self.label.grid(row=0, column=0)
        self.label.config(text="ATM New Horizons", font=("Montserrat", 32, "bold"), bg="#00278A", fg="white")
    
    def create_canvas(self):
        self.canvas = Canvas(self.root, width="655", height="425", bg=self.root.cget("bg"), highlightthickness=0)
        self.canvas.grid(row=1, column=0, pady=20, padx=20, sticky=NW)

async def main():
    if know_installs() == False:
        installs = await asyncio.to_thread(install_PyQt5)
        print(installs)
    else:
        print("\nYa está instalado PyQt5\n")
    root = Tk()
    cajero = Cajero(root)
    cajero.create_window()
    cajero.create_frame()
    cajero.create_label()
    cajero.create_canvas()
    root.mainloop()

if __name__ == "__main__":
    asyncio.run(main())
    