from PIL import Image, ImageOps
import numpy as np
from lib.image_classification_fn import *

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
