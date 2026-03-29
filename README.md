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

│── Project Report

│── README.md


## Dataset

Source: Kaggle (Phishing Email Dataset)

Contains:
Email text/content
Labels (Phishing = 1, Safe = 0)

The dataset is placed inside:
Data/Phishing_Email.csv

## How It Works
The script uses a weighted scoring system:
* *Keywords:* +1 point per match.
* *Links:* +2 points.
* *Formatting (Caps):* +1 point.

## Technologies Used

* Python 3
* Basic string processing

## How to Run

1. Make sure Python is installed

2. Clone this repository:

   bash
   git clone https://github.com/your-username/AIML-Project.git
   cd AIML-Project
   
3. Run the script:

   bash
   python phishing_email_detector.py
   
4. Enter an email/message when prompted

## Example

*Input:*


URGENT! Click here to verify your account: http://fake-link.com


*Output:*


High Risk: This looks like a phishing email!
Risk Score: 5

## Project Structure


AIML-Project/
│── phishing_email_detector.py
│── README.md
│── Project Report.docx

## Author

* Vartika Tomar








