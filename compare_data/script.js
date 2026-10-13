// Datei 1 und 2 einlesen
const input_one = document.getElementById('datei_eins');
const input_two = document.getElementById('datei_zwei');


// Form einer Variablen zuweisen
const formular = document.getElementById('form_id')

// auf das absenden(summit) lauschen und unterbrechen sobald es betätigt wird
formular.addEventListener('submit', function(event){
    event.preventDefault(); // Das ist der magische Befehl, der den Reload stoppt!
    console.log("Erolgreich abgefangen.");

    const file1 = input_one.files[0];
    const file2 = input_two.files[0];

    // ABFRAGE ob file 1 und 2 vorhanden
    if(file1 && file2){
        console.log(file1.name + " und " + file2.name + " sind erfolgreich hochgeladen")
        
        // inhalt 1 und 2 deklarieren, die wir später bearbeiten
        let inhalt1 = null
        let inhalt2 = null

        // function um dateien miteinander zu verlgeichen, DEKLARIEREN.
        function vergleicheWennFertig() {
            if (inhalt1 !== null && inhalt2 !== null) {
                console.log("Beide Dateien sind da! Jetzt können wir splitten.")
                
                // Struktur aufbauen
                const zeilen1 = inhalt1.split("\r\n")
                const zeilen2 = inhalt2.split("\r\n")
                
                // Kontrolle
                console.log(zeilen1)
                console.log(zeilen2)

                //Liste erstellen um gecuttete Laverma IDs hinzuzufügen
                const nummern2 = [];

                // For Schleife um IDs zu seperieren und der Liste hinzuzufügen
                for (let zeile of zeilen2) {
                    const reineNummer = zeile.split(",")[0];
                    nummern2.push(reineNummer)

                }
                console.log("die sauberen IDs aus Datei 2:", nummern2)

                // schickt jede einzelne zeile von nummer2 in die "myfunction"
                const gleiche_nummern = nummern2.filter(myfunction);

                function myfunction(aktuelleNummer){
                    // prüft ob jede einzelne Zeile in "zeilen1" in der aktuellen nummer der liste nummern2 vorkommt
                    // update !== "" , weil sonst durch strip die letzten beide leere Zeilen auch verglichen werden.
                    return aktuelleNummer !== "" && zeilen1.includes(aktuelleNummer);                   

                }
                // prüfen ob die übereinstimmung geklappt hat
                console.log("Die ID's die in beiden Versionen vorkommen" + gleiche_nummern);

                // Output definieren und counter definieren
                let output = "";
                let counter = 1;

                // FOR Schleife formatieren, sodass am ende eine schöne Auflistung rauskommt
                for (let zeile of gleiche_nummern) {
                    output += counter + ". " + zeile + "<br>"
                    counter ++
                }
                // innerHTML zum überschreiben der Seite und Darstellen der ID's
                // form_id = formular  ... kuckstu oben
                formular.innerHTML = output // ID's

                // Das Element "middle_header" erst im HTML-Dokument suchen und dann direkt überschreiben
                document.getElementById("middle_header").innerHTML = "ID's die in beiden Dateien enthalten sind:"
                

            }
        }
        // Reader1 erstellen 
        const reader1 = new FileReader()
        
        // Aktion definieren: Was soll passieren, sobald die Datei fertig gelesen ist?
        reader1.onload = function(event) {

            inhalt1 = event.target.result;
            console.log("Inhalt von Datei 1:" , inhalt1)
            // Den Türsteher aufwecken und prüfen lassen!
            vergleicheWennFertig();
            }
        
        // Startschuss: Die physische Datei nehmen und als Text auslesen    
        reader1.readAsText(file1);

        // Reader2 erstellen
        const reader2 = new FileReader()

        // Aktion definieren: Was soll passieren, sobald die Datei fertig gelesen ist?
        reader2.onload = function(event) {

            inhalt2 = event.target.result
            console.log("Inhalt von Datei 2:" , inhalt2)
            // Den Türsteher aufwecken und prüfen lassen!
            vergleicheWennFertig();
        }
        
        // Startschuss: Die physische Datei nehmen und als Text auslesen    
        reader2.readAsText(file2)
    
    // Wenn Datei 1 und 2 nicht vorliegen.    
    } else {
        console.log("Fehler: Bitte beide Dateien überprüfen")
        }
    




    
        

})