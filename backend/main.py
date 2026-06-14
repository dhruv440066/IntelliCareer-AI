from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

from resume_parser import extract_text_from_pdf
from skill_analyzer import extract_skills
from roadmap_generator import (
    analyze_career_fit,
    generate_roadmap,
    CAREER_ROLES
)
from interview_generator import generate_questions
from suggestion_generator import get_suggestions
from resume_scorer import calculate_resume_score
from report_generator import generate_report

import os

latest_skills = []

app = FastAPI(
    title="IntelliCareer AI",
    description="AI Career Assistant",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.get("/")
def home():
    return {
        "message": "Welcome to IntelliCareer AI"
    }


@app.get("/health")
def health():
    return {
        "status": "running"
    }


@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):

    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(file_path, "wb") as f:
        f.write(await file.read())

    extracted_text = extract_text_from_pdf(
        file_path
    )

    skills = extract_skills(
        extracted_text
    )

    global latest_skills
    latest_skills = skills

    return {
        "filename": file.filename,
        "skills": skills,
        "resume_text": extracted_text[:1000]
    }


@app.get("/career-match")
def career_match():

    global latest_skills

    if not latest_skills:
        return {
            "error": "Upload resume first"
        }

    best_role = None
    best_score = 0

    for role, required_skills in CAREER_ROLES.items():

        matched = 0

        for skill in required_skills:
            if skill in latest_skills:
                matched += 1

        score = (
            matched / len(required_skills)
        ) * 100

        if score > best_score:
            best_score = score
            best_role = role

    result = analyze_career_fit(
        latest_skills,
        best_role
    )

    return result


@app.get("/learning-roadmap")
def learning_roadmap():

    global latest_skills

    if not latest_skills:
        return {
            "error": "Upload resume first"
        }

    career_result = career_match()

    roadmap = generate_roadmap(
        career_result["missing_skills"]
    )

    return roadmap


@app.get("/interview-questions")
def interview_questions():

    global latest_skills

    if not latest_skills:
        return {
            "error": "Upload resume first"
        }

    career_result = career_match()

    role = career_result["target_role"]

    questions = generate_questions(role)

    return {
        "role": role,
        "questions": questions
    }


@app.get("/resume-score")
def resume_score():

    global latest_skills

    if not latest_skills:
        return {
            "error": "Upload resume first"
        }

    score = calculate_resume_score(
        latest_skills
    )

    return {
        "score": score
    }


@app.get("/suggestions")
def suggestions():

    global latest_skills

    if not latest_skills:
        return {
            "error": "Upload resume first"
        }

    career_result = career_match()

    role = career_result["target_role"]

    return {
        "role": role,
        "suggestions": get_suggestions(role)
    }


@app.get("/download-report")
def download_report():

    global latest_skills

    if not latest_skills:
        return {
            "error": "Upload resume first"
        }

    career = career_match()

    roadmap = learning_roadmap()

    score = calculate_resume_score(
        latest_skills
    )

    report_data = {
    "Resume Score":
        f"{score}/100",

    "Recommended Career":
        career["target_role"],

    "Career Match Score":
        f"{career['match_score']}%",

    "Missing Skills":
        "<br/>".join(
            career["missing_skills"]
        ),

    "Learning Roadmap":
        "<br/>".join(
            [
                f"{month} → {skill}"
                for month, skill in roadmap.items()
            ]
        ),

    "Interview Questions":
        "<br/>".join(
            generate_questions(
                career["target_role"]
            )
        ),

    "AI Suggestions":
        "<br/>".join(
            get_suggestions(
                career["target_role"]
            )
        )
}

    filename = "career_report.pdf"

    generate_report(
        report_data,
        filename
    )

    return FileResponse(
        path=filename,
        media_type="application/pdf",
        filename=filename
    )