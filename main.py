from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

# Wir starten unsere webanwendung mit FastAPI
app = FastAPI()

# Wir sagen FastAPI, dass wir Jinja2 als Template-Engine verwenden und die Templates im Ordner "templates" liegen
templates = Jinja2Templates(directory="templates")


@app.get("/rechner")
def zeige_rechner(request: Request):
    # Wir rendern die HTML-Datei "rechner.html" und übergeben das Request-Objekt
    return templates.TemplateResponse(request, "rechner.html")


@app.get("/seite1")
def zeige_seite1(request: Request):
    # Wir rendern die HTML-Datei "seite1.html" und übergeben das Request-Objekt
    return templates.TemplateResponse(request, "seite1.html")

@app.get("/")
def startseite(request: Request):
    # Wir rendern die HTML-Datei "startseite.html" und übergeben das Request-Objekt
    return templates.TemplateResponse(request, "startseite.html")

@app.get("/addieren")
def addiere_zahlen(request: Request, a: int, b: int):
    # Die eigentliche Logik
    ergebnis = a + b
    
    # Wir rufen das Template auf und füttern es mit unseren Variablen
    return templates.TemplateResponse(request, "ergebnis.html", {
        "request": request,
        "zahl1": a,
        "zahl2": b,
        "loesung": ergebnis
    })

@app.get("/bootstrap")
def zeige_bootstrap(request: Request):
    return templates.TemplateResponse(request, "bootstrap.html")

@app.get("/ueberMich")
def zeige_ueber_mich(request: Request):
    return templates.TemplateResponse(request, "ueberMich.html")