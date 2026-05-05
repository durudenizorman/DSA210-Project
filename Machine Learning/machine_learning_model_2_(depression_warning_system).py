import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns

print("--- Specific Side Effect Prediction (Depression Warning System) ---")

# 1. Load data
df_fda = pd.read_csv("isotretinoin_project_data.csv")
df_spec = df_fda.dropna(subset=['patient_age', 'gender', 'dosage_mg', 'side_effects']).copy()

# 2. Target Variable: Does the patient have Depression? (1 = Yes, 0 = No)
# We use Regex to catch words like 'Depression', 'Depressed mood', etc.
df_spec['has_depression'] = df_spec['side_effects'].str.contains(r'depress', case=False, na=False).astype(int)
df_spec['gender_encoded'] = df_spec['gender'].map({'Male': 1, 'Female': 0})

X_spec = df_spec[['patient_age', 'gender_encoded', 'dosage_mg']]
y_spec = df_spec['has_depression']

# 3. Train/Test Split
X_train_sp, X_test_sp, y_train_sp, y_test_sp = train_test_split(X_spec, y_spec, test_size=0.2, random_state=42)

# 4. Train Model (Using balanced weights because Depression is a minority class)
clf_spec = RandomForestClassifier(n_estimators=100, max_depth=3, class_weight='balanced', random_state=42)
clf_spec.fit(X_train_sp, y_train_sp)
preds_spec = clf_spec.predict(X_test_sp)

# 5. Print Results
acc_spec = accuracy_score(y_test_sp, preds_spec)
print(f"Training size: {len(X_train_sp)} | Test size: {len(X_test_sp)}")
print(f"Accuracy Score for predicting Depression: {acc_spec:.2%}")
print("\nClassification Report (Depression):")
print(classification_report(y_test_sp, preds_spec, target_names=['No Depression', 'Has Depression'], zero_division=0))

# 6. Feature Importance specifically for Depression
feat_imp = clf_spec.feature_importances_
feat_names = ['Patient Age', 'Gender (Male=1)', 'Daily Dosage (mg)']

plt.figure(figsize=(8, 4))
sns.barplot(x=feat_imp, y=feat_names, hue=feat_names, palette='crest', legend=False)
plt.title('Feature Importance: Predicting Depression Risk')
plt.xlabel('Importance Score')
plt.tight_layout()
plt.show()
