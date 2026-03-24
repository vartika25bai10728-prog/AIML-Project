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




