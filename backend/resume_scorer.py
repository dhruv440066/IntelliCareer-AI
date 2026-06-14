def calculate_resume_score(skills):

    score = 0

    score += min(len(skills) * 10, 60)

    bonus_skills = [
        "Python",
        "Java",
        "Machine Learning",
        "Artificial Intelligence",
        "SQL",
        "AWS",
        "Docker"
    ]

    for skill in bonus_skills:
        if skill in skills:
            score += 5

    if score > 100:
        score = 100

    return score