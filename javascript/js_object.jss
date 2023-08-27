var carInfo={make:"Mahindra",year:1909,model:"Thar"}
//console.log(carInfo)
//console.log(carInfo["year"])


var myNewO = {a:"hello",b:[1,2,3],c:{in:[1,2,3]}};
//console.log(myNewO['c']['in'][0])
console.log(myNewO['c'])

carInfo['year']=2002
console.log(carInfo)
console.dir(carInfo)

for(o in carInfo){
    console.log(o)
}


/////Objects Methods////

var myOM={
    pop:"Hello",
    myMethod : function(){
        console.log("My method was called !");
        alert(this.pop);
    }
}
myOM.myMethod()