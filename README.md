# Quantitative Analysis of Isotretinoin Dosage on Side Effect Severity and Patient Sentiment

**DSA 210 - Introduction to Data Science** **Sabancı University (Fall 2025-2026)** **Student:** Duru Deniz Orman  

---

## 1. Project Motivation & Goals
Isotretinoin is one of the most effective treatments for severe acne, yet it carries a significant burden of side effects. [cite_start]As a student currently undergoing this treatment, I noticed that side effect intensity fluctuates with dosage changes[cite: 2]. [cite_start]The primary goal of this project is to apply data science methodologies to determine the statistical relationship between daily dosage levels, side effect severity, and overall patient sentiment[cite: 2].By analyzing public datasets, I aim to create a predictive model that helps manage symptoms beforehand.

The project aims to:
* **Quantify** the relationship between dosage (mg) and the number of side effects.
* **Identify** demographic factors (Age, Gender) that act as catalysts for side effect intensity.
* [cite_start]**Bridge** the gap between clinical reports (FDA) and patient narratives (User Reviews)[cite: 2].

---

## 2. Data Collection & Pipeline
[cite_start]To meet the academic requirements for data enrichment[cite: 1], this project integrates two high-fidelity datasets:

### A. FDA Adverse Event Reports (FAERS)
* **Source:** Extracted using a custom Python script interfacing with the OpenFDA API.
* **Volume:** 3,000+ clinical reports.
* **Variables:** Patient Age, Gender, Dosage (mg/day), and a list of specific Adverse Reactions.

### B. Drugs.com Patient Reviews
* **Source:** Scraped repository of patient experiences.
* **Variables:** Sentiment Rating (1-10), Usefulness Count, and raw review text.
* **NLP Extraction:** Daily dosages were extracted from raw text using Regex-based Natural Language Processing to create a structured dosage variable from unstructured narratives.

---

## 3. Analysis Methodology (April 14 Milestone)
[cite_start]The current phase focused on Data Collection, Exploratory Data Analysis (EDA), and formal Hypothesis Testing[cite: 3].

### Data Preparation
1. **Cleaning:** Removed invalid dosages (UNK, N/A) and outlier ages.
2. **Feature Engineering:** Created a `severity_score` based on the count of distinct side effects per patient.
3. **Sentiment Normalization:** Aligned patient ratings from reviews with clinical severity scores from FDA data.

### Hypothesis Testing Results
| Hypothesis | Description | Test Method | Result |
| :--- | :--- | :--- | :--- |
| **H1 (Dosage vs Severity)** | Does a higher daily dose lead to more side effects? | Pearson Correlation | **Weak Correlation (r=0.01)**. Dosage alone is not a linear predictor of side effect count. |
| **H2 (Dosage vs Sentiment)** | Do higher doses decrease patient satisfaction? | Pearson Correlation | **No Correlation**. Efficacy often outweighs side effects in patient ratings. |
| **H3 (Gender vs Severity)** | Do males and females experience side effects differently? | Independent T-Test | **Significant (P=0.004)**. Males report significantly higher severity (3.34) than females (2.75). |

---

## 4. Key Findings & Exploratory Visualizations
* **The "Gender Gap":** Our findings suggest that biological sex is a stronger predictor of side effect severity than the raw dosage amount. This is a critical finding for the upcoming predictive model.
* **Dosage Clusters:** Most treatments revolve around 20mg, 40mg, and 60mg daily intakes, yet severity remains relatively flat across these clusters, suggesting idiosyncratic reactions are dominant.

---

## 5. Future Work: Machine Learning (May 5 Deliverable)
[cite_start]Building on the April 14 findings[cite: 3], the next phase will focus on:
1. **Severity Prediction (Regression):** Using Age, Gender, and Dosage to predict the expected number of symptoms.
2. **Sentiment Analysis (Classification):** Predicting patient rating categories based on reported side effects.
3. **Model Evaluation:** Comparing Random Forest and Logistic Regression models to identify non-linear relationships in treatment tolerance.

---

## 6. Repository Structure
* `/data`: Raw and cleaned CSV files (FDA & Reviews).
* `/notebooks`: Jupyter notebooks containing the API extraction, EDA, and Hypothesis Testing.
* `/plots`: Visualizations of correlation matrices and gender comparisons.
* `README.md`: Project documentation and roadmap.

---

## 7. Setup & Reproducibility
To reproduce the analysis:
1. Clone the repository: `git clone https://github.com/[username]/[repo-name]`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the analysis notebook: `jupyter notebook notebooks/April_14_Analysis.ipynb`

---

## 8. AI Assistance Disclosure
AI tools (e.g., Gemini) were utilized for:
* Assisting in the extraction logic for FDA API data.
* Structuring the NLP/Regex patterns for dosage extraction from unstructured text.
* [cite_start]Reviewing and refining statistical interpretations and documentation[cite: 3].

---
*This project is submitted as part of the DSA 210 course at Sabancı University, Fall 2025-2026.*
