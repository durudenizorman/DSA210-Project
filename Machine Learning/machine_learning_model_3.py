import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

print("--- NLP Sentiment Analysis (Text Classification) ---")

# 1. Load the original reviews data
df_rev = pd.read_csv("isotretinoin_reviews.csv")

# 2. Drop empty reviews and ratings
df_nlp = df_rev.dropna(subset=['review', 'rating']).copy()

# 3. Define target: Rating 8-10 = Positive (1), 1-7 = Negative (0)
df_nlp['sentiment'] = df_nlp['rating'].apply(lambda x: 1 if x >= 8 else 0)

# 4. TF-IDF Vectorization (Turning words into numbers)
# We limit to the top 1000 most meaningful words and remove English stop words
vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')
X_text = vectorizer.fit_transform(df_nlp['review'])
y_sentiment = df_nlp['sentiment']

# 5. Train/Test Split
X_train_txt, X_test_txt, y_train_txt, y_test_txt = train_test_split(X_text, y_sentiment, test_size=0.2, random_state=42)

# 6. Train a Logistic Regression model (Highly effective for Text Classification)
clf_nlp = LogisticRegression(class_weight='balanced', random_state=42)
clf_nlp.fit(X_train_txt, y_train_txt)
preds_nlp = clf_nlp.predict(X_test_txt)

# 7. Print Results
acc_nlp = accuracy_score(y_test_txt, preds_nlp)
print(f"Training size: {X_train_txt.shape[0]} | Test size: {X_test_txt.shape[0]}")
print(f"NLP Model Accuracy: {acc_nlp:.2%} (AI successfully reads and understands patient reviews!)")
print("\nClassification Report (Sentiment):")
print(classification_report(y_test_txt, preds_nlp, target_names=['Negative', 'Positive']))
