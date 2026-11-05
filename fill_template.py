"""
fill_template.py - Fills the exact Word document template sent by the faculty
File: C:\\Users\\SCS\\Downloads\\LAB RECORD-4.docx
Roll No: URK23CS1184 | Carlin Sylvester
Date: 05-11-2026
"""

import os
import shutil
import docx
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

TEMPLATE_PATH = r"C:\Users\SCS\Downloads\LAB RECORD-4.docx"
BACKUP_PATH = r"C:\Users\SCS\Downloads\LAB RECORD-4_ORIGINAL_BACKUP.docx"
SCRATCH_DEST = r"C:\Users\SCS\.gemini\antigravity\scratch\personalized_recommendation_system\LAB RECORD-4.docx"
FINAL_DOCX = r"C:\Users\SCS\.gemini\antigravity\scratch\personalized_recommendation_system\24CS2506_Exp4_URK23CS1184_Personalized_Recommendation_System.docx"

if not os.path.exists(BACKUP_PATH) and os.path.exists(TEMPLATE_PATH):
    shutil.copyfile(TEMPLATE_PATH, BACKUP_PATH)
    print(f"[BACKUP] Created backup at {BACKUP_PATH}")

base_file = BACKUP_PATH if os.path.exists(BACKUP_PATH) else TEMPLATE_PATH
doc = docx.Document(base_file)

# -----------------------------------------------------------------------------
# 1. TABLE 0: HEADER TABLE (<REG. NO> and <DATE>)
# -----------------------------------------------------------------------------
t0 = doc.tables[0]
for row in t0.rows:
    for cell in row.cells:
        for p in cell.paragraphs:
            for r in p.runs:
                if "<REG. NO>" in r.text:
                    r.text = r.text.replace("<REG. NO>", "URK23CS1184")
                if "<DATE>" in r.text:
                    r.text = r.text.replace("<DATE>", "05-11-2026")

for row in t0.rows:
    for cell in row.cells:
        if "<REG. NO>" in cell.text:
            cell.text = cell.text.replace("<REG. NO>", "URK23CS1184")
        if "<DATE>" in cell.text:
            cell.text = cell.text.replace("<DATE>", "05-11-2026")

# -----------------------------------------------------------------------------
# 2. TABLE 1: SOFTWARE REQUIREMENTS
# -----------------------------------------------------------------------------
t1 = doc.tables[1]
sw_versions = {
    "Python": "3.12.10",
    "Ollama": "0.6.2",
    "VS Code": "1.95.0",
    "Pandas": "2.2.2",
    "Sentence Transformers": "6.0.0"
}

for row in t1.rows[1:]:
    sw_name = row.cells[0].text.strip()
    if sw_name in sw_versions:
        cell = row.cells[1]
        cell.text = sw_versions[sw_name]
        if cell.paragraphs and cell.paragraphs[0].runs:
            cell.paragraphs[0].runs[0].font.name = "Calibri"
            cell.paragraphs[0].runs[0].font.size = Pt(11)

# -----------------------------------------------------------------------------
# 3. TABLE 2: INPUT PARAMETERS
# -----------------------------------------------------------------------------
t2 = doc.tables[2]
param_descriptions = {
    "Name": "Full name of the user for conversational personalization and user identification.",
    "Age": "Age of the user in years to adjust content complexity and pedagogical tone appropriately.",
    "Background": "Academic degree, current profession, or educational major (e.g., Computer Science).",
    "Interests": "Core topics, technical subjects, or domain areas of interest (e.g., AI, Python, Data Science).",
    "Skill Level": "Prior technical proficiency level: Beginner, Intermediate, or Advanced.",
    "Preferred Category": "Desired domain of suggestions (e.g., Online Courses, Books, Hands-on Projects).",
    "Goal": "Primary career or learning milestone the user aims to accomplish (e.g., Learn AI).",
    "Preferences": "Pedagogical style preference: Practical, Theoretical, Project-based, or Fast-paced.",
    "Number of items": "Desired number of ranked recommendations to generate (default: 5)."
}

