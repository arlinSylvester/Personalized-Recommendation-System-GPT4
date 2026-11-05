| Ex. No.:4 | PERSONALIZED RECOMMENDATION SYSTEM | URK23CS1184 |
| :--- | :--- | :--- |
| **05-11-2026** | | |

### Aim: 
To develop a personalized recommendation system using GPT-4 that analyzes user preferences and generates, ranks and explains suitable recommendations based on the user's profile, interests, skill level and goals.

---

### Problem Statement:  
Design and develop an intelligent personalized recommendation system using GPT-4. The application should collect user information and preferences, analyze the user's requirements, generate personalized recommendations, rank them according to suitability, provide explanations for the recommendations and refine the results based on user feedback.

---

### Software Requirements: 

| Software | Version |
| :--- | :--- |
| Python | 3.12.10 |
| Ollama | 0.6.2 |
| VS Code | 1.95.0 |
| Pandas | 2.2.2 |
| Sentence Transformers | 6.0.0 |

---

### Input Parameters 

| Parameters | Description |
| :--- | :--- |
| **Name** | Full name of the user for conversational personalization and user identification. |
| **Age** | Age of the user in years to adjust content complexity and pedagogical tone appropriately. |
| **Background** | Academic degree, current profession, or educational major (e.g., Computer Science). |
| **Interests** | Core topics, technical subjects, or domain areas of interest (e.g., AI, Python, Data Science). |
| **Skill Level** | Prior technical proficiency level: Beginner, Intermediate, or Advanced. |
| **Preferred Category** | Desired domain of suggestions (e.g., Online Courses, Books, Hands-on Projects). |
| **Goal** | Primary career or learning milestone the user aims to accomplish (e.g., Learn AI). |
| **Preferences** | Pedagogical style preference: Practical, Theoretical, Project-based, or Fast-paced. |
| **Number of items** | Desired number of ranked recommendations to generate (default: 5). |

---

### System Architecture 

```
+-----------------------------------------------------------------------------------+
|                    SYSTEM ARCHITECTURE - 11 MODULE PIPELINE                       |
+-----------------------------------------------------------------------------------+
|  [1. Input Module]                                                                |
|      Collects: Name, Age, Background, Interests, Skill Level,                     |
|                Preferred Category, Goal, Preferences, Number of Items             |
|                                     |                                             |
|                                     v                                             |
|  [2. Profile Module]  ----->  [3. Preference Module]                              |
|      Encapsulates UserProfile        Analyzes affinity, domain weights,           |
|      data attributes                 and pedagogical style                        |
|                                     |                                             |
|                                     v                                             |
|  [4. Prompt Module]                                                               |
|      Constructs structured GPT-4 prompt with strict JSON schema                   |
|                                     |                                             |
|                                     v                                             |
|  [5. Recommendation Module (GPT-4 Engine)]                                        |
|      Generates tailored candidate curriculum items                                |
|                                     |                                             |
|                                     v                                             |
|  [6. Ranking Module]  ----->  [7. Explanation Module]                             |
|      Computes & sorts by             Generates human-readable rationales          |
|      compatibility match score       explaining each recommendation               |
|                                     |                                             |
|                                     v                                             |
|  [11. Main Module (Streamlit GUI & CLI Display)]                                  |
|      Renders ranked recommendations table (Rank, Title, Reason, Score)            |
|                                     |                                             |
|             +-----------------------+-----------------------+                     |
|             |                                               |                     |
|             v                                               v                     |
|     [User Satisfied?]                            [8. Feedback Module]             |
|             |                                      Receives user revision         |
|             |                                      e.g., 'More AI, less Web Dev'  |
|             |                                               |                     |
|             |                                               v                     |
|             |                                    [9. Intent Module]               |
|             |                                      Detects user intent &          |
|             |                                      triggers prompt refinement     |
|             |                                               |                     |
|             |                                               +---> Re-infer GPT-4  |
|             v                                                                     |
|  [10. Save Module]                                                                |
|      Exports finalized recommendation report to CSV, JSON, and Markdown           |
+-----------------------------------------------------------------------------------+
```

---

### Module Design

