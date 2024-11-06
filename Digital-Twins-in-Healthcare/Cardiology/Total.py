import os
import subprocess

def run_script(script_name):
    result = subprocess.run(['python', script_name], capture_output=True, text=True)
    print(result.stdout)

if __name__ == "__main__":
    
    run_script('GenerateData.py')
    
    
    run_script('PreprocessData.py')
    
    
    run_script('TrainModel.py')
    
    
    run_script('Prediction.py')
