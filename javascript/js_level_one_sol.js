var f_name=prompt("Enter your first name")
var l_name=prompt("Enteryour last name")
var age=prompt("Enter your age")
var height=prompt("Enter yout height in cm")
var pet=prompt("Enter yout pet name")
alert(pet.length)

if(f_name[0] === l_name[0]){
    console.log("Name Matched")
    if(age>=20 && age<=30){
        console.log("Age matched")
        if(height>170){
            console.log("Height also matched")
            if(pet[pet.length-1] === "y"){
                console.log("all matched")
                console.log("you are Spy")
            }
            else{
                console.log("Not a SPY")
            }
        }
        else{
            console.log("Height not matched")
        }
    }
    else{
        console.log("Age does not matched")
    }
}
else{
    prompt("Thank you")
}