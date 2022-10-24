from tkinter import *
import tkinter.messagebox
import kinotekos_backendas

class Kinas():
    def __init__(self, root):
        self.root = root
        self.root.title("Tiketa")
        self.root.geometry("")
        self.root.config(bg = "black")

        kino_pavadinimas=StringVar()
        kino_ID=StringVar()
        isleidimo_data=StringVar()
        kino_biudzetas=StringVar()
        reitingas=StringVar()

        def iseiti():
            iseiti = tkinter.messagebox.askyesno("Tiketa", "Ar tikrai norite iseiti???")
            if iseiti>0:
                root.destroy()
            return
