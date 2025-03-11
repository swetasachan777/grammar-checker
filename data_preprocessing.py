import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path)
    df = df.dropna()  # Remove empty rows
    df = df[['Incorrect Sentence', 'Correct Sentence']]  # Select required columns
    return df

if __name__ == "__main__":
    dataset = load_data("grammar_correction.csv")
    print(dataset.head())  # Preview dataset
