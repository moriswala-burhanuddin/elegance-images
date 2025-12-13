import os
import json
import time

def generate_gallery_json():
    images_dir = 'images'
    output_file = 'images.json'
    
    # Ensure images dir exists
    if not os.path.exists(images_dir):
        print(f"Error: Directory '{images_dir}' not found.")
        return

    images = []
    valid_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.webp', '.svg'}

    print("Scanning images...")
    for filename in os.listdir(images_dir):
        ext = os.path.splitext(filename)[1].lower()
        if ext in valid_extensions:
            filepath = os.path.join(images_dir, filename)
            stats = os.stat(filepath)
            
            images.append({
                'name': filename,
                'path': f'images/{filename}',
                'size': stats.st_size,
                'created': stats.st_mtime
            })
    
    # Sort by newest first
    images.sort(key=lambda x: x['created'], reverse=True)

    with open(output_file, 'w') as f:
        json.dump(images, f, indent=2)
    
    print(f"Success! Found {len(images)} images. Saved to {output_file}.")

if __name__ == "__main__":
    generate_gallery_json()
