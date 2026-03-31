# PHISHING EMAIL DETECTOR 


import pandas as pd
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report



# 1. LOAD DATA


def load_data(path):
    df = pd.read_csv(path, index_col=0)  
    df = df.dropna()

    X = df['Email Text']
    y = df['Email Type']

    return X, y



# 2. TRAIN MODEL


def train_model(X, y):
    vectorizer = TfidfVectorizer()

    X_vectorized = vectorizer.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X_vectorized, y, test_size=0.2, random_state=42
    )

    model = LogisticRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    print("\n Model Evaluation:\n")
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("\nClassification Report:\n")
    print(classification_report(y_test, y_pred))

    return model, vectorizer



# 3. SAVE MODEL


def save_model(model, vectorizer):
    pickle.dump(model, open("model.pkl", "wb"))
    pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))
    print("\n Model saved successfully!")



# 4. LOAD MODEL


def load_model():
    model = pickle.load(open("model.pkl", "rb"))
    vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
    return model, vectorizer



# 5. PREDICT FUNCTION


def predict_email(text, model, vectorizer):
    vectorized_text = vectorizer.transform([text])
    prediction = model.predict(vectorized_text)
    return prediction[0]



# 6. MAIN PROGRAM


def main():
    print(" AI Phishing Email Detector\n")

    import os
    print(os.getcwd())

    # Load and train
    X, y = load_data("AIML-Project/Data/Phishing_Email.csv")
    model, vectorizer = train_model(X, y)

    # Save model
    save_model(model, vectorizer)

    # Load model again (to simulate real use)
    model, vectorizer = load_model()

    # User input loop
    while True:
        print("\n-----------------------------------")
        user_input = input("Enter email (or type 'exit'): ")

        if user_input.lower() == 'exit':
            print("👋 Exiting...")
            break

        result = predict_email(user_input, model, vectorizer)

        print("🔍 Prediction:", result)



# RUN


if __name__ == "__main__":
    main()