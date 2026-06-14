SUGGESTIONS = {
    "AI Engineer": [
        "Learn Docker for deployment",
        "Learn AWS cloud services",
        "Build Machine Learning projects",
        "Earn AI certifications"
    ],

    "Data Analyst": [
        "Master SQL queries",
        "Practice Power BI dashboards",
        "Learn Excel advanced features",
        "Build real-world analytics projects"
    ],

    "Java Developer": [
        "Learn Spring Boot",
        "Practice REST APIs",
        "Improve MySQL skills",
        "Build full-stack Java projects"
    ],

    "Cyber Security Analyst": [
        "Practice Linux commands",
        "Learn Network Security",
        "Study Penetration Testing",
        "Complete cybersecurity labs"
    ]
}

def get_suggestions(role):
    return SUGGESTIONS.get(role, [])