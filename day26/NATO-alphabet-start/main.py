import pandas as pd

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
df=pd.read_csv("nato_phonetic_alphabet.csv",skiprows=1,header=None)
data_dict=df.values.tolist()
print(data_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

