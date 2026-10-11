let numberRandom = Math.round(Math.random() *100);
let tries = 0;

function guessTheNumber(){

    tries = tries + 1;
    id_try.innerHTML = "Bisherige Versuche: " + tries;

    if(numberRandom == input_id.value){
        head_id.innerHTML = "Du hast gewonnen 🥳";
    }
    if(numberRandom < input_id.value){
        head_id.innerHTML = "Die Zahl ist zu groß"
    }
    

    input_id.value = ""
}