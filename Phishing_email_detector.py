def detect_phishing(email):

    suspicious_keywords = ["urgent", "click", "verify", "free", "win", "account", "password"]

    score = 0

    # Check for suspicious keywords
    for word in suspicious_keywords:
        if word in email.lower():
            score += 1

    # Check for links
    if "http" in email.lower() or "www" in email.lower():
        score += 2

    # Check for ALL CAPS words
    if email.isupper():
        score += 1

    # Result
    if score >= 4:
        print("⚠️ High Risk: This looks like a phishing email!")
    elif score >= 2:
        print("⚠️ Medium Risk: Be careful, this may be suspicious.")
    else:
        print("✅ Low Risk: Seems safe, but stay alert.")

    print("Risk Score:", score)

# Main Program
print("📧 Phishing Email Detector")

email = input("Enter email/message: ")

detect_phishing(email)

import pandas as pd

df = pd.read_csv("Data/Phishing_Email.csv")
print(df.head())

print(df.columns)

X = df['text']     # email content
y = df['label']    # 0 = safe, 1 = phishing

from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()

X_vectorized = vectorizer.fit_transform(X)

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized, y, test_size=0.2
)

model = LogisticRegression()
model.fit(X_train, y_train)




