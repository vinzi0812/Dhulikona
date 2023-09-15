// change navbar style on scroll

window.addEventListener('scroll', () => {
    document.querySelector('nav').classList.toggle
    ('window-scroll', window.scrollY > 0)
})

// show /hide nav menu 
const menu =document.querySelector(".nav__menu");
const menuBtn =document.querySelector("#open-menu-btn");
const CloseBtn =document.querySelector("#close-menu-btn");


menuBtn.addEventListener('click', ()=> {
    menu.style.display= "flex";
    CloseBtn.style.display="inline-block";
    menuBtn.style.display="none";

})

//close nav menu

const closeNav = () => {
    menu.style.display = "none";
    CloseBtn.style.display ="none";
    menuBtn.style.display = "inline-block";
}

CloseBtn.addEventListener('click',closeNav);

