// Mobile menu toggle
const hamburger = document.querySelector('.hamburger');
const navLinks = document.querySelector('.nav-links');

if (hamburger) {
    hamburger.addEventListener('click', () => {
        hamburger.classList.toggle('active');
        navLinks.classList.toggle('active');
    });
}

// Close mobile menu when clicking on a link
document.querySelectorAll('.nav-links a').forEach(link => {
    link.addEventListener('click', () => {
        hamburger.classList.remove('active');
        navLinks.classList.remove('active');
    });
});

// Sticky Navbar Background on Scroll
const navbar = document.querySelector('.navbar');

window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
        navbar.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.1)';
        navbar.style.backgroundColor = 'rgba(255, 255, 255, 0.98)';
    } else {
        navbar.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.05)';
        navbar.style.backgroundColor = '#ffffff';
    }
});
