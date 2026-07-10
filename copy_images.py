import os
import shutil
import glob

source_dir = r"C:\Users\daniy\.gemini\antigravity-ide\brain\7318fbe3-e29d-4959-b54f-7884c1c30615"
dest_dir = r"c:\Users\daniy\OneDrive\Desktop\OrangeValley\assets\images"

os.makedirs(dest_dir, exist_ok=True)

# Find the latest generated files
def get_latest(prefix):
    files = glob.glob(os.path.join(source_dir, f"{prefix}*.png"))
    return sorted(files)[-1] if files else None

src_shirt_stack = get_latest("shirt_stack")
src_scrubs = get_latest("scrubs_models")
src_white = get_latest("mannequin_white")
src_grey = get_latest("mannequin_grey")
src_lightblue = get_latest("mannequin_lightblue")
src_darkblue = get_latest("mannequin_darkblue")

# Map to what HTML expects
mappings = {
    'corporate-collection.jpg': src_shirt_stack,
    'scrubs-collection.jpg': src_scrubs,
    'scrubs-hero.jpg': src_scrubs,
    'scrubs-men.jpg': src_scrubs,
    'scrubs-women.jpg': src_scrubs,
    'scrubs-unisex.jpg': src_scrubs,
    'scrub-1.jpg': src_scrubs,
    'scrub-2.jpg': src_scrubs,
    'style-1.jpg': src_white,
    'style-2.jpg': src_grey,
    'style-3.jpg': src_lightblue,
    'style-4.jpg': src_darkblue,
    'hero-home.jpg': src_lightblue,
    'corporate-hero.jpg': src_white,
    'about-building.jpg': src_shirt_stack,
    'gallery-1.jpg': src_white,
    'gallery-2.jpg': src_grey,
    'gallery-3.jpg': src_lightblue,
    'gallery-4.jpg': src_darkblue,
    'gallery-5.jpg': src_scrubs,
    'gallery-6.jpg': src_shirt_stack,
}

for dest_name, src_path in mappings.items():
    if src_path and os.path.exists(src_path):
        dest_path = os.path.join(dest_dir, dest_name)
        shutil.copy2(src_path, dest_path)
        print(f"Copied {src_path} to {dest_path}")
    else:
        print(f"Warning: Source for {dest_name} not found.")
