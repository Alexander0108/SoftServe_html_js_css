// Select all links within the navbar
const navbarLinks = document.querySelectorAll('.navbar-collapse .nav-link');

// Add a click event listener to each link
navbarLinks.forEach(function (link) {
    link.addEventListener('click', function () {
        // Find the navbar collapse element
        var navbarCollapse = document.querySelector('.navbar-collapse');

        // Check if the navbar is currently expanded
        if (navbarCollapse.classList.contains('show')) {
            // Trigger the Bootstrap collapse toggle
            var navbarToggler = document.querySelector('.navbar-toggler');
            navbarToggler.click();
        }
    });
});
