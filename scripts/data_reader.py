import pandas as pd

def read_data(file_path):
    """Reads data from a CSV file."""
    try:
        data = pd.read_csv("E:\\Codtech projects\\Task 2\\automated_report_generation\\data\\sample_data.csv")
        return data
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
