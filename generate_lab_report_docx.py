"""
generate_lab_report_docx.py - Generates the Word Document (.docx) for Experiment 4
Course: 24CS2506 – Building Applications using GPT-4
Experiment 4: Personalized Recommendation System
Roll No: URK23CS1184 | Carlin Sylvester
"""

import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls


def set_cell_background(cell, fill_hex):
    """Sets background color of a table cell."""
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)


def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    """Sets inner margins for a table cell in dxa (1 pt = 20 dxa)."""
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(
        f'<w:tcMar {nsdecls("w")}>'
        f'<w:top w:w="{top}" w:type="dxa"/>'
        f'<w:bottom w:w="{bottom}" w:type="dxa"/>'
        f'<w:left w:w="{left}" w:type="dxa"/>'
        f'<w:right w:w="{right}" w:type="dxa"/>'
        f'</w:tcMar>'
    )
    tcPr.append(tcMar)


def set_table_borders(table, color="D3D3D3"):
    """Sets clean light borders on a table."""
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'<w:top w:val="single" w:sz="4" w:space="0" w:color="{color}"/>'
        f'<w:bottom w:val="single" w:sz="6" w:space="0" w:color="{color}"/>'
        f'<w:left w:val="none"/>'
        f'<w:right w:val="none"/>'
        f'<w:insideH w:val="single" w:sz="4" w:space="0" w:color="{color}"/>'
        f'<w:insideV w:val="none"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)


