import numpy as np
import pandas as pd

def generate_synthetic_data(num_samples=50):
    np.random.seed(42)
    eachSize = num_samples//4

    heart_rates_normal = np.random.randint(60, 100, size=eachSize*2)
    heart_rates_arrhythmia1 = np.random.randint(122, 200, size=eachSize)
    heart_rates_arrhythmia2 = np.random.randint(45, 59, size=eachSize)
    heart_rates_tachycardia = np.random.randint(101, 121, size=eachSize*2)

    heart_rates = np.concatenate([
        heart_rates_normal, 
        heart_rates_arrhythmia1, 
        heart_rates_arrhythmia2, 
        heart_rates_tachycardia
    ])

    diagnoses = np.concatenate([
        np.full(eachSize*2, 'Normal'), 
        np.full(eachSize, 'Arrhythmia'), 
        np.full(eachSize, 'Arrhythmia'), 
        np.full(eachSize*2, 'Tachycardia')
    ])


    data = pd.DataFrame({'HeartRate': heart_rates, 'Diagnosis': diagnoses})
    data = data.sample(frac=1, random_state=42).reset_index(drop=True)
    return data

if __name__ == "__main__":
    data = generate_synthetic_data()
    data.to_csv('synthetic_data_dt.csv', index=False)
    print("Synthetic data generated and saved to 'synthetic_data_dt.csv'")
