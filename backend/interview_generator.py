INTERVIEW_QUESTIONS = {
    "Data Analyst": [
        "What is SQL JOIN?",
        "Explain Data Cleaning.",
        "What is Power BI?",
        "Difference between SQL and NoSQL?"
    ],

    "AI Engineer": [
        "What is Machine Learning?",
        "What is Overfitting?",
        "Explain Neural Networks.",
        "Difference between AI and ML?"
    ],

    "Java Developer": [
        "What is JVM?",
        "What is Spring Boot?",
        "Difference between HashMap and HashSet?",
        "Explain OOP concepts."
    ],

    "Cyber Security Analyst": [
        "What is a Firewall?",
        "Difference between IDS and IPS?",
        "What is SQL Injection?",
        "Explain Phishing attacks."
    ]
}

def generate_questions(role):
    return INTERVIEW_QUESTIONS.get(role, [])