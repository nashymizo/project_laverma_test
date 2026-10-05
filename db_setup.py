import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect("fangbuch.db")

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create the "fische" table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS fische ( 
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        art TEXT,
        gewicht REAL,
        laenge REAL
    )
''')

# Insert sample data into the "fische" table
cursor.execute("INSERT INTO fische (name, art, gewicht, laenge) VALUES ('Hecht', 'Esox lucius', 5000, 120.5)")


