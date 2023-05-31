const image = document.getElementById("signal");
setTimeout(changeToB, 500);
function changeToB(){
    image.src = imgB;
    setTimeout(changeToA, 500);
}
function changeToA(){
    image.src = imgA;
    setTimeout(changeToB, 500);
}