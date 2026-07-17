// ================= MOBILE MENU =================

const hamburger = document.querySelector(".hamburger");
const navLinks = document.querySelector(".nav-links");
const hamburgerIcon = hamburger?.querySelector("i");

if (hamburger && navLinks) {

    hamburger.addEventListener("click", () => {

        hamburger.classList.toggle("active");
        navLinks.classList.toggle("active");

        if (navLinks.classList.contains("active")) {

            hamburgerIcon?.classList.remove("fa-bars");
            hamburgerIcon?.classList.add("fa-xmark");

        } else {

            hamburgerIcon?.classList.remove("fa-xmark");
            hamburgerIcon?.classList.add("fa-bars");

        }

    });

}


// ================= CLOSE MOBILE MENU =================

document.querySelectorAll(".nav-links a").forEach(link => {

    link.addEventListener("click", () => {

        hamburger?.classList.remove("active");
        navLinks?.classList.remove("active");

        hamburgerIcon?.classList.remove("fa-xmark");
        hamburgerIcon?.classList.add("fa-bars");

    });

});


// ================= STICKY NAVBAR =================

const navbar = document.querySelector(".navbar");

if (navbar) {

    window.addEventListener("scroll", () => {

        if (window.scrollY > 50) {

            navbar.style.boxShadow =
                "0 2px 10px rgba(0,0,0,0.1)";

            navbar.style.backgroundColor =
                "rgba(255,255,255,0.98)";

        } else {

            navbar.style.boxShadow =
                "0 2px 10px rgba(0,0,0,0.05)";

            navbar.style.backgroundColor =
                "#ffffff";

        }

    });

}


// ================= CUSTOMIZATION FILTER =================

const filterButtons = document.querySelectorAll(".filter-btn");
const filterSections = document.querySelectorAll(".filter-section");

filterButtons.forEach(button => {

    button.addEventListener("click", () => {

        const selectedFilter = button.dataset.filter;

        filterButtons.forEach(btn => {

            btn.classList.remove("active");

        });

        button.classList.add("active");

        filterSections.forEach(section => {

            const category = section.dataset.category;

            if (
                selectedFilter === "all" ||
                selectedFilter === category
            ) {

                section.classList.remove("filter-hidden");

                section.classList.remove("filter-enter");

                void section.offsetWidth;

                section.classList.add("filter-enter");

            } else {

                section.classList.add("filter-hidden");

            }

        });

    });

});


// ================= EMAILJS CONTACT FORM =================

const contactForm = document.getElementById("contactForm");

if (contactForm) {

    contactForm.addEventListener("submit", function (e) {

        e.preventDefault();

        const submitButton = document.querySelector(".contact-submit");

        submitButton.disabled = true;
        submitButton.innerHTML = "Sending...";

        emailjs.sendForm(
            "service_y28crum",
            "template_3vk8n84",
            this
        )

        .then(() => {

            alert("✅ Thank you! Your enquiry has been sent successfully.");

            contactForm.reset();

        })

        .catch((error) => {

            console.error(error);

            alert("❌ Failed to send message. Please try again.");

        })

        .finally(() => {

            submitButton.disabled = false;

            submitButton.innerHTML =
                'Send Message <i class="fa-solid fa-arrow-right"></i>';

        });

    });

}