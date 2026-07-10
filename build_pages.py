import os

header = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Uniform Valley</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="css/pages.css">
</head>
<body>
    <nav class="navbar">
        <div class="container nav-container">
            <a href="index.html" class="logo">UNIFORM VALLEY</a>
            <ul class="nav-links">
                <li><a href="index.html" {home_active}>Home</a></li>
                <li><a href="about.html" {about_active}>About Us</a></li>
                <li><a href="corporate.html" {corp_active}>Corporate Collection</a></li>
                <li><a href="scrubs.html" {scrubs_active}>Medical Scrubs</a></li>
                <li><a href="materials.html" {mat_active}>Materials</a></li>
                <li><a href="customization.html" {cust_active}>Customization</a></li>
                <li><a href="contact.html" {cont_active}>Contact Us</a></li>
            </ul>
            <a href="contact.html" class="btn btn-primary nav-btn">Get in Touch</a>
            <div class="hamburger"><i class="fa-solid fa-bars"></i></div>
        </div>
    </nav>
"""

footer = """
    <footer class="footer">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-brand">
                    <h3>UNIFORM VALLEY</h3>
                    <p style="margin-top: 15px;">A Modern Premium<br>Workwear Brand</p>
                </div>
                <div class="footer-links-col">
                    <h4>Quick Links</h4>
                    <ul>
                        <li><a href="index.html">Home</a></li>
                        <li><a href="about.html">About Us</a></li>
                        <li><a href="corporate.html">Corporate Collection</a></li>
                        <li><a href="scrubs.html">Medical Scrubs</a></li>
                        <li><a href="materials.html">Materials</a></li>
                        <li><a href="customization.html">Customization</a></li>
                        <li><a href="contact.html">Contact Us</a></li>
                    </ul>
                </div>
                <div class="footer-links-col">
                    <h4>Collections</h4>
                    <ul>
                        <li><a href="corporate.html">Corporate Shirts</a></li>
                        <li><a href="#">Executive Wear</a></li>
                        <li><a href="scrubs.html">Medical Scrubs</a></li>
                        <li><a href="#">Hospital Uniforms</a></li>
                        <li><a href="#">Accessories</a></li>
                    </ul>
                </div>
                <div class="footer-contact">
                    <h4>Contact Us</h4>
                    <p style="margin-bottom: 15px;"><strong>Subha Devi</strong><br>Corporate Specialist</p>
                    <p><i class="fa-regular fa-envelope"></i> subhadevi@cratus.in</p>
                    <p><i class="fa-solid fa-phone"></i> +91 88846 71299</p>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2024 Uniform Valley. All Rights Reserved.</p>
            </div>
        </div>
    </footer>
    <script src="js/script.js"></script>
</body>
</html>
"""

pages = {
    'about.html': {
        'title': 'About Us',
        'active': 'about_active',
        'content': """
    <section class="page-hero">
        <div class="container page-hero-container">
            <div class="page-hero-content">
                <h3 class="sub-section-title">ABOUT US</h3>
                <h1>Crafting Professional Identity<br>Through Premium Workwear</h1>
                <p>Uniform Valley is India's specialist in premium corporate shirts and medical scrubs. With over two decades of manufacturing excellence and export experience, we deliver quality uniforms that reflect your brand identity.</p>
            </div>
            <div class="page-hero-image">
                <img src="https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=600&q=80" alt="Company Building">
            </div>
        </div>
    </section>

    <section class="section-padding pt-0">
        <div class="container">
            <h3 class="sub-section-title">OUR STRENGTHS</h3>
            <div class="features-grid" style="margin-top: 2rem;">
                <div class="feature-item">
                    <div class="feature-icon"><i class="fa-solid fa-calendar-check"></i></div>
                    <h3>20+ Years Experience</h3>
                    <p>Two decades of<br>manufacturing<br>excellence.</p>
                </div>
                <div class="feature-item">
                    <div class="feature-icon"><i class="fa-solid fa-pen-ruler"></i></div>
                    <h3>CAD Design Capability</h3>
                    <p>Advanced CAD design<br>for precision & perfect<br>fit.</p>
                </div>
                <div class="feature-item">
                    <div class="feature-icon"><i class="fa-solid fa-shirt"></i></div>
                    <h3>Premium Quality</h3>
                    <p>Best fabrics, finest<br>stitching and quality<br>assurance.</p>
                </div>
                <div class="feature-item">
                    <div class="feature-icon"><i class="fa-solid fa-globe"></i></div>
                    <h3>Export Standards</h3>
                    <p>International quality<br>benchmarks in every<br>product.</p>
                </div>
            </div>
        </div>
    </section>

    <section class="section-padding pt-0">
        <div class="container">
            <h3 class="sub-section-title">OUR PROCESS</h3>
            <div class="process-wrapper">
                <div class="process-step">
                    <div class="process-icon"><i class="fa-regular fa-file-lines"></i></div>
                    <h4>1. Requirement<br>Analysis</h4>
                </div>
                <div class="process-step">
                    <div class="process-icon"><i class="fa-solid fa-bezier-curve"></i></div>
                    <h4>2. CAD Design &<br>Sampling</h4>
                </div>
                <div class="process-step">
                    <div class="process-icon"><i class="fa-solid fa-layer-group"></i></div>
                    <h4>3. Fabric<br>Selection</h4>
                </div>
                <div class="process-step">
                    <div class="process-icon"><i class="fa-solid fa-industry"></i></div>
                    <h4>4. Manufacturing<br>Excellence</h4>
                </div>
                <div class="process-step">
                    <div class="process-icon"><i class="fa-solid fa-clipboard-check"></i></div>
                    <h4>5. Quality Check &<br>Delivery</h4>
                </div>
            </div>
        </div>
    </section>
