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
con.close()

def prideti_filma(kino_ID, kino_pavadinimas, isleidimo_data, kino_biudzetas, reitingas):
    kursorius.execute("INSERT INTO kinoteka VALUE (NUL, ?,?,?,?,?)", (kino_ID, kino_pavadinimas, isleidimo_data, kino_biudzetas, reitingas))
    con.commit()
    con.close()

def kinu_datos_perziura():
    kursorius.execute("SELECT * FROM kinoteka")
    viska = kursorius.fetchall()
    con.close()
    return viska

def istrinti_kino_data(id):
    kursorius.execute("DELETE FROM kinoteka WHERE id=?", (id))
    con.commit()
    con.close()

def redaguoti_kino_data(id, kino_ID="", kino_pavadinimas="", isleidimo_data="", kino_biudzetas="", reitingas=""):
    kursorius.execute("UPDATE kinoteka SET kino_ID=?, kino_pavadinimas=?, isleidimo_data=?, kino_biudzetas=?, reitingas=?, WHERE id=?",
    (kino_ID, kino_pavadinimas, isleidimo_data, kino_biudzetas, reitingas))
    con.commit()
    con.close()

