import requests
import pandas as pd
import time
import re

def fetch_and_clean_fda_data(total_records=3000):
    print("Fetching data from FDA API. This may take a moment...")
    all_data = []

    for skip in range(0, total_records, 100):
        url = f"https://api.fda.gov/drug/event.json?search=patient.drug.medicinalproduct:isotretinoin&limit=100&skip={skip}"

        try:
            response = requests.get(url)
            if response.status_code != 200:
                break

            results = response.json().get('results', [])
            for record in results:
                patient = record.get('patient', {})
                reactions = [r.get('reactionmeddrapt') for r in patient.get('reaction', []) if r.get('reactionmeddrapt')]
                drugs = patient.get('drug', [])
                iso_drug = [d for d in drugs if 'ISOTRETINOIN' in d.get('medicinalproduct', '').upper()]

                if iso_drug:
                    dosage_text = iso_drug[0].get('drugdosagetext')
                    if dosage_text and str(dosage_text).strip().upper() not in ['NONE', 'UNK', 'UNKNOWN', 'N/A']:
                        all_data.append({
                            'report_id': record.get('safetyreportid'),
                            'dosage_raw': dosage_text,
                            'side_effects': ", ".join(reactions),
                            'patient_age': patient.get('patientonsetage'),
                            'gender': patient.get('patientsex')
                        })
            time.sleep(0.2)

        except Exception as e:
            print(f"Error occurred at skip {skip}: {e}")
            break

    df = pd.DataFrame(all_data)

    if not df.empty:
        df['patient_age'] = pd.to_numeric(df['patient_age'], errors='coerce')
        gender_map = {'1': 'Male', '2': 'Female'}
        df['gender'] = df['gender'].astype(str).map(gender_map)
        df['dosage_mg'] = df['dosage_raw'].str.extract(r'(\d+\.?\d*)').astype(float)
        df = df.dropna(subset=['dosage_mg'])
        df = df[(df['dosage_mg'] > 0) & (df['dosage_mg'] <= 150)]

    return df

df_final = fetch_and_clean_fda_data(3000)

if not df_final.empty:
    csv_name = 'isotretinoin_project_data.csv'
    df_final.to_csv(csv_name, index=False)
    print(f"\nData successfully saved to: {csv_name}")
    print(f"Total cleaned records ready for analysis: {len(df_final)}\n")
    print(df_final.head())
else:
    print("Failed to fetch data. Please check your internet connection or API status.")

