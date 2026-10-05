from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# Wir starten unsere webanwendung mit FastAPI
app = FastAPI()


# # Die Startseite(wird aufgerufen, wenn die IP oder localhost aufgerufen wird)
# @app.get("/")
# def Startseite():
#     return {"Nachricht": "Willkommen auf der Startseite!"}

@app.get("/", response_class=HTMLResponse)
def startseite():
    html_inhalt = """
    <!DOCTYPE html>
    <html>
    <head><title>Startseite</title></head>
    <body>
        <h1>Willkommen auf meiner ersten Web-App!</h1>
        <p>Was möchtest du tun?</p>
        <ul>
            <!-- Der Link zur Eingabemaske -->
            <li><a href="/rechner">Zum Additions-Rechner wechseln</a></li>
        </ul>
        <p>Oder du kannst auch direkt auf Seite 1 gehen:</p>
        <ul>
            <li><a href="/seite1">Gehe zu Seite 1</a></li>
        </ul>
    </body>
    </html>
    """
    return html_inhalt

# Hier wird die Seite1 erstellt, die aufgerufen wird, wenn /Seite1 in der URL eingegeben wird
@app.get("/seite1", response_class=HTMLResponse)
def Seite1():
    html_inhalt = """
    <!DOCTYPE html>
    <html>
    <head><title>Startseite</title></head>
    <body>
        <h1>Willkommen auf meiner ersten angehängten Seite!</h1>
        <p>Hier ist ein Link zurück zur Startseite:</p>
        <ul>
            <li><a href="/">🏠 Zurück zur Startseite</a></li>
        </ul>        
    </body>
    </html>
    """
    return html_inhalt


# Hier wird die Seite2 erstellt, die aufgerufen wird, wenn /Seite2 in der URL eingegeben wird
# @app.get("/addieren")
# def addiere_zahlen(a: int, b: int):
#     ergebnis = a + b
#     return {"Status": "Rechnung erfolgreich",
#             "Aufgabe": f"{a} + {b}",
#             "Ergebnis": ergebnis
#             }

# Hier wird die Seite2 erstellt, die aufgerufen wird, wenn /Seite2 in der URL eingegeben wird
@app.get("/addieren", response_class=HTMLResponse)
def addiere_zahlen(a: int, b: int):
    # 1. Die Python-Logik (Rechnen)
    ergebnis = a + b
    
    # 2. Die visuelle Ausgabe (HTML mit eingefügten Variablen)
    html_inhalt = f"""
    <!DOCTYPE html>
    <html>
    <head><title>Ergebnis</title></head>
    <body>
        <h1>Das Ergebnis ist da!</h1>
        <p>Deine Aufgabe war: <b>{a} + {b}</b></p>
        <h2>Die Lösung lautet: <span style="color: green;">{ergebnis}</span></h2>
        
        <!-- Navigation zurück -->
        <div style="position: fixed; bottom: 20px; left: 20px;">
            <a href="/rechner">⬅ Nochmal rechnen</a>
        </div>
        <div style="position: fixed; bottom: 20px; left: 200px;">
            <a href="/">🏠 Zur Startseite</a>
        </div>
    </body>
    </html>
    """
    return html_inhalt

@app.get("/rechner", response_class=HTMLResponse)
def zeige_rechner():
    html_inhalt = """
    <!DOCTYPE html>
    <html>
    <head><title>Mein Web-Rechner</title></head>
    <body>
        <h1>Python Additions-Rechner</h1>
        <!-- Hier passiert die Magie: -->
        <form action="/addieren" method="get">
            <label>Zahl 1:</label>
            <input type="number" name="a" required><br><br>

            <label>Zahl 2:</label>
            <input type="number" name="b" required><br><br>

            <button type="submit">Berechnen</button>
        </form>
        <!-- Der Zurück-Link am unteren Bildschirmrand -->
        <div style="position: fixed; bottom: 20px; left: 20px;">
            <a href="/">🏠 Zur Startseite</a>
        </div>
    </body>
    </html>
    """
    return html_inhalt