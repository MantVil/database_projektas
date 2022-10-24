import sqlite3


con = sqlite3.connect("kinoteka.db")
kursorius = con.cursor()

kursorius.execute("""
    CREATE TABLE IF NOT EXISTS
    kinoteka (id INTEGER PRIMARY KEY,
    kino_ID text,
    kino_pavadinimas text,
    isleidimo_data text,
    kino_biudzetas text,
    reitingas text)
    """
    )
con.commit()

def prideti_filma(kino_ID, kino_pavadinimas, isleidimo_data, kino_biudzetas, reitingas):
    kursorius.execute("INSERT INTO kinoteka VALUES (NULL, ?,?,?,?,?)", (kino_ID, kino_pavadinimas, isleidimo_data, kino_biudzetas, reitingas))
    con.commit()
    
    
def kinu_datos_perziura():
    kursorius.execute("SELECT * FROM kinoteka")
    viska = kursorius.fetchall()
    
    return viska

def istrinti_kino_data(id):
    kursorius.execute("DELETE FROM kinoteka WHERE id=?", (id))
    con.commit()
    
def pasirinkti(kino_ID="", kino_pavadinimas="", isleidimo_data="", kino_biudzetas="", reitingas=""):  
    kursorius.execute("SELECT * FROM kinotekas WHERE kino_ID=? OR kino_pavadinimas=? OR isleidimo_data=? OR kino_biudzetas=? OR reitingas=?",(kino_ID, kino_pavadinimas , isleidimo_data, kino_biudzetas , reitingas))
    rows= kursorius.fetchall()   
    return rows

def redaguoti_kino_data(id, kino_ID="", kino_pavadinimas="", isleidimo_data="", kino_biudzetas="", reitingas=""):
    kursorius.execute("UPDATE kinoteka SET kino_ID=?, kino_pavadinimas=?, isleidimo_data=?, kino_biudzetas=?, reitingas=?, WHERE id=?",
    (kino_ID, kino_pavadinimas, isleidimo_data, kino_biudzetas, reitingas))
    con.commit()
    