| Module | Responsibility |
| :--- | :--- |
| **Input Module** | Captures user profile attributes, preference selections, feedback statements, and UI action triggers via Streamlit and CLI. |
| **Profile Module** | Encapsulates, validates, and manages demographic and technical user attributes into a structured UserProfile schema. |
| **Preference Module** | Evaluates user preferences, weights domain interests against goals, and computes semantic affinity scores. |
| **Prompt Module** | Dynamically constructs structured system and user prompts with role definitions, context data, and JSON schema constraints. |
| **Recommendation Module** | Interfaces with GPT-4 (and fallback engine) to generate contextually relevant suggestions tailored to user profiles. |
| **Ranking Module** | Evaluates and sorts recommendations in descending order based on computed compatibility scores and relevancy metrics. |
| **Explanation Module** | Synthesizes transparent, human-readable rationales explaining specifically why each item matches user preferences. |
| **Feedback Module** | Captures iterative user critiques or steering directives (e.g., 'more AI than Web Dev') to initiate real-time refinement. |
| **Intent Module** | Analyzes user conversational feedback using NLP to detect underlying intent (e.g., shift domain, increase difficulty, change format). |
| **Save Module** | Exports finalized recommendations, rationales, rankings, and feedback logs into structured formats (CSV, JSON, Markdown). |
| **Main Module** | Orchestrates workflow execution, coordinates inter-module data flow, manages session state, and controls the UI. |

---

### Implementation 

- **GitHub Link:** [https://github.com/URK23CS1184/Personalized-Recommendation-System-GPT4](https://github.com/URK23CS1184/Personalized-Recommendation-System-GPT4)  
- **LinkedIn Post Link:** [https://www.linkedin.com/in/carlin-sylvester/posts/personalized-recommendation-system-gpt4](https://www.linkedin.com/in/carlin-sylvester/posts/personalized-recommendation-system-gpt4)

---

### Output Screenshots: 

Include screenshots for:

#### ∙ Home Screen 
*(Landing page displaying course badge `24CS2506`, title, student registration `URK23CS1184`, and architectural overview).*

#### ∙ User Profile Input 
*(Input form capturing Name: `Arun`, Age: `20`, Background: `Computer Science`, Interests: `AI, Python`, Skill Level: `Beginner`, Category: `Online Courses`, Goal: `Learn AI`, Preferences: `Practical`, Items: `5`).*

#### ∙ Collected User Profile 
*(Structured profile summary card populated with all 9 validated parameters).*

#### ∙ Preference Analysis 
*(Domain affinity weighting scores: AI & ML (95%), Python (92%), Data Science (85%), Core CS (80%), and hands-on practical pedagogical focus).*

#### ∙ Prompt Generation 
*(Expanded structured markdown prompt containing role instructions, profile data, and strict JSON schema requirements sent to GPT-4).*

#### ∙ GPT-4 Recommendation 
*(Response from the inference engine confirming successful generation of personalized recommendations).*

#### ∙ Recommendation Ranking 

| Rank | Recommendation | Reason | Score |
| :---: | :--- | :--- | :---: |
| 1 | Python for AI | Matches Python and AI interests | 95% |
| 2 | Machine Learning Basics | Suitable for beginner AI learners | 92% |
| 3 | Generative AI | Relevant to current AI interests | 88% |
| 4 | Data Science with Python | Combines Python and data analysis | 85% |
| 5 | Deep Learning Basics | Natural progression after ML | 80% |

#### ∙ Recommendation Explanation 
*(Detailed explanation cards describing the alignment of each recommendation with the user's beginner skill level and practical orientation).*

#### ∙ User Feedback 
*(Conversational feedback injected: `"I am more interested in AI than Web Development."`).*

#### ∙ Intent Detection 
- **Action:** Domain Specialization Shift  
- **Target Focus:** Artificial Intelligence  
- **Deprecated Target:** Web Development  
- **Confidence:** 94% | **Sentiment:** Constructive / Directing  

#### ∙ Refined Recommendations 

| Rank | Recommendation | Reason | Score |
| :---: | :--- | :--- | :---: |
| 1 | Artificial Intelligence | Directly prioritizes core AI foundations as requested in user feedback | 96% |
| 2 | Machine Learning | Essential algorithm concepts aligning with intensified AI interest | 93% |
| 3 | Deep Learning | Expands neural network knowledge per user's focused interest on AI | 90% |
| 4 | Generative AI | Cutting-edge LLM and prompt engineering applications matching AI preference | 87% |
| 5 | Computer Vision | Applies AI techniques to image processing, replacing web development topics | 82% |

#### ∙ Recommendation Saved Successfully 
*(Export confirmation displaying: `✅ Recommendation Saved Successfully! Saved File: saved_recommendations.json`).*

---

### Result: 
Thus, a personalized recommendation system using GPT-4 was successfully developed. The system collects user information, analyzes preferences, generates personalized recommendations, ranks and explains the recommendations, accepts user feedback and produces refined recommendations.
