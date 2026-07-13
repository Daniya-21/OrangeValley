// ================= MOBILE MENU =================

const hamburger = document.querySelector('.hamburger');
const navLinks = document.querySelector('.nav-links');

if (hamburger && navLinks) {

    hamburger.addEventListener('click', () => {
        hamburger.classList.toggle('active');
        navLinks.classList.toggle('active');
    });

}


// Close mobile menu when clicking on a link

document.querySelectorAll('.nav-links a').forEach(link => {

    link.addEventListener('click', () => {

        if (hamburger && navLinks) {
            hamburger.classList.remove('active');
            navLinks.classList.remove('active');
        }

    });

});



// ================= STICKY NAVBAR =================

const navbar = document.querySelector('.navbar');

if (navbar) {

    window.addEventListener('scroll', () => {

        if (window.scrollY > 50) {

            navbar.style.boxShadow =
                '0 2px 10px rgba(0, 0, 0, 0.1)';

            navbar.style.backgroundColor =
                'rgba(255, 255, 255, 0.98)';

        } else {

            navbar.style.boxShadow =
                '0 2px 10px rgba(0, 0, 0, 0.05)';

            navbar.style.backgroundColor =
                '#ffffff';

        }

    });

}



// ================= CUSTOMIZATION FILTER =================

const filterButtons = document.querySelectorAll('.filter-btn');

const filterSections =
    document.querySelectorAll('.filter-section');


filterButtons.forEach(button => {

    button.addEventListener('click', () => {

        const selectedFilter = button.dataset.filter;


        // Active button

        filterButtons.forEach(btn => {
            btn.classList.remove('active');
        });

        button.classList.add('active');


        // Filter sections

        filterSections.forEach(section => {

            const category = section.dataset.category;


            if (
                selectedFilter === 'all' ||
                selectedFilter === category
            ) {

                section.classList.remove('filter-hidden');

                section.classList.remove('filter-enter');

                void section.offsetWidth;

                section.classList.add('filter-enter');

            } else {

                section.classList.add('filter-hidden');

            }

        });

    });

});