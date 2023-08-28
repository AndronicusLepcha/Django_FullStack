var squares= document.querySelectorAll('td')

var restart=document.querySelector("#b")

//clear all the squares
function clearBoard(){
    for(var i=0;i<squares.length;i++){
        squares[i].textContent='';
    }
}
restart.addEventListener('click',clearBoard);
//check the square
var one=document.querySelector('#one')

function changeMarker(){
    if(this.textContent=== ''){
        //alert("Game over")
        this.textContent = 'X';
    }else if(this.textContent === 'X'){
        this.textContent='O';
    }else{
        this.textContent='';
    }
}
function checkGame(){
    if(this.textContent === 'X' && squares[1].textContent === "X" &&squares[2].textContent==="X"){
        alert("Game Over")
        clearBoard()
    }else if(this.textContent === 'X' && squares[3].textContent === "X" &&squares[4].textContent==="X"){
        alert("Game Over")
        clearBoard()
    }

}

for(var i=0;i<squares.length;i++){
    squares[i].addEventListener('click',changeMarker);
    squares[i].addEventListener('click',checkGame);
    
}



