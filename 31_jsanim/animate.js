var c = document.getElementById("playground");
var dotButton = document.getElementById("buttonCircle");
var  stopButton = document.getElementById("buttonStop");

var ctx = c.getContext("2d");

ctx.fillStyle = "blue";

var requestID;

var clear = (e) => {
    ctx.clearRect(0, 0, c.width, c.height);
}

var radius = 100;
var growing = true;

var drawDot = (e) =>{
    clear(e);
    if(radius === 250) {growing = false}
    if(radius === 0) {growing = true}
    // while(true){
        if (growing){
            radius += 5;
        }
        else{
            radius -= 5;
        }
        console.log(radius);
        ctx.beginPath();
        ctx.arc(c.width / 2, c.height / 2, radius, 0, Math.PI * 2);
        ctx.stroke();
        ctx.fill();
    // }
    
}

var stopIt = (e) => {
    console.log("stopit invoked...");
    console.long( requestID );

}


dotButton.addEventListener("click", drawDot);
stopButton.addEventListener("click", stopIt);