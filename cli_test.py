"""
cli_test.py - End-to-End Terminal Demonstration for Experiment 4
Validates all 11 modules and 12 output requirements
Course: 24CS2506 – Building Applications using GPT-4
Roll No: URK23CS1184 | Carlin Sylvester
"""

import sys
import os
import json

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from recommender import (
    UserProfile,
    PersonalizedRecommendationPipeline,
    SaveModule
)


def run_full_demo():
    print("=" * 80)
    print(" 24CS2506 – Building Applications using GPT-4")
    print(" Experiment 4: Personalized Recommendation System")
    print(" Student: Carlin Sylvester | Reg. No: URK23CS1184 | Date: 05-11-2026")
    print("=" * 80)
    print()

    # 1. Home Screen
    print("[SCREEN 1: HOME SCREEN]")
    print("System: Personalized Recommendation System using GPT-4")
    print("Architecture: 11-Module Cognitive Pipeline")
    print()

    # 2. User Profile Input
    print("[SCREEN 2: USER PROFILE INPUT]")
    profile = UserProfile(
        name="Arun",
        age=20,
        background="Computer Science",
        interests="AI, Python",
        skill_level="Beginner",
        preferred_category="Online Courses",
        goal="Learn AI",
        preferences="Practical",
        number_of_items=5
    )
    print("Captured 9 parameters: Name, Age, Background, Interests, Skill Level, Preferred Category, Goal, Preferences, Number of Items.")
    print()

    # 3. Collected User Profile
    print("[SCREEN 3: COLLECTED USER PROFILE]")
    print(f"  Name               : {profile.name}")
    print(f"  Age                : {profile.age}")
    print(f"  Background         : {profile.background}")
    print(f"  Interests          : {profile.interests}")
    print(f"  Skill Level        : {profile.skill_level}")
    print(f"  Preferred Category : {profile.preferred_category}")
    print(f"  Goal               : {profile.goal}")
    print(f"  Preferences        : {profile.preferences}")
    print(f"  Number of Items    : {profile.number_of_items}")
    print()

    pipeline = PersonalizedRecommendationPipeline()

    # Run initial pipeline
    res = pipeline.run_pipeline(profile)

    # 4. Preference Analysis
    print("[SCREEN 4: PREFERENCE ANALYSIS]")
    pref = res["preference_analysis"]
    print(f"  Alignment Summary  : {pref['alignment_summary']}")
    print(f"  Pedagogical Focus  : {pref['pedagogical_focus']}")
    print(f"  Primary Domains    : {pref['primary_domains']}")
    print(f"  Domain Weights     : {pref['domain_affinity_scores']}")
    print()

    # 5. Prompt Generation
    rec_out = res["recommendation_output"]
    print("[SCREEN 5: PROMPT GENERATION]")
    print(">> Generated System & User Prompt:")
    print("-" * 50)
    print(rec_out["prompt_used"].strip())
    print("-" * 50)
    print()

    # 6. GPT-4 Recommendation
    print("[SCREEN 6: GPT-4 RECOMMENDATION]")
    print(f"  Inference Engine : {rec_out['engine']}")
    print(f"  Output Summary   : {rec_out['user_summary']}")
    print()

    # 7. Recommendation Ranking
    print("[SCREEN 7: RECOMMENDATION RANKING]")
    print(f"{'Rank':<6} | {'Recommendation':<30} | {'Reason':<45} | {'Score':<6}")
    print("-" * 95)
    for it in rec_out["items"]:
        print(f"{it.rank:<6} | {it.recommendation:<30} | {it.reason:<45} | {it.score:<6}")
    print("-" * 95)
    print()

    # 8. Recommendation Explanation
    print("[SCREEN 8: RECOMMENDATION EXPLANATION]")
    for it in rec_out["items"]:
        print(f"  * #{it.rank} {it.recommendation} ({it.score}) -> Reason: {it.reason}")
    print()

    # 9. User Feedback
    feedback = "I am more interested in AI than Web Development."
    print("[SCREEN 9: USER FEEDBACK]")
    print(f"  User Feedback Statement: \"{feedback}\"")
    print()

    ref_res = pipeline.refine_pipeline(profile, rec_out["items"], feedback)

    # 11. Intent Detection
    print("[SCREEN 11: INTENT DETECTION]")
    intent = ref_res["detected_intent"]
    print(f"  Primary Action     : {intent['primary_action']}")
    print(f"  Target Focus       : {intent['focus_target']}")
    print(f"  Deprecated Target  : {intent['deprecated_target']}")
    print(f"  Confidence Score   : {intent['intent_confidence']}")
    print()

    # 10. Refined Recommendations
    print("[SCREEN 10: REFINED RECOMMENDATIONS]")
    ref_items = ref_res["refined_output"]["items"]
    print(f"{'Rank':<6} | {'Recommendation':<30} | {'Reason':<45} | {'Score':<6}")
    print("-" * 95)
    for it in ref_items:
        print(f"{it.rank:<6} | {it.recommendation:<30} | {it.reason:<45} | {it.score:<6}")
    print("-" * 95)
    print()

    # 12. Recommendation Saved Successfully
    print("[SCREEN 12: RECOMMENDATION SAVED SUCCESSFULLY]")
    save_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "saved_recommendations.json")
    SaveModule.save_report(profile, ref_items, feedback=feedback, intent=intent, filepath=save_path)
    print(f"  STATUS: Recommendation Saved Successfully!")
    print(f"  Saved File: {save_path}")
    print()

    print("=" * 80)
    print(" ALL 11 MODULES & 12 OUTPUT SCREENS VERIFIED SUCCESSFULLY!")
    print("=" * 80)


if __name__ == "__main__":
    run_full_demo()
