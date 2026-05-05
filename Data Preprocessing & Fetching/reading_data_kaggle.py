import pandas as pd

file_name = "drugs_reviews_kaggle.csv"

print("Scanning dataset to bypass hidden rows...")

skip_lines = 0
separator = ','

with open(file_name, 'r', encoding='utf-8', errors='ignore') as f:
    for i, line in enumerate(f):
        if 'drugName' in line:
            skip_lines = i
            if '\t' in line:
                separator = '\t'
            elif ';' in line:
                separator = ';'
            else:
                separator = ','
            break

print(f"Headers found at line {skip_lines}. Separator used: '{separator}'")

df_raw = pd.read_csv(file_name, sep=separator, skiprows=skip_lines, on_bad_lines='skip', engine='python')

print(f"Total records in raw dataset: {len(df_raw)}")
print("Detected columns:", df_raw.columns.tolist())

df_iso = df_raw[df_raw['drugName'].astype(str).str.contains('isotretinoin', case=False, na=False)]

if 'Unnamed: 0' in df_iso.columns:
    df_iso = df_iso.drop(columns=['Unnamed: 0'])

csv_name = "isotretinoin_reviews.csv"
df_iso.to_csv(csv_name, index=False)

print("\nFiltering successfully completed!")
print(f"A total of {len(df_iso)} isotretinoin reviews have been saved to {csv_name}.")
