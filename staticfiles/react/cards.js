function processCards(input){
    input.slice(1,input.length-1);
    let raw_array = (input.split(","));
    let number = Number(raw_array[0].slice(1,raw_array[0].length))
    switch(number){
        case(1):
            number="A";
            break;
        case(11):
            number="J";
            break;
        case(12):
            number="Q";
            break;
        case(13):
            number="K";
            break;
    }
    let symbol_string = raw_array[1];
    symbol_string = symbol_string.slice(2,symbol_string.length-2);
    switch(symbol_string){
        case("heart"):
            symbol_string = "♥";
            break;
        case("spade"):
            symbol_string = "♠";
            break;
        case("diamond"):
            symbol_string = "♦";
            break;
        case("club"):
            symbol_string = "♣";
            break;
    }
    return({"num":number,"symbol":symbol_string});
}
function transformDiv(element){
    let content = element.innerHTML;
    element.innerHTML = "";
    let nunAndSymbol = processCards(content);
    return (nunAndSymbol);
}
function CardComponent(props){
    return(
        <div className = {(props.symbol == "♥" || 
        props.symbol == "♦")?"red-card":"black-card"}>
            <p>{props.num}{props.symbol}</p>
        </div>
    )
}
let raw_cards = document.querySelectorAll(".card");
const cards_array = Array.from(raw_cards);
let props_array = cards_array.map(function(element){
    return(transformDiv(element));
});
let index = 0;
props_array.map(function(element){
    ReactDOM.render(<CardComponent num={element.num} symbol={element.symbol}/>,cards_array[index])
    index += 1;
});