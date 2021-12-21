let pause = document.querySelector('.pause');
let play = document.querySelector('.play');
let btn = document.querySelector('#app');

btn.addEventListener('click', () => {
    if ( play.classList.contains("active") ) {
        play.classList.remove("active");
        pause.classList.add("active");
    }
    else {
        pause.classList.remove("active");
        play.classList.add("active");
    }
})