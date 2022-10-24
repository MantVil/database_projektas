import sqlite3

con = sqlite3.connect("kinoteka.db")
kursorius = con.cursor()

kursorius.execute(""""
    CREATE TABLE IF NOT EXISTS
    kinoteka (id INTEGER PRIMARY KEY,
    kino_ID text,
    kino_Pavadinimas text,
    isleidimo_data text,
    kino_biudzetas text,
    Reitingas text)
    """
    )
con.commit()
con.close()