"""
    },
    'corporate.html': {
        'title': 'Corporate Collection',
        'active': 'corp_active',
        'content': """
    <section class="page-hero">
        <div class="container page-hero-container">
            <div class="page-hero-content">
                <h3 class="sub-section-title">CORPORATE COLLECTION</h3>
                <h1>Executive Shirts for the<br>Modern Professional</h1>
                <p>Our Executive Collection offers four distinct shirt styles crafted with premium fabrics and impeccable finishing.</p>
            </div>
            <div class="page-hero-image">
                <img src="https://images.unsplash.com/photo-1596755094514-f87e32f85e2c?auto=format&fit=crop&w=400&q=80" alt="Corporate Shirt">
            </div>
        </div>
    </section>

    <section class="section-padding pt-0">
        <div class="container">
            <h3 class="sub-section-title">THE SHIRT STYLES</h3>
            <div class="shirt-styles-grid">
                <div class="shirt-card">
                    <h4>Style 1</h4>
                    <p style="font-size: 0.8rem; color: #666;">Classic Collar<br>With Placket<br>With Pocket</p>
                    <img src="https://images.unsplash.com/photo-1602810318383-e386cc2a3ccf?auto=format&fit=crop&w=300&q=80" alt="Style 1">
                </div>
                <div class="shirt-card">
                    <h4>Style 2</h4>
                    <p style="font-size: 0.8rem; color: #666;">Classic Collar<br>Without Placket<br>Without Pocket</p>
                    <img src="https://images.unsplash.com/photo-1598033129183-c4f50c736f10?auto=format&fit=crop&w=300&q=80" alt="Style 2">
                </div>
                <div class="shirt-card">
                    <h4>Style 3</h4>
                    <p style="font-size: 0.8rem; color: #666;">Mandarin Collar<br>With Placket<br>With Pocket</p>
                    <img src="https://images.unsplash.com/photo-1596755094514-f87e32f85e2c?auto=format&fit=crop&w=300&q=80" alt="Style 3">
                </div>
                <div class="shirt-card">
                    <h4>Style 4</h4>
                    <p style="font-size: 0.8rem; color: #666;">Mandarin Collar<br>Without Placket<br>Without Pocket</p>
                    <img src="https://images.unsplash.com/photo-1629450348780-e37452e85ab8?auto=format&fit=crop&w=300&q=80" alt="Style 4">
                </div>
            </div>
            <div class="text-center">
                <a href="#" class="btn btn-primary" style="padding: 12px 32px;">View Style Comparison</a>
            </div>
        </div>
    </section>
