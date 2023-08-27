var roaster=["Richard"] //empty array

function add(name){
    roaster.push(name)
}
//add('Andro')
//console.log(roaster)
 function remove(){
    roaster.pop()
 }
function display(){
    //console.log(2323323)
    for(n of roaster){
        console.log(n)
    }
}
//display()
var input=true
while(input){
    var ch=prompt("Chose any option 1.Add 2.Remove 3.Display 4. exit")
    //console.log(ch)
    if(ch=="add"){
        var nam=prompt('Enter name to add in an array ')
        add(nam)
    }
    else if(ch=="remove"){
        remove()
    }
    else if(ch == "display"){
        display()
    }
    else{
        alert("thank you for the information")
        input=false
    }
}