import "./App.css";
import { useState } from "react";
import axios from "axios";

function App() {

  const [file, setFile] = useState(null);

  const [skills, setSkills] = useState([]);
  const [careerMatch, setCareerMatch] = useState(null);
  const [roadmap, setRoadmap] = useState(null);

  const [questions, setQuestions] = useState([]);
  const [role, setRole] = useState("");

  const [resumeScore, setResumeScore] = useState(null);

  const [suggestions, setSuggestions] = useState([]);
  const [suggestionRole, setSuggestionRole] = useState("");

  const uploadResume = async () => {

    try {

      const formData = new FormData();
      formData.append("file", file);

      // Upload Resume
      const response = await axios.post(
        "http://127.0.0.1:8000/upload-resume",
        formData
      );

      setSkills(response.data.skills);

      // Career Match
      const careerResponse = await axios.get(
        "http://127.0.0.1:8000/career-match"
      );

      setCareerMatch(careerResponse.data);

      // Roadmap
      const roadmapResponse = await axios.get(
        "http://127.0.0.1:8000/learning-roadmap"
      );

      setRoadmap(roadmapResponse.data);

      // Interview Questions
      const interviewResponse = await axios.get(
        "http://127.0.0.1:8000/interview-questions"
      );

      setRole(interviewResponse.data.role);
      setQuestions(interviewResponse.data.questions);

      // Resume Score
      const scoreResponse = await axios.get(
        "http://127.0.0.1:8000/resume-score"
      );

      setResumeScore(scoreResponse.data.score);

      // Suggestions
      const suggestionResponse = await axios.get(
        "http://127.0.0.1:8000/suggestions"
      );

      setSuggestionRole(
        suggestionResponse.data.role
      );

      setSuggestions(
        suggestionResponse.data.suggestions
      );

    } catch (error) {
      console.error(error);
      alert("Something went wrong!");
    }
  };

  const downloadReport = () => {

    window.open(
      "http://127.0.0.1:8000/download-report",
      "_blank"
    );
  };

  return (
    <div className="container">

      <h1>🚀 IntelliCareer AI</h1>

      <p
        style={{
          textAlign: "center",
          marginBottom: "30px"
        }}
      >
        AI-Powered Career Guidance Platform
      </p>

      {/* Resume Upload */}
      <div className="card">

        <h2>📄 Resume Upload</h2>

        <input
          type="file"
          onChange={(e) =>
            setFile(e.target.files[0])
          }
        />

        <button onClick={uploadResume}>
          Upload Resume
        </button>

      </div>

      {/* Skills */}
      <div className="card">

        <h2>🛠 Detected Skills</h2>

        <ul>
          {skills.map((skill, index) => (
            <li key={index}>
              {skill}
            </li>
          ))}
        </ul>

      </div>

      {/* Resume Score */}
      <div className="card">

        <h2>📊 Resume Score</h2>

        {resumeScore !== null && (
          <>
            <div className="score-circle">
              {resumeScore}/100
            </div>

            <p>
              Overall Resume Strength
            </p>
          </>
        )}

      </div>

      {/* Career Match */}
      <div className="card">

        <h2>🎯 Career Match</h2>

        {careerMatch && (
          <>
            <div className="role">
              🎯 {careerMatch.target_role}
            </div>

            <div className="score">
              {careerMatch.match_score}%
            </div>

            <h3>Missing Skills</h3>

            <ul>
              {careerMatch.missing_skills.map(
                (skill, index) => (
                  <li key={index}>
                    {skill}
                  </li>
                )
              )}
            </ul>
          </>
        )}

      </div>

      {/* Roadmap */}
      <div className="card">

        <h2>📚 Learning Roadmap</h2>

        {roadmap && (
          <ul>
            {Object.entries(roadmap).map(
              ([month, skill]) => (
                <li
                  key={month}
                  className="roadmap-item"
                >
                  📚 {month} → {skill}
                </li>
              )
            )}
          </ul>
        )}

      </div>

      {/* Interview Questions */}
      <div className="card">

        <h2>🎤 Interview Questions</h2>

        {questions.length > 0 && (
          <>
            <p>
              <strong>Role:</strong> {role}
            </p>

            <ul>
              {questions.map(
                (question, index) => (
                  <li key={index}>
                    {question}
                  </li>
                )
              )}
            </ul>
          </>
        )}

      </div>

      {/* AI Suggestions */}
      <div className="card">

        <h2>💡 AI Suggestions</h2>

        {suggestions.length > 0 && (
          <>
            <p>
              <strong>Role:</strong>{" "}
              {suggestionRole}
            </p>

            <ul>
              {suggestions.map(
                (item, index) => (
                  <li key={index}>
                    ✅ {item}
                  </li>
                )
              )}
            </ul>
          </>
        )}

      </div>

      {/* PDF Report */}
      <div className="card">

        <h2>📄 Career Report</h2>

        <p>
          Download a complete career analysis report
          including score, roadmap, interview
          questions and suggestions.
        </p>

        <button
          className="report-btn"
          onClick={downloadReport}
        >
          Download PDF Report
        </button>

      </div>

    </div>
  );
}

export default App;