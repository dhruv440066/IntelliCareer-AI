def extract_skills(text):

    skills_database = [
        "Python",
        "Java",
        "C++",
        "JavaScript",
        "React",
        "Node.js",
        "Spring Boot",
        "MySQL",
        "SQL",
        "MongoDB",
        "Power BI",
        "Excel",
        "Machine Learning",
        "Data Analysis",
        "Artificial Intelligence",
        "Git",
        "Docker",
        "AWS",
        "Azure"
    ]

    found_skills = []

    text_lower = text.lower()

    for skill in skills_database:
        if skill.lower() in text_lower:
            found_skills.append(skill)

    return found_skills