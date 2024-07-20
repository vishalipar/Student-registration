var btn = document.querySelector('button')
var msg = document.querySelector('.message')
var nav = document.querySelector('a')

btn.addEventListener('click', function() {
    msg.style.visibility = 'visible'


})

nav.addEventListener('click', function() {
    nav.style.backgroundColor = "yellow"
    nav.style.color = "white"
})