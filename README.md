# Quantitative Analysis of Isotretinoin Dosage on Side Effect Severity and Patient Sentiment

**DSA 210 - Introduction to Data Science**
**Sabancı University (Fall 2025-2026)**
**Student:** Duru Deniz Orman  

---

## Project Motivation & Goals
Isotretinoin is highly effective for treating severe acne, yet it carries a significant burden of side effects. The dosage used in the treatment plays a crucial role in the patient's experience. As a student currently undergoing this treatment, my primary motivation is to apply data science methodologies to determine if there is a statistical causation and/or correlation between daily dosage levels, the intensity (severity) of reported side effects, and overall patient sentiment. 

Ultimately, my goal is to utilize these findings to create a **predictive machine learning model** that helps anticipate and manage symptoms beforehand based on patient characteristics and dosage.


## Repository Structure
``` 
├── Data Preprocessing & Fetching/
│   ├── fda_api_data.py
│   └── reading_data_kaggle.py
├── Machine Learning/
│   ├── machine_learning_model_1_balanced.py
│   ├── machine_learning_model_2_(depression_warning_system).py
│   └── machine_learning_model_3.py
├── data/
│   ├── isotretinoin_project_data.csv
│   └── isotretinoin_reviews.csv
├── DSA 210 Project Proposal - Duru Deniz Orman.pdf 
├── HT_EDA.py
├── README.md
├── figures.png
└── requirements.txt
``` 

## Data Collection (Enrichment)
To ensure a robust analysis and meet the project's data enrichment requirement, two distinct public datasets were integrated:

1. **FDA Adverse Event Reports (FAERS):** Extracted via Python API. The initial query retrieved 3,000 raw clinical records, which were subsequently cleaned to remove missing values. This resulted in a robust dataset of over 1,200 pristine clinical records detailing patient age, gender, prescribed dosage (mg), and specific adverse reactions.
2. **Drugs.com Patient Reviews:** Sourced from the publicly available "Drugs.com" dataset on Kaggle. The raw dataset was programmatically filtered to isolate records specifically related to the active ingredient 'Isotretinoin'. Furthermore, Natural Language Processing (Regex) was utilized to extract numerical daily dosages directly from these unstructured patient narratives.

## Exploratory Data Analysis (EDA)
During the initial EDA phase, the focus was on data cleaning and feature engineering:
* A quantitative `severity_score` was created by counting the distinct number of side effects reported by each patient in the FDA dataset.
* Visualizations revealed that patient dosages are heavily clustered around 20mg, 40mg, and 60mg daily intakes, while the patient age distribution skews towards the 15-25 demographic.

## Hypothesis Testing 
Three formal hypotheses were tested to validate the core assumptions of the project:

* **H1 (Dosage vs. Severity):** Tested the correlation between daily dosage and the severity score.
  * *Result:* No strong linear correlation found (p > 0.05). Side effect severity appears to be influenced by individual biological factors rather than raw dosage alone.
* **H2 (Dosage vs. Sentiment):** Tested the relationship between extracted dosage and patient satisfaction ratings.
  * *Result:* No negative correlation found. Patients report high satisfaction despite high dosages, indicating that the drug's efficacy outweighs its side effects.
* **H3 (Gender vs. Severity):** Conducted an Independent T-Test to compare side effect severity between genders.
  * *Result:* **Statistically Significant (p = 0.004).** Male patients report a significantly higher average number of side effects (3.34) compared to female patients (2.75).

## Findings
The most striking finding from this phase is the "Gender Gap." While increasing the raw dosage does not linearly increase the number of side effects, biological sex plays a statistically significant role in treatment tolerance. This finding validates the initial motivation to create a predictive model, as Gender will serve as a crucial feature, alongside Age and Dosage, in anticipating side effect severity.

## Predictive Modeling (Machine Learning)

In the final phase of the project, I applied Machine Learning models to predict side effect severity and patient sentiment, focusing on three distinct clinical objectives.

### Model 1 = Predicting General Toxicity Risk (Balanced Model)
**Goal:** Predict if a patient falls into a "High Risk" (≥2 side effects) or "Low Risk" (0-1 side effects) category based on Age, Gender, and Raw Dosage.
* **Result:** The balanced Random Forest model achieved an Accuracy of 55.36%.
* **Interpretation:** While standard models achieved an artificially high accuracy by predicting "High Risk" for everyone, the balanced model correctly prioritized identifying minority classes. The modest 55.36% accuracy demonstrates that predicting idiosyncratic drug reactions using only 3 basic features is highly complex.

### Model 2 = Predicting Specific Adverse Events (Depression Warning System)
**Goal:** Create a medical early warning system specifically for Depression, one of the most severe psychological side effects.
* **Result:** The model achieved an overall Accuracy of 53.57%, but a crucial Recall of 0.55 for the Depression class.
* **Interpretation:** In Medical AI, it is clinically safer to over-warn and closely monitor a patient (False Positive) than to miss a severe psychological breakdown (False Negative). Successfully identifying over half (55%) of the high-risk patients proves the value of prioritizing Recall over baseline Accuracy in specific adverse event prediction.

### Model 3 = Predicting Patient Sentiment via NLP
**Goal:** Predict patient satisfaction (Positive/Negative) directly from their raw review texts using a TF-IDF Logistic Regression model.
* **Result:** The model achieved an Accuracy of 64.71%, with a striking 1.00 Recall for Positive reviews and only 0.08 for Negative reviews.
* **Interpretation (Ambivalent Sentiment):** Even patients reporting severe side effects frequently used highly positive "cure" vocabulary (e.g., "miracle", "cleared my severe acne"). This linguistic confusion makes simple text-based classification challenging but perfectly illustrates the complex patient psychology.

## Key Findings 
* **The Gender Gap in Toxicity (Validating H3):** Feature Importance analysis of the balanced FDA model revealed that Gender had a significantly higher importance score than raw Daily Dosage. This mathematically validates that biological sex dictates treatment tolerance far more than a uniform pill size.
* **The Ambivalence of Medical Sentiment:** In medical text mining, patients frequently experience "Ambivalent Sentiment". Even patients reporting severe side effects still used highly positive "cure" vocabulary (e.g., "miracle", "cleared my acne").
* **Efficacy Outweighs Toxicity (Validating H2):** Despite the linguistic confusion, the NLP model successfully captured the overarching trend that patients generally report high satisfaction regardless of the specific dosage.
* **Idiosyncratic Drug Reactions (Validating H1):** The modest 55.3% accuracy in the balanced model demonstrates that side effect severity is highly idiosyncratic and cannot be linearly predicted.
* **Clinical Safety over Algorithmic Accuracy:** In Medical AI, it is clinically safer to be overly cautious and flag everyone as high risk (False Positive) than to completely miss a patient who might suffer severe side effects (False Negative). This ethical algorithmic behavior was successfully demonstrated in our Depression Warning System, which prioritized recall to closely monitor high-risk patients.


## Limitations & Future Work
* **Missing Confounding Variables (Weight):** In clinical dermatology, Isotretinoin is prescribed strictly based on body weight (mg/kg). Because exact patient weight is omitted in public FAERS data due to privacy constraints, "raw dosage" alone lacks the necessary context to serve as a definitive toxicity threshold.
* **Genetics and Lab Results:** Future iterations would require integrating longitudinal patient lab results (e.g., liver enzyme panels) and genetic data to build a highly accurate, clinical-grade predictive model.


## AI Assistance Disclosure
AI tools (LLMs) were utilized strictly for assisting with Regex pattern formulation for text extraction, generating code, and reviewing the documentation, in accordance with the academic integrity guidelines.