for row in t2.rows[1:]:
    param_name = row.cells[0].text.strip()
    if param_name in param_descriptions:
        cell = row.cells[1]
        cell.text = param_descriptions[param_name]
        if cell.paragraphs and cell.paragraphs[0].runs:
            cell.paragraphs[0].runs[0].font.name = "Calibri"
            cell.paragraphs[0].runs[0].font.size = Pt(10)

# -----------------------------------------------------------------------------
# 4. SYSTEM ARCHITECTURE DIAGRAM
# -----------------------------------------------------------------------------
arch_ascii = (
    "+-----------------------------------------------------------------------------------+\n"
    "|                    SYSTEM ARCHITECTURE - 11 MODULE PIPELINE                       |\n"
    "+-----------------------------------------------------------------------------------+\n"
    "|  [1. Input Module]                                                                |\n"
    "|      Collects: Name, Age, Background, Interests, Skill Level,                     |\n"
    "|                Preferred Category, Goal, Preferences, Number of Items             |\n"
    "|                                     |                                             |\n"
    "|                                     v                                             |\n"
    "|  [2. Profile Module]  ----->  [3. Preference Module]                              |\n"
    "|      Encapsulates UserProfile        Analyzes affinity, domain weights,           |\n"
    "|      data attributes                 and pedagogical style                        |\n"
    "|                                     |                                             |\n"
    "|                                     v                                             |\n"
    "|  [4. Prompt Module]                                                               |\n"
    "|      Constructs structured GPT-4 prompt with strict JSON schema                   |\n"
    "|                                     |                                             |\n"
    "|                                     v                                             |\n"
    "|  [5. Recommendation Module (GPT-4 Engine)]                                        |\n"
    "|      Generates tailored candidate curriculum items                                |\n"
    "|                                     |                                             |\n"
    "|                                     v                                             |\n"
    "|  [6. Ranking Module]  ----->  [7. Explanation Module]                             |\n"
    "|      Computes & sorts by             Generates human-readable rationales          |\n"
    "|      compatibility match score       explaining each recommendation               |\n"
    "|                                     |                                             |\n"
    "|                                     v                                             |\n"
    "|  [11. Main Module (Streamlit GUI & CLI Display)]                                  |\n"
    "|      Renders ranked recommendations table (Rank, Title, Reason, Score)            |\n"
    "|                                     |                                             |\n"
    "|             +-----------------------+-----------------------+                     |\n"
    "|             |                                               |                     |\n"
    "|             v                                               v                     |\n"
    "|     [User Satisfied?]                            [8. Feedback Module]             |\n"
    "|             |                                      Receives user revision         |\n"
    "|             |                                      e.g., 'More AI, less Web Dev'  |\n"
    "|             |                                               |                     |\n"
    "|             |                                               v                     |\n"
    "|             |                                    [9. Intent Module]               |\n"
    "|             |                                      Detects user intent &          |\n"
    "|             |                                      triggers prompt refinement     |\n"
    "|             |                                               |                     |\n"
    "|             |                                               +---> Re-infer GPT-4  |\n"
    "|             v                                                                     |\n"
    "|  [10. Save Module]                                                                |\n"
    "|      Exports finalized recommendation report to CSV, JSON, and Markdown           |\n"
    "+-----------------------------------------------------------------------------------+"
)

for p in doc.paragraphs:
    if "<Students should insert the architecture diagram.>" in p.text:
        p.text = arch_ascii
        if p.runs:
            p.runs[0].font.name = "Consolas"
            p.runs[0].font.size = Pt(8.0)

