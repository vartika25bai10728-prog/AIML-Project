# AIML-Project

# Phishing Email Detector


## Project Overview
This project is an AI-based Phishing Email Detector that identifies whether an email/message is phishing i.e. fake or safe.
Initially built using keyword-based detection, I upgraded the project to use Machine Learning (ML) with a real dataset for better accuracy and adaptability.


## Features

*Detects phishing emails using Machine Learning

*Uses TF-IDF vectorization for text processing

*Trained on a real phishing dataset taken from kaggle

*Provides:

   -Prediction (Phishing / Safe)
   
   -Model accuracy
   
*Simple command-line interface


## Project Structure

AIML-Project/

│── Data/
│   └── Phishing_Email.csv

│── Phishing_email_detector.py

│── ProjectReport.docx

│── README.md


## Dataset

Source: Kaggle (Phishing Email Dataset)

Contains:
Email text/content
Labels (Phishing = 1, Safe = 0)

The dataset is placed inside:
Data/Phishing_Email.csv


## Installation

1. Clone the repository
git clone https://github.com/your-username/AIML-Project.git
cd AIML-Project

2. Install dependencies
pip install pandas scikit-learn


## How to Run

Run the Python file:

Phishing_email_detector.py

Then enter an email/message:

Enter email/message: Your account is locked. Click here to verify.

Output:

⚠️ Phishing Email Detected!
Accuracy: 0.95


## How It Works

1. Data Loading
   
Reads dataset using pandas

2. Text Processing
   
Converts text into numerical form using:
TF-IDF (Term Frequency - Inverse Document Frequency)

3. Model Training
 
Uses Logistic Regression to learn patterns

4. Prediction
   
*Takes user input

*Converts it to vector form

*Predicts phishing or safe


## Author

* Vartika Tomar


## Acknowledgements

Kaggle dataset contributors

Open-source Python libraries







