//set of programming languages
var programming_languages = [
	"python",
	"javascript",
	"mongodb",
	"json",
	"java",
	"html",
	"css",
	"c",
	"csharp",
	"golang",
	"kotlin",
	"php",
	"sql",
  "ruby",
  "react",
  "nodejs"
]

let answer = '';
let maxWrong = 6;
let mistakes = 0;
let guessed = [];
let wordStatus = null;

//The task is to select the random element from the array 
function randomWord() {
  //Use Math.random() function to get the random number between(0-1, 1 exclusive).
  //Multiply it by the array length to get the numbers between(0-arrayLength).
  //Use Math.floor() to get the index ranging from(0 to arrayLength-1).
  answer = programming_languages[Math.floor(Math.random() * programming_languages.length)];
}

//keyboard
//generating buttons for 26 alphabets
function generateButtons() {
  let buttonsHTML = 'abcdefghijklmnopqrstuvwxyz'.split('').map(letter =>
    //applying styles to each letter
    `
      <button
        class="btn btn-lg btn-primary m-2"
        id='` + letter + `'
        onClick="handleGuess('` + letter + `')"
      >
        ` + letter + `
      </button>
    `).join('');

  document.getElementById('keyboard').innerHTML = buttonsHTML;
}

function handleGuess(chosenLetter) {
  //check if the guessed letter is in guessed array or not
  //If yes then no need to push
  //If no then push the element into the guessed array.
  guessed.indexOf(chosenLetter) === -1 ? guessed.push(chosenLetter) : null;
  document.getElementById(chosenLetter).setAttribute('disabled', true);

  if (answer.indexOf(chosenLetter) >= 0) {
    guessedWord();
    checkIfGameWon();
  } else if (answer.indexOf(chosenLetter) === -1) {
    mistakes++;
    updateMistakes();
    checkIfGameLost();
    updateHangmanPicture();
  }
}

//According to the count of mistakes , print the image
function updateHangmanPicture() {
    if(mistakes==1){
      document.getElementById('hangmanPic').src = '../static/assests/hang1.PNG';
    }
    else if(mistakes==2){
      document.getElementById('hangmanPic').src = '../static/assests/hang2.PNG';
    }
    else if(mistakes==3){
      document.getElementById('hangmanPic').src = '../static/assests/hang3.PNG';
    }
    else if(mistakes==4){
      document.getElementById('hangmanPic').src = '../static/assests/hang4.PNG';
    }
    else if(mistakes==5){
      document.getElementById('hangmanPic').src = '../static/assests/hang5.PNG';
    }
    else {
      document.getElementById('hangmanPic').src = '../static/assests/hang6.PNG';
    }
}

// If the given word matches to the answer,You win.
function checkIfGameWon() {
  if (wordStatus === answer) {
    document.getElementById('keyboard').innerHTML = 'You Won!!!';
  }
}

//If the mistakes exceed the range ,we will reveal the answer and print you lost.
function checkIfGameLost() {
  if (mistakes === maxWrong) {
    document.getElementById('wordSpotlight').innerHTML = 'The answer was: ' + answer;
    document.getElementById('keyboard').innerHTML = 'You Lost!!!';
  }
}

function guessedWord() {
  wordStatus = answer.split('').map(letter => (guessed.indexOf(letter) >= 0 ? letter : " _ ")).join('');

  document.getElementById('wordSpotlight').innerHTML = wordStatus;
}

//This function is used set the mistakes back to zero when the game is reset
function updateMistakes() {
  document.getElementById('mistakes').innerHTML = mistakes;
}

//To restart the game again 
function reset() {
  mistakes = 0;
  guessed = [];
  document.getElementById('hangmanPic').src = '../static/assests/hang0.PNG';

  randomWord();
  guessedWord();
  updateMistakes();
  generateButtons();
}


randomWord();
generateButtons();
guessedWord();