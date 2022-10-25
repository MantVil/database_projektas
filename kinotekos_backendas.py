#backend
import sqlite3

con=sqlite3.connect("kinoteka.db") 
kursorius=con.cursor()

with con:
    kursorius.execute(
        """CREATE TABLE IF NOT EXISTS 
        kinoteka (
        id INTEGER PRIMARY KEY, 
        Movie_ID text,
        Movie_Name text,
        Release_Date text,
        Director text,
        Cast text,
        Budget text,
        Duration text,
        Rating text)"""
    )
con.commit()
con.close()
    
def pridet_filma(kino_ID,kino_pavadinimas,isleidimo_data,kino_biudzetas,reitingas):
    con=sqlite3.connect("kinoteka.db")    
    kursorius=con.cursor()
    kursorius.execute("INSERT INTO kinoteka VALUES (NULL, ?,?,?,?,?)", (kino_ID,kino_pavadinimas,isleidimo_data,kino_biudzetas,reitingas))
    con.commit()
    con.close()

def kinu_datos_perziura():
    con=sqlite3.connect("kinoteka.db")    
    kursorius=con.cursor()
    kursorius.execute("SELECT * FROM kinoteka")
    rows=kursorius.fetchall()
    con.close()    
    return rows

def istrinti_kino_data(id):    
    con=sqlite3.connect("kinoteka.db")    
    kursorius=con.cursor()
    kursorius.execute("DELETE FROM kinoteka WHERE id=?", (id,))
    con.commit()
    con.close()  

def pasirinkti(kino_ID="",kino_pavadinimas="",isleidimo_data="",kino_biudzetas="",reitingas=""):  
    con=sqlite3.connect("kinoteka.db")    
    kursorius=con.cursor()
    kursorius.execute("SELECT * FROM kinoteka WHERE kino_ID=? OR kino_pavadinimas=? OR isleidimo_data=? OR kino_biudzetas=? OR reitingas=?",(kino_ID,kino_pavadinimas,isleidimo_data,kino_biudzetas,reitingas))
    rows=kursorius.fetchall()
    con.close()    
    return rows

def atnaujinti(id,kino_ID="",kino_pavadinimas="",isleidimo_data="",kino_biudzetas="", reitingas=""):
    con=sqlite3.connect("kinoteka.db")    
    kursorius=con.cursor()
    kursorius.execute("UPDATE kinoteka SET kino_ID=?,kino_pavadinimas=?,isleidimo_data=?,kino_biudzetas=?, reitingas=?, WHERE id=?",(kino_ID,kino_pavadinimas,isleidimo_data,kino_biudzetas,reitingas))
    con.commit()
    con.close()

