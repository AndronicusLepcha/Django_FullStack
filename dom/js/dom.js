var an=document.querySelector("h1")
an.style.color = 'green';



function getRandomColor(){
    var letters = "0123456780ABCDEF"
    var color='#'
    for(var i=0;i<6;i++){
        color += letters[Math.floor(Math.random()*16)]
    }
    return color
}

function changeHeaderColor(){
    colorInput=getRandomColor()
    an.style.color=colorInput
}
setInterval("changeHeaderColor()",500)