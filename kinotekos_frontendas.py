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

        # Funkcijos

        def iseiti():
            iseiti = tkinter.messagebox.askyesno("Tiketa", "Ar tikrai norite iseiti???")
            if iseiti>0:
                root.destroy()
            return

        def cleardata():
            self.txtkino_ID.delete(0,END)
            self.txtkino_pavadinimas.delete(0,END)
            self.txtisleidimo_data(0,END)
            self.txtkino_biudzetas(0,END)
            self.txtreitingas(0,END)

        def prideti_data():
            if(len(kino_ID.get())!=0):
                kinotekos_backendas.prideti_filma(
                    kino_ID.get(), 
                    kino_pavadinimas.get(),
                    isleidimo_data.get(),
                    kino_biudzetas.get(),
                    reitingas.get()
                )
                KinuSarasas.delete(0,END)

        # Frame'ai
        Pagrindinis_Fr=Frame(self.root, bg="black")
        Pagrindinis_Fr.grid()

        Virsutinis_Fr=Frame(Pagrindinis_Fr, bd=5, padx=54, pady=8, bg="black", relief=RIDGE)
        Virsutinis_Fr.pack(side=TOP)

        self.Virsutinis_Fr = Label(Virsutinis_Fr, font=("Arial", 51, "bold"), text="Kinoteatro Filmu Data", bg="black", fg="orange")
        self.Virsutinis_Fr.grid()

        Apatinis_Fr = Frame(Pagrindinis_Fr, bd=2, width=1300, height=400, padx=20, bg="black", relief=RIDGE)
        Apatinis_Fr.pack(side=BOTTOM)

        
        # Listbox'as ir Scrollbar'as

        sb=Scrollbar(DFrameR)
        sb.grid(row=0, column=1, sticky="ns")