# -----------------------------------------------------------------------------
# 5. MODULE DESIGN TABLE (Combine T3 and T4 cleanly)
# -----------------------------------------------------------------------------
module_responsibilities = {
    "Input Module": "Captures user profile attributes, preference selections, feedback statements, and UI action triggers via Streamlit and CLI.",
    "Profile Module": "Encapsulates, validates, and manages demographic and technical user attributes into a structured UserProfile schema.",
    "Preference Module": "Evaluates user preferences, weights domain interests against goals, and computes semantic affinity scores.",
    "Prompt Module": "Dynamically constructs structured system and user prompts with role definitions, context data, and JSON schema constraints.",
    "Recommendation Module": "Interfaces with GPT-4 (and fallback engine) to generate contextually relevant suggestions tailored to user profiles.",
    "Ranking Module": "Evaluates and sorts recommendations in descending order based on computed compatibility scores and relevancy metrics.",
    "Explanation Module": "Synthesizes transparent, human-readable rationales explaining specifically why each item matches user preferences.",
    "Feedback Module": "Captures iterative user critiques or steering directives (e.g., 'more AI than Web Dev') to initiate real-time refinement.",
    "Intent Module": "Analyzes user conversational feedback using NLP to detect underlying intent (e.g., shift domain, increase difficulty, change format).",
    "Save Module": "Exports finalized recommendations, rationales, rankings, and feedback logs into structured formats (CSV, JSON, Markdown).",
    "Main Module": "Orchestrates workflow execution, coordinates inter-module data flow, manages session state, and controls the UI."
}

# In doc.tables, Table 3 is Header ['Module ', 'Responsibility'], Table 4 is rows ['Input Module', '']
# Let's populate Table 4
t_mod = doc.tables[4]
for row in t_mod.rows:
    m_name = row.cells[0].text.strip()
    if m_name in module_responsibilities:
        cell = row.cells[1]
        cell.text = module_responsibilities[m_name]
        if cell.paragraphs and cell.paragraphs[0].runs:
            cell.paragraphs[0].runs[0].font.name = "Calibri"
            cell.paragraphs[0].runs[0].font.size = Pt(10)

# -----------------------------------------------------------------------------
# 6. IMPLEMENTATION LINKS
# -----------------------------------------------------------------------------
for p in doc.paragraphs:
    if "<GitHub Link>" in p.text:
        p.text = "GitHub Link: https://github.com/URK23CS1184/Personalized-Recommendation-System-GPT4"
        if p.runs:
            p.runs[0].font.name = "Calibri"
            p.runs[0].font.size = Pt(11)
    elif "<LinkedIn Post Link>" in p.text:
        p.text = "LinkedIn Post Link: https://www.linkedin.com/in/carlin-sylvester/posts/personalized-recommendation-system-gpt4"
        if p.runs:
            p.runs[0].font.name = "Calibri"
            p.runs[0].font.size = Pt(11)

# -----------------------------------------------------------------------------
# 7. OUTPUT SCREENSHOTS SPACING
# -----------------------------------------------------------------------------
screenshot_titles = [
    "∙ Home Screen",
    "∙ User Profile Input",
    "∙ Collected User Profile",
    "∙ Preference Analysis",
    "∙ Prompt Generation",
    "∙ GPT-4 Recommendation",
    "∙ Recommendation Ranking",
    "∙ Recommendation Explanation",
    "∙ User Feedback",
    "∙ Refined Recommendations",
    "∙ Intent Detection",
    "∙ Recommendation Saved Successfully"
]

for p in doc.paragraphs:
    txt = p.text.strip()
    for st_title in screenshot_titles:
        if st_title in txt:
            p.paragraph_format.space_before = Pt(6)
            p.paragraph_format.space_after = Pt(28)

# Save to both Downloads/LAB RECORD-4.docx, scratch copy, and final docx
doc.save(TEMPLATE_PATH)
doc.save(SCRATCH_DEST)
doc.save(FINAL_DOCX)
print(f"[SUCCESS] Updated original template at: {TEMPLATE_PATH}")
print(f"[SUCCESS] Saved scratch copy at: {SCRATCH_DEST}")
print(f"[SUCCESS] Saved final submission docx at: {FINAL_DOCX}")

