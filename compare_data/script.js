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

    if(file1 && file2){
        console.log(file1.name + " und " + file2.name + " sind erfolgreich hochgeladen")
    } else {
        console.log("Fehler: Bitte beide Dateien überprüfen")
        showMessage 
    }

})