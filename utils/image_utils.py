from PIL import Image, ImageOps
import numpy as np

def convert_rgba_to_rgb(image):
    if image.mode == 'RGBA':
        image = image.convert("RGBA")
        canvas = Image.new('RGB', image.size, (255, 255, 255))
        canvas.paste(image, mask=image.split()[3]) 
        image = canvas
    return image

def convert_to_grayscale(image):
    if image.mode in ['LA', 'P']:
        image = ImageOps.grayscale(image.convert('RGBA'))
    return image

def resize_image(image):
    aspect_ratio = min(28 / image.size[0], 28 / image.size[1])
    new_size = (int(image.size[0] * aspect_ratio), int(image.size[1] * aspect_ratio))
    image = image.resize(new_size, Image.LANCZOS)
    return image

def center_image(image):
    background = Image.new('L', (28, 28), 255)
    background.paste(image, (int((28 - image.size[0]) / 2), int((28 - image.size[1]) / 2)))
    return background

def invert_image(image):
    inverted_image = ImageOps.invert(image)
    return inverted_image

def normalize_image(image_array):
    image_array = image_array.astype(np.float32) / 255.0
    return image_array

def expand_dims(image_array):
    image_array = np.expand_dims(image_array, axis=-1)
    image_array = np.expand_dims(image_array, axis=0)
    return image_array

def preprocess_image(image):
    image = convert_rgba_to_rgb(image)
    image = convert_to_grayscale(image)
    image = resize_image(image)
    image = center_image(image)
    image = invert_image(image)
    
    image_array = np.asarray(image)
    image_array = normalize_image(image_array)
    image_array = expand_dims(image_array)
    
    return image_array
