import sys
from PIL import Image
import os

def crop_image(image_path, output_dir):
    try:
        img = Image.open(image_path)
        width, height = img.size
        
        # Calculate dimensions for 2x2 grid
        half_width = width // 2
        half_height = height // 2
        
        # Define the 4 crop boxes (left, upper, right, lower)
        boxes = {
            'ayi': (0, 0, half_width, half_height),
            'bobo': (half_width, 0, width, half_height),
            'nihao': (0, half_height, half_width, height),
            'ninhao': (half_width, half_height, width, height)
        }
        
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Crop and save each image
        for name, box in boxes.items():
            cropped_img = img.crop(box)
            output_path = os.path.join(output_dir, f"{name}.png")
            cropped_img.save(output_path)
            print(f"Saved {name}.png")
            
    except Exception as e:
        print(f"Error processing image: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python crop_images_lesson_2.py <image_path> <output_dir>")
        sys.exit(1)
        
    image_path = sys.argv[1]
    output_dir = sys.argv[2]
    crop_image(image_path, output_dir)
