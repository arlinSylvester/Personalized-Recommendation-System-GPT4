"""
app.py - Personalized Recommendation System Web Application
Course: 24CS2506 – Building Applications using GPT-4
Experiment 4: Personalized Recommendation System
Student: Carlin Sylvester | Reg. No: URK23CS1184
"""

import os
import json
import pandas as pd
import streamlit as st

from recommender import (
    UserProfile,
    RecommendationItem,
    PersonalizedRecommendationPipeline,
    SaveModule
)

# -----------------------------------------------------------------------------
# Streamlit Page Configuration
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Personalized Recommender | 24CS2506 Exp 4",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------------------------------
# Custom Styling
# -----------------------------------------------------------------------------
st.markdown("""
<style>
    .badge-course {
        display: inline-block;
        background: linear-gradient(135deg, #1E3A8A, #2563EB);
        color: #FFFFFF !important;
        padding: 5px 14px;
        border-radius: 9999px;
        font-weight: 600;
        font-size: 0.85rem;
        letter-spacing: 0.5px;
        margin-bottom: 8px;
    }
    .main-title {
        font-size: 2.2rem;
        font-weight: 800;
        color: #0F172A;
        margin-bottom: 0.2rem;
        letter-spacing: -0.5px;
    }
    .section-banner {
        background-color: #F1F5F9;
        border-left: 5px solid #2563EB;
        padding: 8px 14px;
        border-radius: 0 6px 6px 0;
        margin-top: 18px;
        margin-bottom: 12px;
        font-weight: 700;
        font-size: 1.15rem;
        color: #1E293B;
    }
    .card-box {
        background: #F8FAFC;
        border: 1px solid #E2E8F0;
        border-radius: 8px;
        padding: 14px 18px;
        margin-bottom: 14px;
    }
    .score-badge {
        background-color: #DCFCE7;
        color: #166534;
        font-weight: 700;
        padding: 4px 10px;
        border-radius: 6px;
        font-size: 0.95rem;
    }
    .intent-box {
        background-color: #FEF3C7;
        border-left: 4px solid #F59E0B;
        padding: 12px 16px;
        border-radius: 0 6px 6px 0;
        margin-bottom: 14px;
    }
    .saved-box {
        background-color: #ECFDF5;
        border: 1px solid #10B981;
        color: #065F46;
        padding: 14px;
        border-radius: 8px;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# Session State Initialization
# -----------------------------------------------------------------------------
if "pipeline_result" not in st.session_state:
    st.session_state.pipeline_result = None
if "refine_result" not in st.session_state:
    st.session_state.refine_result = None
if "saved_status" not in st.session_state:
    st.session_state.saved_status = None


# -----------------------------------------------------------------------------
# Sidebar: Settings & Test Presets
# -----------------------------------------------------------------------------
with st.sidebar:
    st.markdown("### ⚙️ Engine Settings")
    api_key_input = st.text_input(
        "OpenAI API Key (Optional)",
        type="password",
        value=os.getenv("OPENAI_API_KEY", ""),
        help="Leave blank to run the built-in laboratory simulator for 100% offline verification."
    )
    model_choice = st.selectbox(
        "Model Selector",
        ["gpt-4o", "gpt-4-turbo", "gpt-3.5-turbo"],
        index=0
    )

    st.markdown("---")
    st.markdown("### 👤 Select Laboratory Profile")
    profile_preset = st.selectbox(
        "Load Preset Profile",
        [
            "Student A (Arun - AI & Python Beginner)",
            "Student B (Cybersecurity & Networks)",
            "Custom Profile"
        ],
        index=0
    )

    st.markdown("---")
    st.markdown("### 📋 Academic Information")
    st.markdown("""
    **Course:** 24CS2506  
    **Title:** Building Applications using GPT-4  
    **Experiment:** 4 – Personalized Recommendation System  
    **Student:** Carlin Sylvester  
    **Register No:** URK23CS1184  
    **Date:** 05-11-2026  
    """)

    pipeline = PersonalizedRecommendationPipeline(api_key=api_key_input, model=model_choice)


# -----------------------------------------------------------------------------
# SCREEN 1: HOME SCREEN (Title & Overview)
# -----------------------------------------------------------------------------
st.markdown('<span class="badge-course">24CS2506 • EXPERIMENT 4</span>', unsafe_allow_html=True)
st.markdown('<div class="main-title">Personalized Recommendation System using GPT-4</div>', unsafe_allow_html=True)
st.caption("11-Module Architecture implementing User Profiling, Preference Analysis, GPT-4 Prompting, Ranking, Explanation, Intent Detection, Feedback Refinement, and Saving.")

# Tab setup
tab_main, tab_feedback, tab_docs = st.tabs([
    "🎯 Core Pipeline (Screenshots 1-8)",
    "🔄 Feedback, Intent & Refinement (Screenshots 9-11)",
    "💾 Export & Lab Report (Screenshot 12)"
])

# Determine default input values based on preset
if profile_preset == "Student B (Cybersecurity & Networks)":
    d_name = "Student B"
    d_age = 21
    d_background = "Information Technology"
    d_interests = "Cybersecurity, Networks, Ethical Hacking"
    d_skill = "Intermediate"
    d_cat = "Online Courses"
    d_goal = "Penetration Tester"
    d_pref = "Practical"
    d_items = 5
elif profile_preset == "Custom Profile":
    d_name = "Kavitha"
    d_age = 22
    d_background = "Data Science"
    d_interests = "Data Analytics, Machine Learning, Cloud"
    d_skill = "Intermediate"
    d_cat = "Hands-on Projects"
    d_goal = "Build Production ML Pipelines"
    d_pref = "Project-based"
    d_items = 5
else:
    # Student A (Arun) - Default
    d_name = "Arun"
    d_age = 20
    d_background = "Computer Science"
    d_interests = "AI, Python"
    d_skill = "Beginner"
    d_cat = "Online Courses"
    d_goal = "Learn AI"
    d_pref = "Practical"
    d_items = 5


# =============================================================================
# TAB 1: CORE PIPELINE
# =============================================================================
with tab_main:
    # -------------------------------------------------------------------------
    # SCREEN 2: USER PROFILE INPUT
    # -------------------------------------------------------------------------
    st.markdown('<div class="section-banner">∙ User Profile Input (9 Laboratory Parameters)</div>', unsafe_allow_html=True)
    
    with st.form("input_form"):
        col1, col2, col3 = st.columns(3)
        with col1:
            name_val = st.text_input("Name", value=d_name)
            age_val = st.number_input("Age", min_value=15, max_value=80, value=d_age)
            background_val = st.text_input("Background (Degree / Major)", value=d_background)
        with col2:
            interests_val = st.text_input("Interests", value=d_interests)
            skill_val = st.selectbox(
                "Skill Level",
                ["Beginner", "Intermediate", "Advanced"],
                index=0 if d_skill == "Beginner" else (1 if d_skill == "Intermediate" else 2)
            )
            cat_val = st.selectbox(
                "Preferred Category",
                ["Online Courses", "Books & Research Papers", "Hands-on Projects"],
                index=0 if d_cat == "Online Courses" else (1 if d_cat == "Books & Research Papers" else 2)
            )
        with col3:
            goal_val = st.text_input("Goal", value=d_goal)
            pref_val = st.selectbox(
                "Preferences (Learning Style)",
                ["Practical", "Theoretical", "Project-based", "Fast-paced"],
                index=0 if d_pref == "Practical" else (1 if d_pref == "Theoretical" else 2)
            )
            items_val = st.number_input("Number of Items", min_value=3, max_value=10, value=d_items)

        submit_btn = st.form_submit_button("🚀 Run Personalized Recommendation Pipeline", use_container_width=True)

    if submit_btn or st.session_state.pipeline_result is None:
        user_prof = UserProfile(
            name=name_val,
            age=age_val,
            background=background_val,
            interests=interests_val,
            skill_level=skill_val,
            preferred_category=cat_val,
            goal=goal_val,
            preferences=pref_val,
            number_of_items=items_val
        )
        with st.spinner("Executing pipeline through 11 modules..."):
            st.session_state.pipeline_result = pipeline.run_pipeline(user_prof)
            st.session_state.refine_result = None

    # Render Results if available
    if st.session_state.pipeline_result:
        res = st.session_state.pipeline_result
        prof = res["profile"]
        pref = res["preference_analysis"]
        rec = res["recommendation_output"]

        # ---------------------------------------------------------------------
        # SCREEN 3: COLLECTED USER PROFILE
        # ---------------------------------------------------------------------
        st.markdown('<div class="section-banner">∙ Collected User Profile</div>', unsafe_allow_html=True)
        st.markdown(f"""
        <div class="card-box">
            <h4 style="margin-top:0; color:#1E3A8A;">👤 User Profile Summary</h4>
            <div style="display:grid; grid-template-columns: repeat(3, 1fr); gap: 10px;">
                <div><strong>Name:</strong> {prof.name}</div>
                <div><strong>Age:</strong> {prof.age}</div>
                <div><strong>Background:</strong> {prof.background}</div>
                <div><strong>Interests:</strong> {prof.interests}</div>
                <div><strong>Skill Level:</strong> {prof.skill_level}</div>
                <div><strong>Category:</strong> {prof.preferred_category}</div>
                <div><strong>Goal:</strong> {prof.goal}</div>
                <div><strong>Preferences:</strong> {prof.preferences}</div>
                <div><strong>Requested Items:</strong> {prof.number_of_items}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # ---------------------------------------------------------------------
        # SCREEN 4: PREFERENCE ANALYSIS
        # ---------------------------------------------------------------------
        st.markdown('<div class="section-banner">∙ Preference Analysis</div>', unsafe_allow_html=True)
        col_pref1, col_pref2 = st.columns([3, 2])
        with col_pref1:
            st.write(f"**Synthesized Alignment:** {pref.get('alignment_summary')}")
            st.write(f"**Pedagogical Directive:** {pref.get('pedagogical_focus')}")
            st.write(f"**Identified Primary Domains:** {', '.join(pref.get('primary_domains', []))}")
        with col_pref2:
            st.caption("Domain Affinity Weighting")
            affinity_df = pd.DataFrame(
                list(pref.get("domain_affinity_scores", {}).items()),
                columns=["Domain", "Affinity Weight"]
            ).set_index("Domain")
            st.bar_chart(affinity_df)

        # ---------------------------------------------------------------------
        # SCREEN 5: PROMPT GENERATION
        # ---------------------------------------------------------------------
        st.markdown('<div class="section-banner">∙ Prompt Generation</div>', unsafe_allow_html=True)
        with st.expander("🔍 View Structured Prompt Generated for GPT-4", expanded=False):
            st.code(rec["prompt_used"], language="markdown")

        # ---------------------------------------------------------------------
        # SCREEN 6: GPT-4 RECOMMENDATION
        # ---------------------------------------------------------------------
        st.markdown('<div class="section-banner">∙ GPT-4 Recommendation</div>', unsafe_allow_html=True)
        st.info(f"**Engine Invoked:** {rec['engine']} | **Status:** Success")

        # ---------------------------------------------------------------------
        # SCREEN 7: RECOMMENDATION RANKING
        # ---------------------------------------------------------------------
        st.markdown('<div class="section-banner">∙ Recommendation Ranking</div>', unsafe_allow_html=True)
        table_rows = [
            {
                "Rank": item.rank,
                "Recommendation": item.recommendation,
                "Reason": item.reason,
                "Score": item.score
            }
            for item in rec["items"]
        ]
        df_rank = pd.DataFrame(table_rows)
        st.table(df_rank)

        # ---------------------------------------------------------------------
        # SCREEN 8: RECOMMENDATION EXPLANATION
        # ---------------------------------------------------------------------
        st.markdown('<div class="section-banner">∙ Recommendation Explanation</div>', unsafe_allow_html=True)
        for item in rec["items"]:
            st.markdown(f"""
            <div style="border-left: 4px solid #2563EB; background:#FFFFFF; padding:12px 16px; margin-bottom:10px; border-radius:0 6px 6px 0; box-shadow: 0 1px 3px rgba(0,0,0,0.05);">
                <div style="display:flex; justify-content:space-between;">
                    <span style="font-size:1.05rem; font-weight:700; color:#1E3A8A;">Rank #{item.rank}: {item.recommendation}</span>
                    <span class="score-badge">Match: {item.score}</span>
                </div>
                <p style="margin:6px 0 2px 0; color:#334155;"><strong>Explanation Rationale:</strong> {item.reason}</p>
                <small style="color:#64748B;">Category: {item.category} | Level: {item.difficulty}</small>
            </div>
            """, unsafe_allow_html=True)


# =============================================================================
# TAB 2: FEEDBACK, INTENT & REFINEMENT
# =============================================================================
with tab_feedback:
    if st.session_state.pipeline_result is None:
        st.warning("Please execute the Core Pipeline in Tab 1 first.")
    else:
        # ---------------------------------------------------------------------
        # SCREEN 9: USER FEEDBACK
        # -------------------------------------------------------------------------
        st.markdown('<div class="section-banner">∙ User Feedback (Section 6 Demonstration)</div>', unsafe_allow_html=True)
        st.markdown("Users provide natural-language feedback to steer recommendations interactively.")

        fb_preset = st.radio(
            "Select Feedback Example:",
            [
                "\"I am more interested in AI than Web Development.\"",
                "\"I want to focus heavily on PyTorch and Deep Learning.\"",
                "\"I prefer practical penetration testing and network security.\"",
                "Custom Feedback"
            ],
            index=0
        )
        if fb_preset == "Custom Feedback":
            user_feedback_val = st.text_input("Enter Feedback Statement:", value="I prefer more practical AI courses.")
        else:
            user_feedback_val = fb_preset.strip('"')

        refine_click = st.button("🔄 Submit User Feedback & Trigger Refinement", type="primary", use_container_width=True)

        if refine_click or st.session_state.refine_result is None:
            active_prof = st.session_state.pipeline_result["profile"]
            active_items = st.session_state.pipeline_result["recommendation_output"]["items"]
            with st.spinner("Analyzing feedback and detecting intent..."):
                st.session_state.refine_result = pipeline.refine_pipeline(
                    active_prof,
                    active_items,
                    user_feedback_val
                )

        if st.session_state.refine_result:
            ref_data = st.session_state.refine_result
            det_intent = ref_data["detected_intent"]
            ref_out = ref_data["refined_output"]

            # -----------------------------------------------------------------
            # SCREEN 11: INTENT DETECTION
            # -----------------------------------------------------------------
            st.markdown('<div class="section-banner">∙ Intent Detection</div>', unsafe_allow_html=True)
            st.markdown(f"""
            <div class="intent-box">
                <h4 style="margin-top:0; color:#92400E;">🎯 Natural Language Intent Detected</h4>
                <div><strong>Raw Feedback:</strong> "{det_intent['raw_feedback']}"</div>
                <div><strong>Primary Action:</strong> {det_intent['primary_action']}</div>
                <div><strong>Target Focus:</strong> {det_intent['focus_target']}</div>
                <div><strong>Deprecated Target:</strong> {det_intent['deprecated_target']}</div>
                <div><strong>Confidence:</strong> {det_intent['intent_confidence']} | <strong>Sentiment:</strong> {det_intent['sentiment']}</div>
            </div>
            """, unsafe_allow_html=True)

            # -----------------------------------------------------------------
            # SCREEN 10: REFINED RECOMMENDATIONS
            # -----------------------------------------------------------------
            st.markdown('<div class="section-banner">∙ Refined Recommendations</div>', unsafe_allow_html=True)
            ref_rows = [
                {
                    "Rank": item.rank,
                    "Recommendation": item.recommendation,
                    "Reason": item.reason,
                    "Score": item.score
                }
                for item in ref_out["items"]
            ]
            st.table(pd.DataFrame(ref_rows))

            col_before, col_after = st.columns(2)
            with col_before:
                st.caption("Initial Recommendations")
                for it in st.session_state.pipeline_result["recommendation_output"]["items"]:
                    st.write(f"• #{it.rank} **{it.recommendation}** ({it.score})")
            with col_after:
                st.caption("Updated Recommendations (After Feedback)")
                for it in ref_out["items"]:
                    st.write(f"• #{it.rank} **{it.recommendation}** ({it.score})")


# =============================================================================
# TAB 3: EXPORT & LAB REPORT
# =============================================================================
with tab_docs:
    st.markdown('<div class="section-banner">∙ Recommendation Saved Successfully (Save Module)</div>', unsafe_allow_html=True)
    st.markdown("Exports the finalized recommendation session into structured files for academic submission.")

    if st.session_state.pipeline_result:
        active_prof = st.session_state.pipeline_result["profile"]
        current_items = (
            st.session_state.refine_result["refined_output"]["items"]
            if st.session_state.refine_result
            else st.session_state.pipeline_result["recommendation_output"]["items"]
        )
        current_feedback = st.session_state.refine_result["feedback"] if st.session_state.refine_result else None
        current_intent = st.session_state.refine_result["detected_intent"] if st.session_state.refine_result else None

        save_btn = st.button("💾 Save Recommendation Session Now", type="primary")
        if save_btn:
            save_path = os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                "saved_recommendations.json"
            )
            SaveModule.save_report(
                active_prof,
                current_items,
                feedback=current_feedback,
                intent=current_intent,
                filepath=save_path
            )
            st.session_state.saved_status = save_path

        if st.session_state.saved_status:
            st.markdown(f"""
            <div class="saved-box">
                ✅ <strong>Recommendation Saved Successfully!</strong><br>
                File path: <code>{st.session_state.saved_status}</code><br>
                Payload status: Validated JSON with user profile, rankings, rationales, and intent history.
            </div>
            """, unsafe_allow_html=True)

        st.markdown("---")
        st.subheader("Download Options for Student Submission")
        c1, c2 = st.columns(2)
        with c1:
            csv_data = pd.DataFrame([
                {"Rank": i.rank, "Recommendation": i.recommendation, "Reason": i.reason, "Score": i.score}
                for i in current_items
            ]).to_csv(index=False)
            st.download_button("📥 Download Recommendations (CSV)", data=csv_data, file_name="recommendations_exp4.csv", mime="text/csv")
        with c2:
            json_payload = json.dumps([i.to_dict() for i in current_items], indent=2)
            st.download_button("📥 Download JSON Payload", data=json_payload, file_name="recommendations_exp4.json", mime="application/json")