"""
    },
    'scrubs.html': {
        'title': 'Medical Scrubs',
        'active': 'scrubs_active',
        'content': """
    <section class="page-hero">
        <div class="container page-hero-container">
            <div class="page-hero-content">
                <h3 class="sub-section-title">MEDICAL SCRUBS</h3>
                <h1>Comfort. Style. Performance.<br>Everyday.</h1>
                <p>Our scrubs are designed for healthcare professionals who demand comfort, durability and a smart look through long working hours.</p>
            </div>
            <div class="page-hero-image">
                <img src="https://images.unsplash.com/photo-1584515979956-d9f6e5d09982?auto=format&fit=crop&w=400&q=80" alt="Medical Scrubs">
            </div>
        </div>
    </section>

    <section class="section-padding pt-0">
        <div class="container">
            <h3 class="sub-section-title">SCRUB CATEGORIES</h3>
            <div class="custom-grid" style="grid-template-columns: repeat(3, 1fr);">
                <div class="shirt-card" style="padding: 0; overflow: hidden; text-align: left;">
                    <img src="https://images.unsplash.com/photo-1579684385127-1ef15d508118?auto=format&fit=crop&w=400&q=80" alt="Men's Scrubs" style="width: 100%; height: 250px; object-fit: cover; margin: 0;">
                    <div style="padding: 1.5rem;">
                        <h4 style="margin-bottom: 0.5rem;">Men's Scrubs</h4>
                        <p style="font-size: 0.85rem; color: #666;">Functional and comfortable scrubs for everyday performance.</p>
                    </div>
                </div>
                <div class="shirt-card" style="padding: 0; overflow: hidden; text-align: left;">
                    <img src="https://images.unsplash.com/photo-1584982751601-97dcc096659c?auto=format&fit=crop&w=400&q=80" alt="Women's Scrubs" style="width: 100%; height: 250px; object-fit: cover; margin: 0;">
                    <div style="padding: 1.5rem;">
                        <h4 style="margin-bottom: 0.5rem;">Women's Scrubs</h4>
                        <p style="font-size: 0.85rem; color: #666;">Tailored fit scrubs with style, comfort and ease of movement.</p>
                    </div>
                </div>
                <div class="shirt-card" style="padding: 0; overflow: hidden; text-align: left;">
                    <img src="https://images.unsplash.com/photo-1584515979956-d9f6e5d09982?auto=format&fit=crop&w=400&q=80" alt="Unisex Scrubs" style="width: 100%; height: 250px; object-fit: cover; margin: 0;">
                    <div style="padding: 1.5rem;">
                        <h4 style="margin-bottom: 0.5rem;">Unisex Scrubs</h4>
                        <p style="font-size: 0.85rem; color: #666;">Versatile scrubs designed for all healthcare professionals.</p>
                    </div>
                </div>
            </div>
            
            <h3 class="sub-section-title" style="margin-top: 4rem;">SCRUB FEATURES</h3>
            <div class="scrub-features">
                <div class="feature-small">
                    <i class="fa-solid fa-wind"></i>
                    <span>Breathable Fabric</span>
                </div>
                <div class="feature-small">
                    <i class="fa-solid fa-droplet-slash"></i>
                    <span>Moisture Control</span>
                </div>
                <div class="feature-small">
                    <i class="fa-solid fa-shirt"></i>
                    <span>Anti-Wrinkle</span>
                </div>
                <div class="feature-small">
                    <i class="fa-solid fa-hands-bubbles"></i>
                    <span>Easy Maintenance</span>
                </div>
                <div class="feature-small">
                    <i class="fa-solid fa-shield-halved"></i>
                    <span>Durable & Long Lasting</span>
                </div>
            </div>
        </div>
    </section>
"""
    },
    'materials.html': {
        'title': 'Materials & Fabrics',
        'active': 'mat_active',
        'content': """
    <section class="page-hero" style="margin-bottom: 2rem;">
        <div class="container">
            <div class="page-hero-content" style="padding-bottom: 0;">
                <h3 class="sub-section-title">MATERIALS & FABRICS</h3>
                <h1>Premium Fabrics for<br>Every Need</h1>
                <p>We offer a wide range of carefully selected fabrics<br>that ensure comfort, durability and a professional look.</p>
            </div>
        </div>
    </section>

    <section class="section-padding pt-0">
        <div class="container">
            <h3 class="sub-section-title">CORPORATE CUSTOMIZATION</h3>
            <div class="custom-grid">
                <div class="custom-card">
                    <i class="fa-solid fa-pen-nib"></i>
                    <h4>Logo Embroidery</h4>
                </div>
                <div class="custom-card">
                    <i class="fa-solid fa-signature"></i>
                    <h4>Name Embroidery</h4>
                </div>
                <div class="custom-card">
                    <i class="fa-solid fa-palette"></i>
                    <h4>Custom Colors</h4>
                </div>
                <div class="custom-card">
                    <i class="fa-solid fa-shirt"></i>
                    <h4>Collar Options</h4>
                </div>
            </div>

            <h3 class="sub-section-title" style="margin-top: 3rem;">SCRUB CUSTOMIZATION</h3>
            <div class="custom-grid">
                <div class="custom-card">
                    <i class="fa-solid fa-layer-group"></i>
                    <h4>Department Colors</h4>
                </div>
                <div class="custom-card">
                    <i class="fa-solid fa-hospital"></i>
                    <h4>Hospital Branding</h4>
                </div>
                <div class="custom-card">
                    <i class="fa-solid fa-id-badge"></i>
                    <h4>Staff Identification</h4>
                </div>
                <div class="custom-card">
                    <i class="fa-solid fa-ruler"></i>
                    <h4>Custom Sizing</h4>
                </div>
            </div>
            
            <div style="margin-top: 2rem;">
                <a href="contact.html" class="btn btn-primary" style="padding: 12px 32px;">Request Customization</a>
            </div>
        </div>
    </section>
