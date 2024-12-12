from tensorflow.keras.models import load_model # type: ignore

def load_my_model():
    # Path model
    model_path = 'best_model.h5'
    model = load_model(model_path)
    return model
