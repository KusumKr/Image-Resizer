# Image-Resizer

This is a simple Python project that resizes images using the `Pillow` library. The script allows you to specify the input image, new dimensions, and save the resized image to a desired location.

## Features
- Resizes images to specified dimensions.
- Maintains high-quality resizing using the `LANCZOS` resampling filter.
- Easy to use and extend for further functionality.

## Prerequisites

To run this project, you'll need:
- **Python 3.x**: [Download Python here](https://www.python.org/downloads/).
- **Pillow Library**: Install it using pip.

## Installation

1. **Clone the repository or download the code:**

   If you have git installed, you can clone the repository:
   ```bash
   git clone <repository-url>

2. **Install the Pillow library:**

   Navigate to the project directory and install the required library:
   ```bash
   pip install pillow

## Usage
1. **Prepare an input image: Place your image in the project directory or specify its path.**

2. **Edit the script: Open the image_resizer.py script and update the following variables as needed:**
   <br>
   <p>input_image_path: The path to the image you want to resize.</p>
   <p>output_image_path: The path where the resized image will be saved.</p>
   <p>new_size: The new size (width, height) you want for the resized image.</p>
   
4. **Run the script: Open a terminal or command prompt, navigate to the project folder, and run:**
   ```bash
   python image_resizer.py
5. **Check the resized image: The resized image will be saved at the location specified in output_image_path.**

   <h4>Example:</h4>
   <p>Input image: input_image.jpg</p>
   <p>Output image: resized_image.jpg</p>
   <p>New size: (800, 600)</p>  
