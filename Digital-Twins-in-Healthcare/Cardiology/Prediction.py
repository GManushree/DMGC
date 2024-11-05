import pickle
import numpy as np
import pandas as pd

def load_model(file_path='heart_condition_model.pkl'):
    with open(file_path, 'rb') as f:
        model, label_encoder = pickle.load(f)
    return model, label_encoder

def predict_heart_condition(heart_rate, model, label_encoder):
    heart_rate_df = pd.DataFrame({'HeartRate': [heart_rate]})
    prediction = model.predict(heart_rate_df)
    prediction_label = label_encoder.inverse_transform(prediction)
    return prediction_label[0]

if __name__ == "__main__":
    model, label_encoder = load_model()
    print("Enter heart rate: ", end="", flush=True)
    heart_rate = int(input())
    prediction = predict_heart_condition(heart_rate, model, label_encoder)
    print(f"Predicted condition for heart rate {heart_rate}: {prediction}")
