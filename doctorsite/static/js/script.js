// Get the current year for the copyright
$('#year').text(new Date().getFullYear());

// Init Scrollspy
var scrollSpy = new bootstrap.ScrollSpy(document.body, {
    target: '.navbar'
})

// Smooth Scrolling
$(".navbar a").on('click', function (event) {
    if (this.hash !== "") {
        event.preventDefault();

        const hash = this.hash;

        $('html, body').animate({
        scrollTop: $(hash).offset().top
        }, 800, function () {

        window.location.hash = hash;
        });
    }
});

const special = document.querySelector('.btn-special');
const html = document.querySelector('html');
console.log("here we go")

special.addEventListener('click', function(e) {
    html.style.setProperty("font-size", "19px", "important")
});