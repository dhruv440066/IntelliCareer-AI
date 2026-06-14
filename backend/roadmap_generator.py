CAREER_ROLES = {
    "Data Analyst": [
        "Python",
        "SQL",
        "Excel",
        "Power BI",
        "Data Analysis"
    ],

    "AI Engineer": [
        "Python",
        "Machine Learning",
        "Artificial Intelligence",
        "Docker",
        "AWS"
    ],

    "Java Developer": [
        "Java",
        "Spring Boot",
        "MySQL",
        "Git"
    ],

    "Cyber Security Analyst": [
        "Python",
        "Linux",
        "Networking",
        "Cyber Security"
    ]
}

def generate_roadmap(missing_skills):

    roadmap = {}

    month = 1

    for skill in missing_skills:
        roadmap[f"Month {month}"] = skill
        month += 1

    return roadmap

def analyze_career_fit(user_skills, target_role):

    required_skills = CAREER_ROLES.get(target_role, [])

    matched = []
    missing = []

    for skill in required_skills:
        if skill in user_skills:
            matched.append(skill)
        else:
            missing.append(skill)

    if len(required_skills) > 0:
        match_score = int(
            (len(matched) / len(required_skills)) * 100
        )
    else:
        match_score = 0

       

    return {
        "target_role": target_role,
        "match_score": match_score,
        "matched_skills": matched,
        "missing_skills": missing
    }
    

   