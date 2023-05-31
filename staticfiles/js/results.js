let gameOverMessage = document.querySelector(".first-message");
let resultMessage = document.querySelector(".second-message");
let button = document.getElementById("show-button");
let botCards = document.querySelectorAll(".bot-card");
const cardsArray = Array.from(botCards);
gameOverMessage.addEventListener("load",trigger());
function trigger(){
    setTimeout(gameOverAppear,500);
}
function gameOverAppear(){
    gameOverMessage.classList.toggle("hidden");
    setTimeout(resultAppear, 1500);
}
function resultAppear(){
    resultMessage.classList.toggle("hidden");
    button.classList.toggle("hidden");
    cardsArray.map(function(card){
        card.classList.toggle("hide");
    })
}