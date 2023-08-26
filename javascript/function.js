//alert("Function is executed ")
//console.log("Function in JS")
function hello(){
    console.log("hello coder")
}

function robot(name){
    console.log("hello "+name)
}

function addNum(a,b){
    console.log(a+b)
}

function Hacker(name="Andronicus"){
   // console.log("Hacker "+name)
   return "Hacker "+name
}


//////////////GLOBAL && LOCAL VARIABLE//////////////////////////

function five_times(numinput){
    //local scope to the function var result
    var result=numinput*5
    return result
}
//global scope
var v="Gloabal V"
var stuff="Global Stuff"

function fun(stuff){
    console.log(v)
    stuff="Reassign Stuff inside function"
    console.log(stuff)
}
fun() //function call
console.log(stuff)