"""
    },
    'customization.html': {
        'title': 'Customization',
        'active': 'cust_active',
        'content': """
    <section class="page-hero" style="margin-bottom: 2rem;">
        <div class="container">
            <div class="page-hero-content" style="padding-bottom: 0;">
                <h3 class="sub-section-title">CUSTOMIZATION</h3>
                <h1>Your Brand. Speaks<br>for Itself</h1>
                <p>A glimpse of our premium corporate shirts<br>and medical scrubs.</p>
            </div>
        </div>
    </section>

    <section class="section-padding pt-0">
        <div class="container">
            <div class="toggles">
                <button class="toggle-btn active">Corporate Shirts</button>
                <button class="toggle-btn">Medical Scrubs</button>
            </div>
            
            <div class="gallery">
                <img src="https://images.unsplash.com/photo-1556740758-90de374c12ad?auto=format&fit=crop&w=500&q=80" alt="Gallery">
                <img src="https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?auto=format&fit=crop&w=500&q=80" alt="Gallery">
                <img src="https://images.unsplash.com/photo-1556741533-974f8e62a92d?auto=format&fit=crop&w=500&q=80" alt="Gallery">
                <img src="https://images.unsplash.com/photo-1584982751601-97dcc096659c?auto=format&fit=crop&w=500&q=80" alt="Gallery">
                <img src="https://images.unsplash.com/photo-1579684385127-1ef15d508118?auto=format&fit=crop&w=500&q=80" alt="Gallery">
                <img src="https://images.unsplash.com/photo-1584515979956-d9f6e5d09982?auto=format&fit=crop&w=500&q=80" alt="Gallery">
            </div>
        </div>
    </section>
"""
    },
    'contact.html': {
        'title': 'Contact Us',
        'active': 'cont_active',
        'content': """
    <section class="section-padding" style="margin-top: 4rem;">
        <div class="container">
            <div class="contact-wrapper">
                <div class="contact-info">
                    <h3 class="sub-section-title">CONTACT US</h3>
                    <h1 style="font-size: 2.5rem; color: var(--primary-navy); margin-bottom: 2rem; line-height: 1.2;">Let's Create Something<br>Exceptional Together</h1>
                    <p style="margin-bottom: 3rem;">Get in touch with our corporate specialist<br>to discuss your uniform requirements.</p>
                    
                    <h4 style="font-size: 1rem; color: var(--primary-navy); margin-bottom: 1.5rem; text-transform: uppercase;">CONTACT DETAILS</h4>
                    
                    <div style="margin-bottom: 1.5rem;">
                        <strong style="color: var(--primary-navy); display: block; margin-bottom: 0.2rem;">Subha Devi</strong>
                        <span style="color: var(--text-gray); font-size: 0.9rem;">Corporate Specialist</span>
                    </div>
                    
                    <p><i class="fa-regular fa-envelope" style="color: var(--primary-navy); margin-right: 10px;"></i> subhadevi@cratus.in</p>
                    <p><i class="fa-solid fa-phone" style="color: var(--primary-navy); margin-right: 10px;"></i> +91 88846 71299</p>
                </div>
                
                <div class="contact-form">
                    <h4 style="font-size: 1rem; color: var(--primary-navy); margin-bottom: 1.5rem; text-transform: uppercase;">SEND US A MESSAGE</h4>
                    <form>
                        <input type="text" class="form-control" placeholder="Your Name">
                        <input type="text" class="form-control" placeholder="Company Name">
                        <input type="email" class="form-control" placeholder="Email Address">
                        <input type="tel" class="form-control" placeholder="Phone Number">
                        <textarea class="form-control" placeholder="Your Message"></textarea>
                        <button type="submit" class="btn btn-primary" style="width: 100%; padding: 12px;">Send Message</button>
                    </form>
                </div>
            </div>
        </div>
    </section>
"""
    }
}

for filename, data in pages.items():
    opts = {
        'home_active': '', 'about_active': '', 'corp_active': '', 
        'scrubs_active': '', 'mat_active': '', 'cust_active': '', 'cont_active': ''
    }
    opts[data['active']] = 'class="active"'
    
    full_html = header.format(title=data['title'], **opts) + data['content'] + footer
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(full_html)
