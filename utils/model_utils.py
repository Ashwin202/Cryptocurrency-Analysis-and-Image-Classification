import numpy as np
from tensorflow.keras.models import load_model as keras_load_model

def load_model(model_path):
    return keras_load_model(model_path)

def make_prediction(model, preprocessed_image):
    prediction = model.predict(preprocessed_image)
    predicted_number = np.argmax(prediction, axis=1)[0]
    confidence_val = np.max(prediction)
    return predicted_number, confidence_val
