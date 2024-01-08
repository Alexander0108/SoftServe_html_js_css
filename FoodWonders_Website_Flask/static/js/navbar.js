
const navbarLinks = document.querySelectorAll('.navbar-collapse .nav-link');

navbarLinks.forEach(function (link) {
    link.addEventListener('click', function () {
        var navbarCollapse = document.querySelector('.navbar-collapse');
        if (navbarCollapse.classList.contains('show')) {

            var navbarToggler = document.querySelector('.navbar-toggler');
            navbarToggler.click();
        }
    });
});
