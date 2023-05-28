const images = document.querySelectorAll(".dummy-img");
console.log(images)
function FirstComponent(props){
    return(
        <div> 
            <img src={props.imgSrc}></img>
        </div> 
    )
}

const domContainer = document.querySelector("#root");
const imagesList = Array.from(images);
imagesList.map(function(image){
    let thisSource = image.innerHTML;
    image.innerHTML="";
    ReactDOM.render(<FirstComponent imgSrc={thisSource} />, domContainer);

})