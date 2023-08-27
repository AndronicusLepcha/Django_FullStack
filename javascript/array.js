var countries=["USA","India","China"]

countries[0]=20
//console.log(countries)
for(var i=0;i<countries.length;i++){
    console.log(countries[i])
}

// Array are mutable
myArray=['one','two','three']
var l_item=myArray.pop()
console.log(myArray)
myArray.push("Ronaldo")
console.log(myArray)

var matrix=[[1,2,3],[4,5,6],[6,7,8]]
console.log(matrix)


// of for

for(ob in myArray){
    console.log(ob)
}

myArray.forEach(alert)