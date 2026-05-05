import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

print("--- MODEL 2: Kaggle Reviews Data (Satisfaction Classification) ---")

# 1. Load the data
df_rev = pd.read_csv("isotretinoin_reviews.csv")

# 2. Extract dosage using NLP (Regex)
df_rev['extracted_dosage_mg'] = df_rev['review'].astype(str).str.extract(r'([0-9]{2,3})\s?[mM][gG]').astype(float)
df_rev_ml = df_rev.dropna(subset=['extracted_dosage_mg', 'rating']).copy()

# 3. Classification logic: Rating 8-10 = High Satisfaction (1), 1-7 = Low Satisfaction (0)
df_rev_ml['satisfaction_level'] = df_rev_ml['rating'].apply(lambda x: 1 if x >= 8 else 0)

X_rev = df_rev_ml[['extracted_dosage_mg']]
y_rev = df_rev_ml['satisfaction_level']

X_train_rev, X_test_rev, y_train_rev, y_test_rev = train_test_split(X_rev, y_rev, test_size=0.2, random_state=42)

# 4. Train the model
clf_rev = RandomForestClassifier(n_estimators=100, max_depth=3, random_state=42)
clf_rev.fit(X_train_rev, y_train_rev)
preds_rev = clf_rev.predict(X_test_rev)

# 5. Print the results
acc_rev = accuracy_score(y_test_rev, preds_rev)
print(f"Training size: {len(X_train_rev)} | Test size: {len(X_test_rev)}")
print(f"Accuracy Score: {acc_rev:.2%}")
