let numberToGuess = Math.round(Math.random() * 100);
let tries = 0;

function guessTheNumber() {
    
    tries = tries + 1;
    displayTries.innerHTML = "Versuche: " + tries;
    
    if(numberToGuess == myNumber.value)  {
        headline.innerHTML = "Du hast gewonnen!!!👍";
        displayRange.innerHTML = "";
        
    }

    if(numberToGuess < myNumber.value) {
        displayRange.innerHTML = "Die Zahl ist zu groß";
    }

     if(numberToGuess > myNumber.value) {
        displayRange.innerHTML = "Die Zahl ist zu klein";
    }

    myNumber.value = ""
}