var hedOne=document.querySelector("#one")
var hedTwo=document.querySelector("#two")
var hedThree=document.querySelector("#three")

hedOne.addEventListener('mouseover',function(){
    hedOne.textContent = "click me";
    hedOne.style.color='red';
})

hedOne.addEventListener("mouseout",function(){
    hedOne.textContent="click me";
    hedOne.style.color="black";
})

hedTwo.addEventListener("click",function(){
    hedTwo.textContent='Mouse over me';
    hedTwo.style.color='blue';
})
hedThree.addEventListener("dblclick",function(){
    hedThree.textContent='click slowly';
    hedThree.style.color='red';
})
