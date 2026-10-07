from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles



# Wir starten unsere webanwendung mit FastAPI
app = FastAPI()

# NEU: wir geben den static-ordner an, damit FastAPI weiß, wo es die statischen Dateien (CSS, JS, Bilder) findet
app.mount("/static", StaticFiles(directory="static"), name="static")

# Wir sagen FastAPI, dass wir Jinja2 als Template-Engine verwenden und die Templates im Ordner "templates" liegen
templates = Jinja2Templates(directory="templates")

# GET FÄLLT RAUS: wir wollen die Berechnung nicht mehr über GET-Parameter machen, sondern über ein Formular mit POST-Methode. Daher wird die GET-Route auskommentiert.
# @app.get("/rechner")
# def zeige_rechner(request: Request):
#     # Wir rendern die HTML-Datei "rechner.html" und übergeben das Request-Objekt
#     return templates.TemplateResponse(request, "rechner.html")

@app.get("/rechner")
async def zeige_rechner(request: Request):
    # Hier senden wir explizit 'ergebnis=None', damit die Jinja-Bedingung greift und die Box unsichtbar bleibt
    return templates.TemplateResponse(request, "rechner.html", {"request": request, "ergebnis": None})

@app.post("/rechner")
async def berechne(request: Request, zahl1: float = Form(...), zahl2: float = Form(...)):
    summe = zahl1 + zahl2
    # Hier laden wir wieder rechner.html und übergeben die 'summe' unter dem Namen 'ergebnis'
    return templates.TemplateResponse(request,"rechner.html", {"request": request, "ergebnis": summe})

@app.get("/seite1")
def zeige_seite1(request: Request):
    # Wir rendern die HTML-Datei "seite1.html" und übergeben das Request-Objekt
    return templates.TemplateResponse(request, "seite1.html")

@app.get("/")
def startseite(request: Request):
    # Wir rendern die HTML-Datei "startseite.html" und übergeben das Request-Objekt
    return templates.TemplateResponse(request, "startseite.html")

#  wurde durch die neue route und POST-Methode ersetzt, daher auskommentiert

# @app.get("/addieren")
# def addiere_zahlen(request: Request, a: int, b: int):
#     # Die eigentliche Logik
#     ergebnis = a + b
    
    # # Wir rufen das Template auf und füttern es mit unseren Variablen
    # return templates.TemplateResponse(request, "ergebnis.html", {
    #     "request": request,
    #     "zahl1": a,
    #     "zahl2": b,
    #     "loesung": ergebnis
    # })

@app.get("/bootstrap")
def zeige_bootstrap(request: Request):
    return templates.TemplateResponse(request, "bootstrap.html")

@app.get("/ueberMich")
def zeige_ueber_mich(request: Request):
    return templates.TemplateResponse(request, "ueberMich.html")

@app.get("/css-training")
def zeige_css_training(request: Request):
    return templates.TemplateResponse(request, "css_training.html")
