# AIML-Project
# Phishing Email Detector

A lightweight Python-based security tool that analyzes email content for common phishing indicators using keyword matching and structural analysis.

## Features
* *Keyword Analysis:* Scans for high-pressure words like "urgent," "verify," and "win."
* *Link Detection:* Identifies the presence of URLs or web addresses.
* *Urgency Check:* Detects if the message is written in all caps.
* *Risk Scoring:* Provides a tiered risk assessment (Low, Medium, High).

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


⚠️ High Risk: This looks like a phishing email!
Risk Score: 5





