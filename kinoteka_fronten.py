#Frontend

from tkinter import *
import tkinter.messagebox
import kinotekos_backendas

class Kinas:
	def __init__(self, root):
		self.root=root
		self.root.title("Kino Bilietai")
		self.root.geometry("")
		self.root.config(bg="red")
		
		kino_pavadinimas=StringVar()
		kino_ID=StringVar()
		isleidimo_data=StringVar()
		kino_biudzetas=StringVar()
		reitingas=StringVar()

		#Fuctions
		def iExit():
			iExit=tkinter.messagebox.askyesno("Tiketa", "Ar tikrai norite iseiti???")
			if iExit>0:
				root.destroy()
			return

		def clcdata():
			self.txtkino_ID.delete(0,END)
			self.txtkino_pavadinimas.delete(0,END)
			self.txtisleidimo_data.delete(0,END)
			self.txtkino_biudzetas.delete(0,END)
			self.txtreitingas.delete(0,END)
			

		def adddata():
			if(len(kino_ID.get())!=0):
				kinotekos_backendas.pridet_filma(kino_ID.get(),kino_pavadinimas.get(),isleidimo_data.get(),kino_biudzetas.get(),reitingas.get())
				FilmuSarasas.insert(END,(kino_ID.get(),kino_pavadinimas.get(),isleidimo_data.get(),kino_biudzetas.get(),reitingas.get()))

		def disdata():
			FilmuSarasas.delete(0,END)
			for row in kinotekos_backendas.kinu_datos_perziura():
				FilmuSarasas.insert(END, row, str(""))

		def movierec(event):
			global sd
			searchmovie=FilmuSarasas.curselection()[0]
			sd=FilmuSarasas.get(searchmovie)

			self.txtkino_ID.delete(0,END)
			self.txtkino_ID.insert(END,sd[1])
			self.txtkino_pavadinimas.delete(0,END)
			self.txtkino_pavadinimas.insert(END,sd[2])
			self.txtisleidimo_data.delete(0,END)
			self.txtisleidimo_data.insert(END,sd[3])
			self.txtkino_biudzetas.delete(0,END)
			self.txtkino_biudzetas.insert(END,sd[4])
			self.txtreitingas.delete(0,END)
			self.txtreitingas.insert(END,sd[5])

		def deldata():
			if(len(kino_ID.get())!=0):
				kinotekos_backendas.istrinti_kino_data(sd[0])
				clcdata()
				disdata()

		def searchdb():
			FilmuSarasas.delete(0,END)
			for row in kinotekos_backendas.pasirinkti(kino_ID.get(),kino_pavadinimas.get(),isleidimo_data,kino_biudzetas.get(),reitingas.get()):
				FilmuSarasas.insert(END, row, str(""))

		def updata():
			if(len(kino_ID.get())!=0):
				kinotekos_backendas.istrinti_kino_data(sd[0])
			if(len(kino_ID.get())!=0):
				kinotekos_backendas.pridet_filma(kino_ID.get(),kino_pavadinimas.get(),isleidimo_data.get(),kino_biudzetas.get(),reitingas.get())
				FilmuSarasas.delete(0,END)
				FilmuSarasas.insert(END,(kino_ID.get(),kino_pavadinimas.get(),isleidimo_data.get(),kino_biudzetas.get(),reitingas.get()))

		#Frames
		MainFrame=Frame(self.root, bg="black")
		MainFrame.grid()

		TFrame=Frame(MainFrame, bd=5, padx=54, pady=8, bg="black", relief=RIDGE)
		TFrame.pack(side=TOP)

		self.TFrame=Label(TFrame, font=('Arial', 51, 'bold'), text="Kino Bilietu Data", bg="black", fg="orange")
		self.TFrame.grid() 

		BFrame=Frame(MainFrame, bd=2, width=1350, height=70, padx=18, pady=10, bg="orange", relief=RIDGE)
		BFrame.pack(side=BOTTOM)

		DFrame=Frame(MainFrame, bd=2, width=1300, height=400, padx=20, pady=20, bg="black", relief=RIDGE)
		DFrame.pack(side=BOTTOM)

		DFrameL=LabelFrame(DFrame, bd=2, width=1000, height=600, padx=20, bg="black", relief=RIDGE, font=('Arial', 20, 'bold'), text="Filmu Info_\n", fg="white")
		DFrameL.pack(side=LEFT)

		DFrameR=LabelFrame(DFrame, bd=2, width=450, height=300, padx=31, pady=3, bg="black", relief=RIDGE, font=('Arial', 20, 'bold'), text="Filmu Sablonas_\n", fg="white")
		DFrameR.pack(side=RIGHT)

		#Labels & Entry Box

		self.lblkino_ID=Label(DFrameL, font=('Arial', 18, 'bold'), text="Filmo ID:", padx=2, pady=2, bg="black", fg="orange")
		self.lblkino_ID.grid(row=0, column=0, sticky=W)
		self.txtkino_ID=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=kino_ID, width=39, bg="black", fg="white")
		self.txtkino_ID.grid(row=0, column=1) 

		self.lblkino_pavadinimas=Label(DFrameL, font=('Arial', 18, 'bold'), text="Filmo Pavadinimas:", padx=2, pady=2, bg="black", fg="orange")
		self.lblkino_pavadinimas.grid(row=1, column=0, sticky=W) 
		self.txtkino_pavadinimas=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=kino_pavadinimas, width=39, bg="black", fg="white")
		self.txtkino_pavadinimas.grid(row=1, column=1)

		self.lblisleidimo_data=Label(DFrameL, font=('Arial', 18, 'bold'), text="Isleidimo Data:", padx=2, pady=2, bg="black", fg="orange")
		self.lblisleidimo_data.grid(row=2, column=0, sticky=W) 
		self.txtisleidimo_data=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=isleidimo_data, width=39, bg="black", fg="white")
		self.txtisleidimo_data.grid(row=2, column=1)

		self.lblkino_biudzetas=Label(DFrameL, font=('Arial', 18, 'bold'), text="Biudzetas (Eurais):", padx=2, pady=2, bg="black", fg="orange")
		self.lblkino_biudzetas.grid(row=5, column=0, sticky=W) 
		self.txtkino_biudzetas=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=kino_biudzetas, width=39, bg="black", fg="white")
		self.txtkino_biudzetas.grid(row=5, column=1)

		self.lblreitingas=Label(DFrameL, font=('Arial', 18, 'bold'), text="Reitingas (Out of 5):", padx=2, pady=2, bg="black", fg="orange")
		self.lblreitingas.grid(row=7, column=0, sticky=W) 
		self.txtreitingas=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=reitingas, width=39, bg="black", fg="white")
		self.txtreitingas.grid(row=7, column=1)

		#ListBox & ScrollBar
		sb=Scrollbar(DFrameR)
		sb.grid(row=0, column=1, sticky='ns')

		FilmuSarasas=Listbox(DFrameR, width=41, height=16, font=('Arial', 12, 'bold'), bg="black", fg="white", yscrollcommand=sb.set)
		FilmuSarasas.bind('<<ListboxSelect>>', movierec)
		FilmuSarasas.grid(row=0, column=0, padx=8)
		sb.config(command=FilmuSarasas.yview)

		#Buttons
		self.btnadd=Button(BFrame, text="Prideti", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange", command=adddata)
		self.btnadd.grid(row=0, column=0)

		self.btndis=Button(BFrame, text="Rodyti", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange", command=disdata)
		self.btndis.grid(row=0, column=1)

		self.btnclc=Button(BFrame, text="Isvalyti", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange", command=clcdata)
		self.btnclc.grid(row=0, column=2)

		self.btnse=Button(BFrame, text="Ieskoti", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange", command=searchdb)
		self.btnse.grid(row=0, column=3)

		self.btndel=Button(BFrame, text="Istrinti", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange", command=deldata)
		self.btndel.grid(row=0, column=4)

		self.btnup=Button(BFrame, text="Atnaujinti", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange", command=updata)
		self.btnup.grid(row=0, column=5)

		self.btnx=Button(BFrame, text="Exit'as", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="orange", command=iExit)
		self.btnx.grid(row=0, column=6)


if __name__=='__main__':
	root=Tk()
	datbase=Kinas(root)
	root.mainloop()