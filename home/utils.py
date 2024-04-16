# ml/utils.py
import joblib

def save_model(model, filepath="trained_model.pkl"):
    """
    Save the trained model to disk.

    Parameters:
    - model: The trained machine learning model object.
    - filepath: The file path where the model will be saved. Default is 'trained_model.pkl'.
    """
    joblib.dump(model, filepath)