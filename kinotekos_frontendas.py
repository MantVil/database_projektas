from ast import Delete
from tkinter import *
import tkinter.messagebox
from tkinter.ttk import Labelframe
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
            self.txtisleidimo_data.delete(0,END)
            self.txtkino_biudzetas.delete(0,END)
            self.txtreitingas.delete(0,END)

        def prideti_data():
            if(len(kino_ID.get())!=0):
                kinotekos_backendas.prideti_filma(
                    kino_ID.get(), 
                    kino_pavadinimas.get(),
                    isleidimo_data.get(),
                    kino_biudzetas.get(),
                    reitingas.get()
                )
                FilmuSarasas.delete(0,END)
                FilmuSarasas.insert(END,(kino_ID.get(), kino_pavadinimas.get(), isleidimo_data.get(), kino_biudzetas.get(), reitingas.get()))

        # Frame'ai
        Pagrindinis_Fr=Frame(self.root, bg="black")
        Pagrindinis_Fr.grid()

        Virsutinis_Fr=Frame(Pagrindinis_Fr, bd=5, padx=54, pady=8, bg="black", relief=RIDGE)
        Virsutinis_Fr.pack(side=TOP)

        self.Virsutinis_Fr = Label(Virsutinis_Fr, font=("Arial", 51, "bold"), text="Kinoteatro Filmu Data", bg="black", fg="orange")
        self.Virsutinis_Fr.grid()

        Apatinis_Fr = Frame(Pagrindinis_Fr, bd=2, width=1350, height=70, padx=18, pady=10, bg="green", relief=RIDGE)
        Apatinis_Fr.pack(side=BOTTOM)

        Vidinis_Fr = Frame(Pagrindinis_Fr, bd=2, width=1300, height=400, padx=20, pady=20, bg="black", relief=RIDGE)
        Vidinis_Fr.pack(side=BOTTOM)

        Vidinis_FrL = LabelFrame(Vidinis_Fr, bd=2, width=1000, height=600,padx=20, bg="black", relief=RIDGE, font=("Arial", 20, "bold"), text="Kinu Info_\n",fg="white")
        Vidinis_FrL.pack(side=LEFT)

        Vidinis_FrR = Labelframe(Vidinis_Fr, bd=2, width=450, height=300, padx=31, pady=3, bg="black", relief=RIDGE, font=("Arial", 20, "bold"), text="Kinu Smulki Info_\n", fg="white")
        Vidinis_FrR.pack(side=RIGHT)

        # Label'iai ir Entry boxai

        self.lblkino_ID=Label(Vidinis_FrL, font=('Arial', 18, 'bold'), text="Filmo ID: ", padx=2, pady=2, bg="black", fg="orange")
        self.lblkino_ID.grid(row=0, column=0, sticky=W)
        self.txtkino_ID=Entry(Vidinis_FrL, font=('Arial', 18, 'bold'), textvariable=kino_ID, width=39, bg="black", fg="white")
        self.txtkino_ID.grid(row=0, column=1) 

        self.lblkino_pavadinimas=Label(Vidinis_FrL, font=('Arial', 18, 'bold'), text="Filmo Pavadinimas:", padx=2, pady=2, bg="black", fg="orange")
        self.lblkino_pavadinimas.grid(row=1, column=0, sticky=W) 
        self.txtkino_pavadinimas=Entry(Vidinis_FrL, font=('Arial', 18, 'bold'), textvariable=kino_pavadinimas, width=39, bg="black", fg="white")
        self.txtkino_pavadinimas.grid(row=1, column=1)

        self.lblisleidimo_data=Label(Vidinis_FrL, font=('Arial', 18, 'bold'), text="Isleidimo Data:", padx=2, pady=2, bg="black", fg="orange")
        self.lblisleidimo_data.grid(row=2, column=0, sticky=W) 
        self.txtisleidimo_data=Entry(Vidinis_FrL, font=('Arial', 18, 'bold'), textvariable=isleidimo_data, width=39, bg="black", fg="white")
        self.txtisleidimo_data.grid(row=2, column=1)

        self.lblkino_biudzetas=Label(Vidinis_FrL, font=('Arial', 18, 'bold'), text="Biudzetas (Eurais): ", padx=2, pady=2, bg="black", fg="orange")
        self.lblkino_biudzetas.grid(row=5, column=0, sticky=W) 
        self.txtkino_biudzetas=Entry(Vidinis_FrL, font=('Arial', 18, 'bold'), textvariable=kino_biudzetas, width=39, bg="black", fg="white")
        self.txtkino_biudzetas.grid(row=5, column=1)

        self.lblreitingas=Label(Vidinis_FrL, font=('Arial', 18, 'bold'), text="Reitingas (Out of 5):", padx=2, pady=2, bg="black", fg="orange")
        self.lblreitingas.grid(row=7, column=0, sticky=W) 
        self.txtreitingas=Entry(Vidinis_FrL, font=('Arial', 18, 'bold'), textvariable=reitingas, width=39, bg="black", fg="white")
        self.txtreitingas.grid(row=7, column=1)


        # Listbox'as ir Scrollbar'as
        sb=Scrollbar(Vidinis_FrR)
        sb.grid(row=0, column=1, sticky='ns')

        FilmuSarasas=Listbox(Vidinis_FrR, width=41, height=16, font=('Arial', 12, 'bold'), bg="black", fg="white", yscrollcommand=sb.set)
        FilmuSarasas.bind('<<Sarasas>>', movierec)
        FilmuSarasas.grid(row=0, column=0, padx=8)
        sb.config(command=FilmuSarasas.yview)
        
        #Buttons
		
        self.btnadd=Button(Apatinis_Fr, text="Prideti Nauja", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange", command=prideti_data)
        self.btnadd.grid(row=0, column=0)

        self.btndis=Button(Apatinis_Fr, text="Rodyti Visus", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange")
        self.btndis.grid(row=0, column=1)

        self.btnclc=Button(Apatinis_Fr, text="Isvalyti", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange")
        self.btnclc.grid(row=0, column=2)

        self.btndel=Button(Apatinis_Fr, text="Istrinti", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange")
        self.btndel.grid(row=0, column=4)

        self.btnup=Button(Apatinis_Fr, text="Atnaujinti", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange")
        self.btnup.grid(row=0, column=5)

        self.btnx=Button(Apatinis_Fr, text="Isjungti Programa", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange", command=iseiti)
        self.btnx.grid(row=0, column=6)
        

if __name__ == "__main__":
    root=Tk()
    datbase=Kinas(root)
    root.mainloop()