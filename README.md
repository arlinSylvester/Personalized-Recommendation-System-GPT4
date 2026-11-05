# Personalized Recommendation System using GPT-4
### Course: 24CS2506 – Building Applications using GPT-4 | Experiment 4
**Student:** Carlin Sylvester | **Register No:** URK23CS1184

---

## 📌 Project Overview
This project implements **Experiment 4: Personalized Recommendation System** for the course *24CS2506 – Building Applications using GPT-4*.

The system demonstrates:
1. **User Profile Ingestion**: Capturing multidimensional preferences (Name, Age, Field, Interests, Skill Level, Preferred Learning Type, and Goal).
2. **Structured Prompt Engineering**: Translating profile parameters into strict prompt templates with JSON schema guarantees.
3. **GPT-4 LLM Cognitive Processing**: Evaluating user preferences, generating top 5 ranked recommendations with natural-language rationales and percentage match scores.
4. **Interactive Feedback Loop**: Allowing users to steer and refine recommendations via conversational feedback (e.g., *"I am more interested in AI than Web Development"*).
5. **Dual-Mode Engine Architecture**: Seamlessly toggles between live OpenAI GPT-4 API and an intelligent built-in laboratory simulator for 100% test reliability with zero API costs.
6. **Academic Reporting**: Automated generation of official Word document (`.docx`) and Markdown (`.md`) lab records.

---

## 📂 Project Structure
```
personalized_recommendation_system/
│
├── recommender.py                 # Core recommendation engine & prompt engineering
├── app.py                         # Streamlit web application
├── cli_test.py                    # Terminal demonstration test script
├── generate_lab_report_docx.py    # Generates 24CS2506_Exp4_...docx lab record
├── run_app.bat                    # One-click Windows batch launcher
├── requirements.txt               # Project dependencies
├── LAB_REPORT_URK23CS1184.md      # Full Markdown lab record
└── 24CS2506_Exp4_URK23CS1184_Personalized_Recommendation_System.docx
```

---

## 🚀 How to Run

### 1. Run the Terminal CLI Demonstration
```bash
python cli_test.py
```
This runs an automated step-by-step test executing Student A's profile, prompt formulation, initial tabular output (matching Section 7 of the lab manual), feedback refinement (Section 6), and Student B's profile.

### 2. Launch the Streamlit Web Application
Double-click `run_app.bat` or run:
```bash
streamlit run app.py
```
Open your browser at `http://localhost:8503` to interact with the GUI, test different user profiles, provide conversational feedback, and download CSV/JSON exports.

### 3. Regenerate Word Document Lab Record (.docx)
```bash
python generate_lab_report_docx.py
```

---

## 📋 Expected Output (Lab Manual Section 7 Compliance)

```
Personalized Recommendations
User: Computer Science student
Interests: AI, Python
Level: Beginner

Rank | Recommendation           | Reason                              | Score
1    | Python for AI            | Matches Python and AI interests     | 95%
2    | Machine Learning Basics   | Suitable for beginner AI learners   | 92%
3    | Generative AI            | Relevant to current AI interests    | 88%
4    | Data Science with Python | Combines Python and data analysis   | 85%
5    | Deep Learning Basics     | Natural progression after ML        | 80%
```

---

## 🔄 Feedback Refinement (Section 6 Compliance)
- **User Feedback:** `"I am more interested in AI than Web Development."`
- **Updated Recommendations:**
  1. Artificial Intelligence (96%)
  2. Machine Learning (93%)
  3. Deep Learning (90%)
  4. Generative AI (87%)
  5. Computer Vision (82%)

