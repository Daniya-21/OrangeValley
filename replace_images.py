import os
import re

replacements = {
    'index.html': [
        (r'https://images.unsplash.com/photo-1629450348780-[^"]+', 'assets/images/hero-home.jpg'),
        (r'https://images.unsplash.com/photo-1596755094514-[^"]+', 'assets/images/corporate-collection.jpg'),
        (r'https://images.unsplash.com/photo-1584515979956-[^"]+', 'assets/images/scrubs-collection.jpg'),
        (r'https://images.unsplash.com/photo-1602810318383-[^"]+', 'assets/images/style-1.jpg'),
        (r'https://images.unsplash.com/photo-1598033129183-[^"]+', 'assets/images/style-2.jpg'),
        (r'https://images.unsplash.com/photo-1579684385127-[^"]+', 'assets/images/scrub-1.jpg'),
        (r'https://images.unsplash.com/photo-1584982751601-[^"]+', 'assets/images/scrub-2.jpg'),
    ],
    'corporate.html': [
        (r'https://images.unsplash.com/photo-1596755094514-[^"]+', 'assets/images/corporate-hero.jpg'),
        (r'https://images.unsplash.com/photo-1602810318383-[^"]+', 'assets/images/style-1.jpg'),
        (r'https://images.unsplash.com/photo-1598033129183-[^"]+', 'assets/images/style-2.jpg'),
        (r'assets/images/corporate-hero\.jpg', 'assets/images/style-3.jpg'), # Since I mapped the same unsplash link for both
        (r'https://images.unsplash.com/photo-1629450348780-[^"]+', 'assets/images/style-4.jpg'),
    ],
    'scrubs.html': [
        (r'https://images.unsplash.com/photo-1584515979956-[^"]+', 'assets/images/scrubs-hero.jpg'),
        (r'https://images.unsplash.com/photo-1579684385127-[^"]+', 'assets/images/scrubs-men.jpg'),
        (r'https://images.unsplash.com/photo-1584982751601-[^"]+', 'assets/images/scrubs-women.jpg'),
        (r'assets/images/scrubs-hero\.jpg', 'assets/images/scrubs-unisex.jpg'), # Need to handle same URL mapping
    ],
    'about.html': [
        (r'https://images.unsplash.com/photo-1486406146926-[^"]+', 'assets/images/about-building.jpg'),
    ],
    'customization.html': [
        (r'https://images.unsplash.com/photo-1556740758-[^"]+', 'assets/images/gallery-1.jpg'),
        (r'https://images.unsplash.com/photo-1556742049-[^"]+', 'assets/images/gallery-2.jpg'),
        (r'https://images.unsplash.com/photo-1556741533-[^"]+', 'assets/images/gallery-3.jpg'),
        (r'https://images.unsplash.com/photo-1584982751601-[^"]+', 'assets/images/gallery-4.jpg'),
        (r'https://images.unsplash.com/photo-1579684385127-[^"]+', 'assets/images/gallery-5.jpg'),
        (r'https://images.unsplash.com/photo-1584515979956-[^"]+', 'assets/images/gallery-6.jpg'),
    ]
}

for filename, rules in replacements.items():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Specific fixes for duplicated urls before regex replacements
        if filename == 'corporate.html':
            # 1st occurrence is the hero image, 3rd occurrence is style-3
            content = content.replace('https://images.unsplash.com/photo-1596755094514-f87e32f85e2c?auto=format&fit=crop&w=400&q=80', 'assets/images/corporate-hero.jpg', 1)
            content = content.replace('https://images.unsplash.com/photo-1596755094514-f87e32f85e2c?auto=format&fit=crop&w=300&q=80', 'assets/images/style-3.jpg')
            
        if filename == 'scrubs.html':
             # 1st occurrence is the hero image, 3rd occurrence is unisex
             content = content.replace('https://images.unsplash.com/photo-1584515979956-d9f6e5d09982?auto=format&fit=crop&w=400&q=80', 'assets/images/scrubs-hero.jpg', 1)
             content = content.replace('https://images.unsplash.com/photo-1584515979956-d9f6e5d09982?auto=format&fit=crop&w=400&q=80', 'assets/images/scrubs-unisex.jpg')
             
        for pattern, replacement in rules:
            content = re.sub(pattern, replacement, content)
            
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
