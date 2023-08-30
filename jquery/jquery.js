// console.log($('h1').text())
// var x=$('h1').text()
// console.log(x)

$('h1').click(function(){
    console.log('this is clicked')
    $(this).text('I was Changed')
})
$('h1').dblclick(function(){
    console.log('doubled clicked')
    $(this).text('Doubled Clicked')
})
$('li').click(function(){
    console.log('this is clicked')
})
$('input').eq(0).keypress(function(){
    console.log(event)
    if(event.which === 13){
        $('h3').toggleClass('turnblue')
    }
})
// $('input').eq(1).on('click',function(){
//     $('.container').fadeOut(300)
// })
$('input').eq(1).on('click',function(){
    $('.container').slideUp(300)
})