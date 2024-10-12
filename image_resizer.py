from PIL import Image
import os

# Function to resize an image
def resize_image(input_path, output_path, size):
    try:
        with Image.open(input_path) as img:
            # Resize image while maintaining aspect ratio
            img = img.resize(size, Image.Resampling.LANCZOS)
            img.save(output_path)
            print(f"Image successfully resized and saved to {output_path}")
    except Exception as e:
        print(f"Error resizing image: {e}")

# Example Usage
if __name__ == "__main__":
    # Input and output paths
    input_image_path = "input_image.jpg"
    output_image_path = "resized_image.jpg"

    # New size (width, height)
    new_size = (800, 600)

    # Resize the image
    resize_image(input_image_path, output_image_path, new_size)
