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


