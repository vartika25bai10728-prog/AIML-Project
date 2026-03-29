import pandas as pd

# added dataset imported from kaggle
df = pd.read_csv("Data/Phishing_Email.csv")

print(df.head())
print(df.columns)

X = df['text']      
y = df['label']     

# To see data in more organized way
df = df.dropna()

# To convert text to numbers
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Training my model 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized, y, test_size=0.2
)

model = LogisticRegression()
model.fit(X_train, y_train)

# Improving it's accuracy
accuracy = model.score(X_test, y_test)
print("Accuracy:", accuracy)


# Updated my code to ML-based detection
def predict_email(email_text):
    email_vector = vectorizer.transform([email_text])
    prediction = model.predict(email_vector)

    if prediction[0] == 1:
        print("⚠️ Phishing Email Detected!")
    else:
        print("✅ Safe Email")


# Main program
print("\n📧 AI Phishing Email Detector")

email = input("Enter email/message: ")
predict_email(email)


