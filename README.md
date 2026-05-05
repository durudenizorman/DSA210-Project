# Quantitative Analysis of Isotretinoin Dosage on Side Effect Severity and Patient Sentiment

**DSA 210 - Introduction to Data Science**
**Sabancı University (Fall 2025-2026)**
**Student:** Duru Deniz Orman  

---

## Project Motivation & Goals
Isotretinoin is highly effective for treating severe acne, yet it carries a significant burden of side effects. The dosage used in the treatment plays a crucial role in the patient's experience. As a student currently undergoing this treatment, my primary motivation is to apply data science methodologies to determine if there is a statistical causation and/or correlation between daily dosage levels, the intensity (severity) of reported side effects, and overall patient sentiment. 

Ultimately, my goal is to utilize these findings to create a **predictive machine learning model** that helps anticipate and manage symptoms beforehand based on patient characteristics and dosage.

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

I applied Random Forest classification models to test if side effect severity and patient satisfaction could be reliably predicted based solely on Age, Gender, and Raw Dosage.

### Model 1: FDA Data (Risk Level Classification)
**Goal:** Predict whether a patient falls into the "High Risk" (≥2 side effects) or "Low Risk" (0-1 side effects) category based on their demographic and dosage data.

* **Standard Model (Accuracy: 62.50%):** This model suffered from severe Class Imbalance. It achieved artificially high accuracy by predicting "High Risk" for almost everyone, failing to identify "Low Risk" patients. However, in Medical AI, this is often a preferred fallback: it is clinically safer to be overly cautious and flag everyone as high risk (False Positive) than to completely miss a patient who might suffer severe side effects (False Negative).
* **Balanced Model (Accuracy: 55.36%):** I forced the model to learn the minority class by applying `class_weight='balanced'`. While overall accuracy dropped closer to random chance (50%), the model became clinically honest, successfully identifying a significant portion of Low Risk patients.
* **The "Accuracy Paradox" Insight:** The drop from 62.5% to 55.3% is not a failure, but a correction of a biased model. The balanced model mathematically proves that predicting idiosyncratic drug reactions using only 3 basic features is highly limited.

### Model 2: Reviews Data (Patient Satisfaction)
**Goal:** Predict if a patient will rate the drug highly (8-10) based *only* on the numerical dosage extracted via NLP from their text review.

* **Result:** The Random Forest Classifier achieved an Accuracy of 75.00%.
* **Interpretation:** Even with a significantly reduced sample size post-NLP extraction, the model successfully captured the overarching trend that patients generally report high satisfaction regardless of the specific dosage.

## Key Findings (Connecting Hypothesis Tests to ML)
* **Gender is the Strongest Predictor (Validating H3):** Feature Importance analysis of the balanced FDA model revealed that Gender had a significantly higher importance score than raw Daily Dosage. This mathematically validates our initial T-Test hypothesis (H3), confirming that biological sex dictates treatment tolerance far more than a uniform pill size.
* **Predicting Human Biology is Complex (Validating H1):** The modest 55.3% accuracy in the balanced model, along with the low importance of 'Dosage', confirms our initial Pearson Correlation finding (H1). Side effect severity is highly idiosyncratic, influenced by unavailable factors (like weight and genetics) rather than linearly predicted by dosage alone.
* **Efficacy Outweighs Side Effects (Validating H2):** Model 2 successfully predicted patient satisfaction with 75.00% accuracy, reflecting the overarching trend that patients generally report high satisfaction regardless of the specific dosage. This supports our H2 finding that the drug's efficacy often outweighs the perceived severity of side effects.

## Limitations & Future Work
* **Missing Confounding Variables (Weight):** In clinical dermatology, Isotretinoin is prescribed strictly based on body weight (mg/kg). Because exact patient weight is omitted in public FAERS data due to privacy constraints, "raw dosage" alone lacks the necessary context to serve as a definitive toxicity threshold.
* **Genetics and Lab Results:** Future iterations would require integrating longitudinal patient lab results (e.g., liver enzyme panels) and genetic data to build a highly accurate, clinical-grade predictive model.

---

## AI Assistance Disclosure
AI tools (LLMs) were utilized strictly for assisting with Regex pattern formulation for text extraction, generating code, and reviewing the documentation, in accordance with the academic integrity guidelines.
