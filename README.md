# Quantitative Analysis of Isotretinoin Dosage on Side Effect Severity and Patient Sentiment

**DSA 210 - Introduction to Data Science**
**Sabancı University (Fall 2025-2026)**
**Student:** Duru Deniz Orman  

---

## 1. Project Motivation & Goals
Isotretinoin is highly effective for treating severe acne, yet it carries a significant burden of side effects. The dosage used in the treatment plays a crucial role in the patient's experience. As a student currently undergoing this treatment, my primary motivation is to apply data science methodologies to determine if there is a statistical causation and/or correlation between daily dosage levels, the intensity (severity) of reported side effects, and overall patient sentiment. 

Ultimately, my goal is to utilize these findings to create a **predictive machine learning model** that helps anticipate and manage symptoms beforehand based on patient characteristics and dosage.

## 2. Data Collection (Enrichment)
To ensure a robust analysis and meet the project's data enrichment requirement, two distinct public datasets were integrated:

1. **FDA Adverse Event Reports (FAERS):** Extracted via Python API. The initial query retrieved 3,000 raw clinical records, which were subsequently cleaned to remove missing values. This resulted in a robust dataset of over 1,200 pristine clinical records detailing patient age, gender, prescribed dosage (mg), and specific adverse reactions.
2. **Drugs.com Patient Reviews:** Sourced from the publicly available "Drugs.com" dataset on Kaggle. The raw dataset was programmatically filtered to isolate records specifically related to the active ingredient 'Isotretinoin'. Furthermore, Natural Language Processing (Regex) was utilized to extract numerical daily dosages directly from these unstructured patient narratives.

## 3. Exploratory Data Analysis (EDA)
During the initial EDA phase, the focus was on data cleaning and feature engineering:
* A quantitative `severity_score` was created by counting the distinct number of side effects reported by each patient in the FDA dataset.
* Visualizations revealed that patient dosages are heavily clustered around 20mg, 40mg, and 60mg daily intakes, while the patient age distribution skews towards the 15-25 demographic.

## 4. Hypothesis Testing (April 14 Deliverable)
Three formal hypotheses were tested to validate the core assumptions of the project:

* **H1 (Dosage vs. Severity):** Tested the correlation between daily dosage and the severity score.
  * *Result:* No strong linear correlation found (p > 0.05). Side effect severity appears to be influenced by individual biological factors rather than raw dosage alone.
* **H2 (Dosage vs. Sentiment):** Tested the relationship between extracted dosage and patient satisfaction ratings.
  * *Result:* No negative correlation found. Patients report high satisfaction despite high dosages, indicating that the drug's efficacy outweighs its side effects.
* **H3 (Gender vs. Severity):** Conducted an Independent T-Test to compare side effect severity between genders.
  * *Result:* **Statistically Significant (p = 0.004).** Male patients report a significantly higher average number of side effects (3.34) compared to female patients (2.75).

## 5. Key Findings
The most striking finding from this phase is the "Gender Gap." While increasing the raw dosage does not linearly increase the number of side effects, biological sex plays a statistically significant role in treatment tolerance. This finding validates the initial motivation to create a predictive model, as Gender will serve as a crucial feature, alongside Age and Dosage, in anticipating side effect severity.

---

## 6. AI Assistance Disclosure
AI tools (LLMs) were utilized strictly for assisting with Regex pattern formulation for text extraction, generating visualization boilerplate code, and reviewing the documentation, in accordance with the academic integrity guidelines.