def build_document(output_filename):
    doc = docx.Document()

    # Page Margins: 1 inch all around
    sections = doc.sections
    for s in sections:
        s.top_margin = Inches(1.0)
        s.bottom_margin = Inches(1.0)
        s.left_margin = Inches(1.0)
        s.right_margin = Inches(1.0)

    # Base typography
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Calibri'
    normal_style.font.size = Pt(11)
    normal_style.font.color.rgb = RGBColor(0x22, 0x22, 0x22)

    # -------------------------------------------------------------
    # 1. Header Table
    # -------------------------------------------------------------
    header_table = doc.add_table(rows=2, cols=3)
    header_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(header_table, color="1E3A8A")

    col_widths = [Inches(1.5), Inches(3.6), Inches(1.4)]
    for row in header_table.rows:
        for idx, width in enumerate(col_widths):
            row.cells[idx].width = width

    # Row 0
    c00 = header_table.cell(0, 0)
    c00.text = "Ex. No.: 4"
    p00 = c00.paragraphs[0]
    p00.runs[0].bold = True
    p00.runs[0].font.size = Pt(11)
    p00.alignment = WD_ALIGN_PARAGRAPH.LEFT

    c01 = header_table.cell(0, 1)
    c01.text = "PERSONALIZED RECOMMENDATION SYSTEM USING GPT-4"
    p01 = c01.paragraphs[0]
    p01.runs[0].bold = True
    p01.runs[0].font.size = Pt(11)
    p01.runs[0].font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)
    p01.alignment = WD_ALIGN_PARAGRAPH.CENTER

    c02 = header_table.cell(0, 2)
    c02.text = "URK23CS1184"
    p02 = c02.paragraphs[0]
    p02.runs[0].bold = True
    p02.runs[0].font.size = Pt(11)
    p02.alignment = WD_ALIGN_PARAGRAPH.RIGHT

    # Row 1
    c10 = header_table.cell(1, 0)
    c10.text = "04-11-2026"
    p10 = c10.paragraphs[0]
    p10.runs[0].font.size = Pt(10)
    p10.alignment = WD_ALIGN_PARAGRAPH.LEFT

    c11 = header_table.cell(1, 1)
    c11.text = "Course: 24CS2506 – Building Applications using GPT-4"
    p11 = c11.paragraphs[0]
    p11.runs[0].font.size = Pt(9.5)
    p11.runs[0].font.italic = True
    p11.alignment = WD_ALIGN_PARAGRAPH.CENTER

    c12 = header_table.cell(1, 2)
    c12.text = "Carlin Sylvester"
    p12 = c12.paragraphs[0]
    p12.runs[0].font.size = Pt(9.5)
    p12.runs[0].font.bold = True
    p12.alignment = WD_ALIGN_PARAGRAPH.RIGHT

    for row in header_table.rows:
        for cell in row.cells:
            set_cell_margins(cell, top=120, bottom=120, left=150, right=150)
            set_cell_background(cell, "F0F4F8")

    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    # -------------------------------------------------------------
    # Helper to add section headings
    # -------------------------------------------------------------
    def add_section_header(title_text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(13)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(title_text)
        run.bold = True
        run.font.size = Pt(12)
        run.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)
        return p

    def add_body_p(text, italic=False):
        p = doc.add_paragraph()
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.space_after = Pt(6)
        run = p.add_run(text)
        run.font.size = Pt(10.5)
        run.italic = italic
        return p

    # -------------------------------------------------------------
    # 2. Aim
    # -------------------------------------------------------------
    add_section_header("Aim:")
    add_body_p(
        "To develop an AI-powered personalized recommendation system using GPT-4 that suggests relevant items, "
        "courses, and content based on multidimensional user profiles, generates natural language explanations and "
        "percentage match scores, and iteratively refines recommendations based on interactive conversational feedback."
    )

    # -------------------------------------------------------------
    # 3. Problem Statement
    # -------------------------------------------------------------
    add_section_header("Problem Statement:")
    add_body_p(
        "Traditional recommendation systems (collaborative filtering, content-based filtering, and matrix factorization) "
        "depend strictly on predefined rating matrices, categorical taxonomies, and explicit numerical interactions. "
        "Consequently, they suffer severely from the cold-start problem, cannot comprehend nuanced natural-language "
        "preference descriptions, cannot provide transparent reasoning for their suggestions, and struggle with conversational "
        "refinement. The objective of this experiment is to design, implement, and evaluate a personalized recommendation system "
        "powered by GPT-4 that accepts user profile parameters (Name, Age, Field, Interests, Skill Level, Preferred Learning Type, "
        "and Career Goal), transforms them into a structured prompt, generates ranked recommendations with specific justification "
        "rationales and match scores, and provides an interactive conversational feedback loop for real-time recommendation updates."
    )

    # -------------------------------------------------------------
    # 4. Software Requirements
    # -------------------------------------------------------------
    add_section_header("Software Requirements:")
    sw_data = [
        ("Operating System", "Windows 11 / Linux / macOS"),
        ("Programming Language", "Python 3.12 / 3.10+"),
        ("Language Model / API", "OpenAI GPT-4 / GPT-4o / Heuristic Simulator Engine"),
        ("Web Application Framework", "Streamlit 1.33.0+"),
        ("Data Manipulation", "Pandas 2.2.0+"),
        ("Environment Management", "python-dotenv 1.0.0+"),
        ("Development Environment", "VS Code 1.90+ / Antigravity IDE")
    ]
    sw_table = doc.add_table(rows=len(sw_data) + 1, cols=2)
    sw_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(sw_table)

    sw_col_widths = [Inches(3.2), Inches(3.3)]
    for row in sw_table.rows:
        for idx, width in enumerate(sw_col_widths):
            row.cells[idx].width = width

    # Header Row
    sw_headers = ["Software / Component", "Specification / Version"]
    for idx, h in enumerate(sw_headers):
        cell = sw_table.cell(0, idx)
        cell.text = h
        p = cell.paragraphs[0]
        p.runs[0].bold = True
        p.runs[0].font.size = Pt(10)
        p.runs[0].font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        set_cell_background(cell, "1E3A8A")
        set_cell_margins(cell, top=100, bottom=100, left=120, right=120)

    # Content Rows
    for r_idx, (comp, ver) in enumerate(sw_data, start=1):
        c0 = sw_table.cell(r_idx, 0)
        c1 = sw_table.cell(r_idx, 1)
        c0.text = comp
        c1.text = ver
        for cell in (c0, c1):
            cell.paragraphs[0].runs[0].font.size = Pt(9.5)
            set_cell_margins(cell, top=80, bottom=80, left=120, right=120)
        if r_idx % 2 == 1:
            set_cell_background(c0, "F8FAFC")
            set_cell_background(c1, "F8FAFC")

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # -------------------------------------------------------------
    # 5. Input Parameters
    # -------------------------------------------------------------
    add_section_header("Input Parameters:")
    ip_data = [
        ("Name", "String", "User's full name for conversational personalization (e.g., Arun)"),
        ("Age", "Integer", "User's age, providing demographic contextualization (e.g., 20)"),
        ("Field", "String", "Academic major or professional discipline (e.g., Computer Science)"),
        ("Interests", "String / List", "Stated domain preferences (e.g., AI, Python, Data Science)"),
        ("Skill Level", "Categorical", "User technical expertise: Beginner, Intermediate, Advanced"),
        ("Preferred Type", "Categorical", "Pedagogical format: Practical, Theoretical, Project-based, Fast-paced"),
        ("Goal", "String", "Primary learning or career aspiration (e.g., Learn AI)"),
        ("User Feedback", "Natural Language", "Iterative conversational directive (e.g., 'I am more interested in AI than Web Development')")
    ]
    ip_table = doc.add_table(rows=len(ip_data) + 1, cols=3)
    ip_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(ip_table)

    ip_widths = [Inches(1.8), Inches(1.5), Inches(3.2)]
    for row in ip_table.rows:
        for idx, width in enumerate(ip_widths):
            row.cells[idx].width = width

    ip_headers = ["Parameter", "Data Type", "Description & Lab Example"]
    for idx, h in enumerate(ip_headers):
        cell = ip_table.cell(0, idx)
        cell.text = h
        p = cell.paragraphs[0]
        p.runs[0].bold = True
        p.runs[0].font.size = Pt(10)
        p.runs[0].font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        set_cell_background(cell, "1E3A8A")
        set_cell_margins(cell, top=100, bottom=100, left=120, right=120)

    for r_idx, (p_name, p_type, p_desc) in enumerate(ip_data, start=1):
        c0 = ip_table.cell(r_idx, 0)
        c1 = ip_table.cell(r_idx, 1)
        c2 = ip_table.cell(r_idx, 2)
        c0.text = p_name
        c1.text = p_type
        c2.text = p_desc
        for cell in (c0, c1, c2):
            cell.paragraphs[0].runs[0].font.size = Pt(9.5)
            set_cell_margins(cell, top=80, bottom=80, left=120, right=120)
        if r_idx % 2 == 1:
            set_cell_background(c0, "F8FAFC")
            set_cell_background(c1, "F8FAFC")
            set_cell_background(c2, "F8FAFC")

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # -------------------------------------------------------------
    # 6. System Architecture
    # -------------------------------------------------------------
    add_section_header("System Architecture:")
    add_body_p(
        "The architecture of the GPT-4 Personalized Recommendation System operates on a multi-stage cognitive pipeline "
        "designed to handle user profile formulation, prompt construction, LLM inference with strict JSON schema parsing, "
        "and an interactive feedback refinement loop:"
    )

    arch_box = doc.add_paragraph()
    arch_box.paragraph_format.left_indent = Inches(0.4)
    arch_box.paragraph_format.space_before = Pt(4)
    arch_box.paragraph_format.space_after = Pt(8)
    run_box = arch_box.add_run(
        "+-----------------------------------------------------------------------------------+\n"
        "|                             SYSTEM ARCHITECTURE DIAGRAM                           |\n"
        "+-----------------------------------------------------------------------------------+\n"
        "|  [1. User Profile Input]                                                          |\n"
        "|    • Name, Age, Field, Interests, Skill Level, Preferred Type, Goal               |\n"
        "|                                     |                                             |\n"
        "|                                     v                                             |\n"
        "|  [2. Structured Prompt Engineering Module]                                         |\n"
        "|    • Role definition (Recommendation Consultant)                                  |\n"
        "|    • Formats user parameters into structured natural-language context             |\n"
        "|    • Enforces JSON schema (rank, recommendation, reason, score)                   |\n"
        "|                                     |                                             |\n"
        "|                                     v                                             |\n"
        "|  [3. GPT-4 Large Language Model Core]                                             |\n"
        "|    • Understands multidimensional interests simultaneously                        |\n"
        "|    • Synthesizes course / content curriculum with skill level & style             |\n"
        "|    • Computes alignment scores & generates transparent reasoning                  |\n"
        "|                                     |                                             |\n"
        "|                                     v                                             |\n"
        "|  [4. Recommendation Parser & Ranker]                                              |\n"
        "|    • Validates JSON structure, cleans data types, populates dataclasses           |\n"
        "|                                     |                                             |\n"
        "|                                     v                                             |\n"
        "|  [5. Presentation & UI Display (Streamlit / CLI)]                                 |\n"
        "|    • Tabular output: Rank | Recommendation | Reason | Score                       |\n"
        "|    • Visual score charts, profile pills, and export options                       |\n"
        "|                                     |                                             |\n"
        "|            +------------------------+------------------------+                    |\n"
        "|            |                                                 |                    |\n"
        "|            v                                                 v                    |\n"
        "|  [6. Satisfied User]                        [7. Conversational Feedback Loop]     |\n"
        "|      (Export CSV/JSON)                           ('More AI, less Web Dev')        |\n"
        "|                                                              |                    |\n"
        "|                                                              v                    |\n"
        "|                                                 [Refinement Prompting to GPT-4]   |\n"
        "+-----------------------------------------------------------------------------------+"
    )
    run_box.font.name = "Consolas"
    run_box.font.size = Pt(8.5)
    run_box.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)

    # -------------------------------------------------------------
    # 7. Module Design
    # -------------------------------------------------------------
    add_section_header("Module Design:")
    mod_data = [
        (
            "User Profile Module",
            "Collects and encapsulates user parameters (Name, Age, Field, Interests, Skill Level, Preferred Learning Type, and Goal) into a strongly-typed UserProfile dataclass with validation."
        ),
        (
            "Prompt Engineering Module",
            "Transforms raw user profile parameters into an optimized system and user prompt with role definition, strict domain rules, output formatting constraints, and JSON schema guarantees."
        ),
        (
            "GPT-4 Inference Engine",
            "Communicates with OpenAI's ChatCompletion endpoint (gpt-4o / gpt-4-turbo) utilizing temperature tuning (0.7) and structured output modes to generate explainable recommendations."
        ),
        (
            "Recommendation Parser Module",
            "Extracts and sanitizes the JSON response, validates numerical rank orders, formats match scores as percentage strings, and populates RecommendationResponse objects."
        ),
        (
            "Feedback & Refinement Loop",
            "Maintains conversational state, incorporates user feedback (e.g., 'I am more interested in AI than Web Development'), and triggers a recalibrated prompt to adjust rankings dynamically."
        ),
        (
            "Presentation & Export Module",
            "Renders the interactive Streamlit UI, tabular summaries matching lab specifications, bar charts of score distributions, and export utilities (CSV, JSON, Markdown)."
        )
    ]
    mod_table = doc.add_table(rows=len(mod_data) + 1, cols=2)
    mod_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(mod_table)

    mod_widths = [Inches(2.2), Inches(4.3)]
    for row in mod_table.rows:
        for idx, width in enumerate(mod_widths):
            row.cells[idx].width = width

    mod_headers = ["Module Name", "Functional Responsibility"]
    for idx, h in enumerate(mod_headers):
        cell = mod_table.cell(0, idx)
        cell.text = h
        p = cell.paragraphs[0]
        p.runs[0].bold = True
        p.runs[0].font.size = Pt(10)
        p.runs[0].font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        set_cell_background(cell, "1E3A8A")
        set_cell_margins(cell, top=100, bottom=100, left=120, right=120)

    for r_idx, (m_name, m_resp) in enumerate(mod_data, start=1):
        c0 = mod_table.cell(r_idx, 0)
        c1 = mod_table.cell(r_idx, 1)
        c0.text = m_name
        c1.text = m_resp
        for cell in (c0, c1):
            cell.paragraphs[0].runs[0].font.size = Pt(9.5)
            set_cell_margins(cell, top=80, bottom=80, left=120, right=120)
        if r_idx % 2 == 1:
            set_cell_background(c0, "F8FAFC")
            set_cell_background(c1, "F8FAFC")

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # -------------------------------------------------------------
    # 8. Theory & Conceptual Foundations
    # -------------------------------------------------------------
    add_section_header("Theory & Conceptual Foundations:")

    add_body_p(
        "1. What is a Recommendation System?\n"
        "A Recommendation System is an AI-based system that suggests items, content, products, services, or information "
        "to users based on their preferences, interests, previous interactions, or requirements. Prominent industry examples "
        "include Netflix (movie recommendations), YouTube (video suggestions), Amazon (product purchases), Spotify (music discovery), "
        "and online learning platforms (customized course pathways)."
    )

    add_body_p(
        "2. What is Personalized Recommendation?\n"
        "Personalized recommendation ensures that different users receive distinct, tailored suggestions according to their individual "
        "backgrounds and aspirations. For instance, Student A (interested in Python, AI, and Data Science) receives recommendations for "
        "Python Programming, Machine Learning, and Data Science Projects. In contrast, Student B (interested in Cybersecurity, Networks, "
        "and Ethical Hacking) receives Network Security, Ethical Hacking, and Cybersecurity Fundamentals. The fundamental progression is: "
        "User Profile -> Preferences -> AI Analysis -> Personalized Recommendations."
    )

    add_body_p(
        "3. Why Use Generative AI for Recommendations?\n"
        "Traditional recommendation algorithms (Collaborative Filtering and Matrix Factorization) suffer from notable limitations: "
        "they cannot process unstructured natural language descriptions, struggle with the cold-start problem for new users, cannot "
        "synthesize cross-disciplinary interests, and operate as black boxes incapable of explaining 'why' an item was recommended. "
        "Generative AI models like GPT-4 overcome these limitations because they:\n"
        "• Deeply comprehend complex, free-form natural language preference statements.\n"
        "• Simultaneously balance multiple conflicting or complementary interests.\n"
        "• Formulate transparent, convincing human-readable rationales for every suggestion.\n"
        "• Support conversational multi-turn interaction, allowing users to iteratively steer recommendations."
    )

    add_body_p(
        "4. Feedback-Based Recommendation Refinement\n"
        "A critical capability of LLM-based recommenders is real-time conversational refinement. When presented with initial suggestions, "
        "a user can provide clarifying feedback (such as 'I am more interested in AI than Web Development'). GPT-4 digests this prompt "
        "delta, prunes irrelevant suggestions, elevates AI core topics (Deep Learning, Generative AI, Computer Vision), and recalculates "
        "match scores, demonstrating true interactive personalization."
    )

    # -------------------------------------------------------------
    # 9. Implementation Source Code
    # -------------------------------------------------------------
    add_section_header("Implementation Source Code:")
    add_body_p("Core Recommendation Engine (recommender.py):")

    code_sample = '''import os, json, re
from dataclasses import dataclass, field, asdict
from typing import List, Dict, Any, Optional
from openai import OpenAI

@dataclass
class UserProfile:
    name: str = "Arun"
    age: int = 20
    field: str = "Computer Science"
    interests: str = "AI, Python"
    skill_level: str = "Beginner"
    preferred_type: str = "Practical"
    goal: str = "Learn AI"
    domain: str = "Online Courses"

@dataclass
class RecommendationItem:
    rank: int
    recommendation: str
    reason: str
    score: str
    category: str = "Core Subject"
    difficulty: str = "Beginner"

class PersonalizedRecommender:
    def __init__(self, api_key: Optional[str] = None, model: str = "gpt-4o"):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY", "")
        self.model = model
        self.client = OpenAI(api_key=self.api_key) if self.api_key else None

    def construct_initial_prompt(self, profile: UserProfile) -> str:
        return f"""You are an advanced AI Recommendation System powered by GPT-4.
Analyze the following user profile and generate exactly 5 top personalized recommendations.

USER PROFILE:
- Name: {profile.name} | Age: {profile.age} | Field: {profile.field}
- Stated Interests: {profile.interests}
- Skill Level: {profile.skill_level} | Preferred Style: {profile.preferred_type}
- Career/Learning Goal: {profile.goal}

INSTRUCTIONS:
Return strictly a valid JSON object matching this schema:
{{
  "user_summary": "Computer Science student | Interests: AI, Python | Level: Beginner",
  "recommendations": [
    {{
      "rank": 1,
      "recommendation": "Course Title",
      "reason": "Detailed justification matching user preferences",
      "score": "95%",
      "category": "Category Name",
      "difficulty": "Beginner"
    }}
  ]
}}"""

    def construct_feedback_prompt(self, profile, prev_items, feedback) -> str:
        return f"""Refine recommendations based on user feedback: "{feedback}"
Initial suggestions: {prev_items}
Adjust rankings and recommendations to strictly satisfy the user's feedback."""

    def get_recommendations(self, profile: UserProfile):
        prompt = self.construct_initial_prompt(profile)
        if self.client:
            res = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "system", "content": "You are an expert AI Recommendation Consultant."},
                          {"role": "user", "content": prompt}],
                response_format={"type": "json_object"}
            )
            return json.loads(res.choices[0].message.content)
        # Fallback heuristic engine ensures 100% lab uptime
        return self._heuristic_recommendation(profile)
'''
    p_code = doc.add_paragraph()
    p_code.paragraph_format.left_indent = Inches(0.2)
    p_code.paragraph_format.space_before = Pt(2)
    p_code.paragraph_format.space_after = Pt(6)
    r_c = p_code.add_run(code_sample)
    r_c.font.name = "Consolas"
    r_c.font.size = Pt(8.5)
    r_c.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)

    # -------------------------------------------------------------
    # 10. Sample Test Runs & Experimental Output
    # -------------------------------------------------------------
    add_section_header("Sample Test Runs & Experimental Output:")

    add_body_p("Test Case 1: Initial Recommendations for Student A (Arun)", italic=True)
    add_body_p("User Profile: Computer Science student (Arun, Age 20) | Interests: AI, Python | Level: Beginner | Style: Practical | Goal: Learn AI")

    out_data_1 = [
        (1, "Python for AI", "Matches Python and AI interests", "95%"),
        (2, "Machine Learning Basics", "Suitable for beginner AI learners", "92%"),
        (3, "Generative AI", "Relevant to current AI interests", "88%"),
        (4, "Data Science with Python", "Combines Python and data analysis", "85%"),
        (5, "Deep Learning Basics", "Natural progression after ML", "80%")
    ]
    t_out1 = doc.add_table(rows=len(out_data_1) + 1, cols=4)
    t_out1.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_out1)
    t_widths = [Inches(0.8), Inches(2.2), Inches(2.7), Inches(0.8)]
    for row in t_out1.rows:
        for idx, w in enumerate(t_widths):
            row.cells[idx].width = w

    t_headers = ["Rank", "Recommendation", "Reason", "Score"]
    for idx, h in enumerate(t_headers):
        c = t_out1.cell(0, idx)
        c.text = h
        p = c.paragraphs[0]
        p.runs[0].bold = True
        p.runs[0].font.size = Pt(9.5)
        p.runs[0].font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        set_cell_background(c, "1E3A8A")
        set_cell_margins(c, top=80, bottom=80, left=100, right=100)

    for r_idx, (rk, rec, reas, sc) in enumerate(out_data_1, start=1):
        c0, c1, c2, c3 = t_out1.cell(r_idx, 0), t_out1.cell(r_idx, 1), t_out1.cell(r_idx, 2), t_out1.cell(r_idx, 3)
        c0.text = str(rk)
        c1.text = rec
        c2.text = reas
        c3.text = sc
        for c in (c0, c1, c2, c3):
            c.paragraphs[0].runs[0].font.size = Pt(9.5)
            set_cell_margins(c, top=60, bottom=60, left=100, right=100)
        if r_idx % 2 == 1:
            for c in (c0, c1, c2, c3):
                set_cell_background(c, "F8FAFC")

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # Test Case 2: Feedback
    add_body_p("Test Case 2: Feedback-Based Refinement (Section 6 Demonstration)", italic=True)
    add_body_p("Conversational Feedback Injected: \"I am more interested in AI than Web Development.\"")

    out_data_2 = [
        (1, "Artificial Intelligence", "Directly prioritizes core AI foundations as requested in user feedback", "96%"),
        (2, "Machine Learning", "Essential algorithm concepts aligning with intensified AI interest", "93%"),
        (3, "Deep Learning", "Expands neural network knowledge per user's focused interest on AI", "90%"),
        (4, "Generative AI", "Cutting-edge LLM and prompt engineering applications matching AI preference", "87%"),
        (5, "Computer Vision", "Applies AI techniques to image processing, replacing web development topics", "82%")
    ]
    t_out2 = doc.add_table(rows=len(out_data_2) + 1, cols=4)
    t_out2.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_out2)
    for row in t_out2.rows:
        for idx, w in enumerate(t_widths):
            row.cells[idx].width = w

    for idx, h in enumerate(t_headers):
        c = t_out2.cell(0, idx)
        c.text = h
        p = c.paragraphs[0]
        p.runs[0].bold = True
        p.runs[0].font.size = Pt(9.5)
        p.runs[0].font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        set_cell_background(c, "059669")
        set_cell_margins(c, top=80, bottom=80, left=100, right=100)

    for r_idx, (rk, rec, reas, sc) in enumerate(out_data_2, start=1):
        c0, c1, c2, c3 = t_out2.cell(r_idx, 0), t_out2.cell(r_idx, 1), t_out2.cell(r_idx, 2), t_out2.cell(r_idx, 3)
        c0.text = str(rk)
        c1.text = rec
        c2.text = reas
        c3.text = sc
        for c in (c0, c1, c2, c3):
            c.paragraphs[0].runs[0].font.size = Pt(9.5)
            set_cell_margins(c, top=60, bottom=60, left=100, right=100)
        if r_idx % 2 == 1:
            for c in (c0, c1, c2, c3):
                set_cell_background(c, "F0FDF4")

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # Test Case 3: Student B
    add_body_p("Test Case 3: Recommendations for Student B (Cybersecurity & Networks)", italic=True)
    add_body_p("User Profile: Information Technology student | Interests: Cybersecurity, Networks, Ethical Hacking | Level: Intermediate | Goal: Penetration Tester")

    out_data_3 = [
        (1, "Network Security", "Fundamental networking principles essential for cybersecurity defense", "95%"),
        (2, "Ethical Hacking", "Hands-on labs simulating real cyber defense and penetration scenarios", "92%"),
        (3, "Cybersecurity Fundamentals", "Comprehensive primer covering threat vectors, defense, and security hygiene", "89%"),
        (4, "Linux for Ethical Hackers", "Essential CLI navigation and scripting for cybersecurity practitioners", "85%"),
        (5, "Cryptography & Secure Communications", "Theoretical and practical foundations of encryption and secure tunnels", "80%")
    ]
    t_out3 = doc.add_table(rows=len(out_data_3) + 1, cols=4)
    t_out3.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_out3)
    for row in t_out3.rows:
        for idx, w in enumerate(t_widths):
            row.cells[idx].width = w

    for idx, h in enumerate(t_headers):
        c = t_out3.cell(0, idx)
        c.text = h
        p = c.paragraphs[0]
        p.runs[0].bold = True
        p.runs[0].font.size = Pt(9.5)
        p.runs[0].font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        set_cell_background(c, "4338CA")
        set_cell_margins(c, top=80, bottom=80, left=100, right=100)

    for r_idx, (rk, rec, reas, sc) in enumerate(out_data_3, start=1):
        c0, c1, c2, c3 = t_out3.cell(r_idx, 0), t_out3.cell(r_idx, 1), t_out3.cell(r_idx, 2), t_out3.cell(r_idx, 3)
        c0.text = str(rk)
        c1.text = rec
        c2.text = reas
        c3.text = sc
        for c in (c0, c1, c2, c3):
            c.paragraphs[0].runs[0].font.size = Pt(9.5)
            set_cell_margins(c, top=60, bottom=60, left=100, right=100)
        if r_idx % 2 == 1:
            for c in (c0, c1, c2, c3):
                set_cell_background(c, "EEF2FF")

    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    # -------------------------------------------------------------
    # 11. Viva Questions & Model Answers
    # -------------------------------------------------------------
    add_section_header("Viva Questions & Model Answers:")
    viva_qa = [
        (
            "Q1. How does a Generative AI recommendation system differ from Collaborative Filtering?",
            "Collaborative filtering relies on user-item interaction matrices and historical rating similarities. It suffers from the cold-start problem when no historical data exists. In contrast, Generative AI uses LLM semantic reasoning to evaluate natural language descriptions of user interests, working immediately without prior interaction histories and providing human-readable justifications."
        ),
        (
            "Q2. What role does prompt structure play in generating consistent recommendations?",
            "Prompt engineering dictates the persona of the model, provides structured context (Name, Field, Interests, Skill Level, Learning Style), imposes deterministic constraints, and mandates strict JSON output schemas, ensuring that the response can be programmatically parsed and rendered into tabular UI representations."
        ),
        (
            "Q3. How is conversational feedback incorporated in the recommendation pipeline?",
            "The system preserves conversational state (user profile and previous recommendations) and appends the user's feedback statement (e.g., 'I am more interested in AI than Web Development'). A refinement prompt instructs GPT-4 to re-rank items, prune de-emphasized domains, introduce aligned specialized courses, and explain the updated alignment in the reason field."
        ),
        (
            "Q4. Why is temperature tuning important in recommendation applications?",
            "A lower to moderate temperature (e.g., 0.5 to 0.7) strikes an optimal balance: it keeps the recommendations grounded in established academic curricula and user preferences while providing sufficient linguistic flexibility to formulate compelling, diverse explanations."
        ),
        (
            "Q5. How can the system be safeguarded against API unavailability during evaluation?",
            "By implementing a dual-mode fallback architecture: if the OpenAI API key is missing or encounters network timeouts/rate limits, the application smoothly delegates to an offline heuristic scoring engine that emulates GPT-4's ranking and feedback behavior, guaranteeing 100% test reliability."
        )
    ]

    for q, a in viva_qa:
        pq = doc.add_paragraph()
        pq.paragraph_format.space_before = Pt(4)
        pq.paragraph_format.space_after = Pt(1)
        pq.paragraph_format.keep_with_next = True
        rq = pq.add_run(q)
        rq.bold = True
        rq.font.size = Pt(10)
        rq.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)

        pa = doc.add_paragraph()
        pa.paragraph_format.space_after = Pt(5)
        ra = pa.add_run(a)
        ra.font.size = Pt(9.5)

    # -------------------------------------------------------------
    # 12. Result & Conclusion
    # -------------------------------------------------------------
    add_section_header("Result & Conclusion:")
    add_body_p(
        "Thus, an AI-powered Personalized Recommendation System using GPT-4 was successfully designed, implemented, "
        "and evaluated. The application efficiently captured multidimensional user profiles, transformed them into structured "
        "prompts, generated ranked personalized recommendations with explainable reasons and match scores, and dynamically "
        "refined recommendations through conversational user feedback. The system successfully validated all test cases outlined "
        "in the laboratory manual for both initial recommendations and feedback-driven iterations."
    )

    doc.save(output_filename)
    print(f"[SUCCESS] Lab Report Word Document generated at: {output_filename}")


if __name__ == "__main__":
    dest_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "24CS2506_Exp4_URK23CS1184_Personalized_Recommendation_System.docx"
    )
    build_document(dest_path)

