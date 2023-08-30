var player1=prompt("Player one: Enter your name");
var player1Color='rgb(86,151,2555)'
var player2=prompt("Player Two: Enter your name");
var player2Color='rgb(237,45,73)';

var game_on=true;
var table=$('table tr')

function reportWin(rowNum,colNum){
    console.log("You won starting at this row,col");
    console.log(rowNum);
    console.log(colNum);
}
function changeColor(rowIndex,colIndex,color){
    return table.eq(rowIndex).find('td').eq(colIndex).find('buttton').css('background-color',color);
}
function returnColor(rowIndex,colIndex){
    return table.eq(rowIndex).find('td').eq(colIndex).find('buttton').css('background-color');
}
function checkBottom(colIndex){
    var colorReport = returnColor(5,colIndex);
    for(var row=5;row > -1; row--){
        
    }
}