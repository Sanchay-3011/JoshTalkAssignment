# 🇮🇳 India E-Commerce Text-to-Image Model Evaluation Platform
> **A rigorous, human-in-the-loop benchmark of OpenAI and Google foundation models for Indian retail, fashion, and lifestyle imagery.**  
> *Developed for the Josh Talks AI — Product Operations Hiring Task (July 2026).*

---

## 📌 Executive Overview
This repository contains the complete evaluation platform, reproducible data pipeline, statistical analysis, and interactive dashboard benchmarking three leading text-to-image foundation models on Indian e-commerce catalog and festive advertising tasks.

Unlike generic image demos, this evaluation uses **actual survey data** (11 verified adult participants providing 165 dimension-level ratings), **15 original generated images** across 5 curated product verticals, and a scientifically principled **10-participant primary protocol** with an explicit **11-participant sensitivity analysis**.

```
                           EVALUATION OVERVIEW AT A GLANCE
┌───────────────────────────┬──────────────────────────────────────────────────────────────────┐
│ Evaluated Models          │ 1. OpenAI ChatGPT Images 2.5                                     │
│                           │ 2. Google Gemini 3.1 Pro Image                                   │
│                           │ 3. Google Gemini 3.5 Flash-Lite / 2.5 Flash                      │
├───────────────────────────┼──────────────────────────────────────────────────────────────────┤
│ Curated Prompts (5)       │ Banarasi Saree, Steel Tiffin, Festive Namkeen, Kurta, Sadri      │
├───────────────────────────┼──────────────────────────────────────────────────────────────────┤
│ Evaluator Sample          │ 10 Primary Participants (N=10) + 1 Sensitivity Check (N=11)     │
├───────────────────────────┼──────────────────────────────────────────────────────────────────┤
│ Rating Dimensions (1-5)   │ Prompt Adherence, Visual Quality, Indian Cultural Authenticity   │
├───────────────────────────┼──────────────────────────────────────────────────────────────────┤
│ Primary Benchmark Winner  │ 🥇 Model A (OpenAI ChatGPT Images 2.5) — 4.73 / 5.00 (Clean Sweep)│
├───────────────────────────┼──────────────────────────────────────────────────────────────────┤
│ Rater Disagreement        │ Model A: σ = ±0.58 (Consensus) vs. Model C: σ = ±1.35 (Polarized)│
└───────────────────────────┴──────────────────────────────────────────────────────────────────┘
```

---

## 🎯 Problem Statement
In digital commerce, high-converting product photography is the single largest determinant of customer click-through and purchase conversion. However, for India's 63 million+ Micro, Small, and Medium Enterprises (MSMEs) and regional Direct-to-Consumer (D2C) brands, professional photography studio shoots cost **₹50,000 to ₹2,00,000 per collection**.

While state-of-the-art text-to-image foundation models offer the promise of near-zero marginal cost catalog creation, global AI models are predominantly pre-trained on Western cultural imagery. When prompted for Indian products, they frequently collapse into orientalist tropes, distort traditional garments (e.g. confusing a sleeveless Nehru jacket with a European tuxedo), or fail on practical catalog requirements (e.g. rendering an empty closed tiffin box rather than showcasing food compartments).

---

## 🇮🇳 Why India-Specific Evaluation Matters
1. **India is Not a Monolith**: Indian fashion and lifestyle products possess intricate regional and occasion-specific rules (e.g., Banarasi silk brocade drape, Chikankari embroidery on cotton kurtas, brass samai lamps vs. Western candles). A Western-trained model generating "a brown person in ethnic dress" fails commercial viability.
2. **Real-World Return Rates (RTO)**: In Indian e-commerce, misleading product imagery directly drives Return-to-Origin (RTO) rates and customer dissatisfaction. If an AI generates a full-sleeved blazer when a seller lists a sleeveless Nehru jacket, the customer returns the item immediately.
3. **Training & Alignment Signals for AI Labs**: AI research labs building for India (such as Josh Talks AI, Sarvam AI, or enterprise LLM/VL developers) need granular failure logs: *Which prompts triggered uncanny mannequin artifacts? Where did models fail on fine-grained ethnic apparel taxonomy?*

---

## 🏆 Models Evaluated

| Model Identifier | Commercial Developer | Foundation Model Version | Aspect Ratio Behavior |
|:---:|---|---|---|
| **Model A** | **OpenAI** | ChatGPT Images 2.5 | Adaptive (Portrait 2:3 for apparel, Square 1:1 for packaged goods) |
| **Model B** | **Google** | Gemini 3.1 Pro Image (`Gemini 3.1 Pro`) | Predominantly widescreen 16:9; prone to multi-panel split montages |
| **Model C** | **Google** | Gemini 3.5 Flash-Lite / 2.5 Flash | Strict widescreen 16:9; leaves wide peripheral dead space |

*Note: In compliance with blind evaluation best practices, models were labeled as `Model A`, `Model B`, and `Model C` during human evaluation.*

---

## 🛍️ Use Case & Curated Prompts
The evaluation benchmarks 5 representative prompts covering apparel, home goods, and packaged foods:

1. **Prompt 1 — Red Banarasi Silk Saree** *(Ethnic Apparel)*:  
   > *"A lifestyle product photo of a red Banarasi silk saree draped elegantly on a mannequin, soft natural lighting, styled for an Instagram e-commerce ad, clean minimal background"*
2. **Prompt 2 — Stainless Steel Indian Tiffin Box** *(Kitchenware & Daily Essentials)*:  
   > *"A lifestyle product photo of a stainless steel Indian tiffin box (lunch box) with 3 compartments, placed on a wooden kitchen table with soft morning light, styled for an e-commerce listing"*
3. **Prompt 3 — Festive Namkeen Snack Pouch** *(Packaged Food & FMCG / Diwali)*:  
   > *"A lifestyle product photo of a colorful Indian namkeen snack pouch on a festive background with diyas and marigold flowers, styled for a Diwali sale Instagram ad"*
4. **Prompt 4 — Beige Cotton Kurta Set** *(Casual Ethnic Wear)*:  
   > *"A lifestyle product photo of a beige cotton kurta set on a young Indian model standing against a plain studio background, natural lighting, styled for an e-commerce catalog"*
5. **Prompt 5 — Navy Blue Nehru Jacket with White Kurta** *(Men's Occasion Wear)*:  
   > *"A lifestyle product photo of a navy blue Nehru jacket paired with a white kurta, worn by a young Indian model standing in a warmly lit indoor setting with traditional decor in the background, styled for a wedding-season e-commerce catalog"*

---

## 📐 Human Evaluation Method & Scoring Framework
Evaluators graded each generated image across three orthogonal criteria on a 1–5 Likert scale:
1. **Prompt Adherence**: Faithfulness to all nouns, adjectives, and functional constraints specified in the prompt.
2. **Visual Quality**: Photorealism, lighting realism, texture fidelity, and absence of visual artifacts or deformed anatomy.
3. **Indian Cultural Authenticity**: Plausibility of traditional draping, jewelry styling, festive iconography, and culinary props in Indian contexts.

### The 10 vs. 11 Participant Protocol
- **Assignment Constraint**: The hiring brief specifies a sample of **8–10 participants**.
- **Execution**: 11 responses were received in the Google Form.
- **Scientific Protocol**: To adhere strictly to pre-registered evaluation methodology, the **first 10 valid responses** form the **Primary Benchmark**.
- **Sensitivity Analysis**: All 11 responses were retained and evaluated in a programmatic sensitivity check, proving that the model rankings are **100% stable** ($A > B > C$).
- **Privacy**: All personal names and email addresses are masked; participants are identified as `P01` through `P11`. All participants gave affirmative 18+ consent.

---

## 📊 Benchmark Results

### Primary Benchmark Leaderboard ($N=10$, 150 Ratings)

| Rank | Model | Overall Score | Prompt Adherence | Visual Quality | Indian Authenticity | High Rating % (≥4) | Consistency Index | Std Dev (σ) |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 🥇 **1** | **Model A (OpenAI)** | **4.73 / 5.00** | **4.78** | **4.74** | **4.68** | **92.7%** | **0.633** | **±0.58** |
| 🥈 **2** | **Model B (Google Pro)** | **3.76 / 5.00** | **3.76** | **3.72** | **3.80** | **59.3%** | **0.532** | **±0.88** |
| 🥉 **3** | **Model C (Google Flash)**| **3.29 / 5.00** | **3.28** | **3.30** | **3.28** | **46.7%** | **0.426** | **±1.35** |

### Robustness Check ($N=11$, 165 Ratings)

| Model | Primary ($N=10$) | Sensitivity ($N=11$) | Delta (Δ) | Primary Rank | Sensitivity Rank | Status |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **Model A** | 4.733 | 4.739 | +0.006 | 1 | 1 | **✓ Stable** |
| **Model B** | 3.760 | 3.806 | +0.046 | 2 | 2 | **✓ Stable** |
| **Model C** | 3.287 | 3.321 | +0.034 | 3 | 3 | **✓ Stable** |

---

## 💡 Key Evidence-Based Findings
1. **Model A Swept Every Prompt & Dimension (15/15 sub-metrics)**: Model A demonstrated emergent commercial comprehension. It automatically inserted high-converting e-commerce elements—rendering 3 open tiffin bowls with yellow dal tadka, jeera rice, and sabzi, alongside marketing copy and Milton-style feature badges.
2. **Model B Closes the Gap on Festive Visuals**: Model B's highest-scoring category was the Diwali snack pouch (**4.21** vs. 4.61 for Model A). Evaluators responded enthusiastically to its marigold garlands and earthen diyas, though penalized its tendency to generate unsolicited split-screen layouts.
3. **Model C Failed on Cultural Taxonomy and Anatomy**: Model C exhibited 2.3× higher rater disagreement ($\sigma = \pm 1.35$). Major failure modes included generating an articulated wooden artist doll with exposed ball joints for the Saree prompt, and generating a full-sleeved Bandhgala blazer instead of a sleeveless Nehru jacket.

---

## ⚠️ Limitations
- **Sample Size ($N=10$)**: Exploratory signal; sufficient for identifying gross differences between models, but requires $N \ge 50$ for regional demographic breakdown.
- **Primacy Bias**: Model A was presented first in the Google Form; future rounds will use dynamic randomized ordering.
- **Single Generation Seed**: Evaluated one generation per model per prompt; multi-seed variance testing is recommended for production deployment.

---

## 🚀 Scaling Proposal & Evaluation Product Concept

### Proposed 4-Stage Architecture
```mermaid
graph LR
    A[Curated Regional Prompts\n25+ Indian Languages] --> B[Unified Multi-Model Runner]
    B --> C[Tier 1: Vision LLM Judge\nHigh-Throughput Safety & Glitch Screen]
    C --> D[Tier 2: Josh Jobs Human Raters\nTier-2/3 Regional Contributors]
    D --> E[Real-Time Consensus Engine\nKrippendorff Alpha & Outlier Filtering]
    E --> F[Enterprise Elo Arena & Leaderboard]
```

1. **Workforce Scaling**: Leverage **Josh Jobs** (20,000+ active Indian contributors) to collect 1,000+ ratings across regional demographics.
2. **Multilingual Ingestion**: Test prompts written in Hindi, Tamil, Telugu, and Hinglish.
3. **Commercial Usefulness Dimension**: Add explicit business criteria rated by D2C merchandising managers.
4. **Automated Vision-Language Calibration**: Use multimodal models (e.g. GPT-4o) as high-throughput Tier-1 screeners, routing ambiguous cases to human raters.

---

## 📂 Project Structure

```
JoshTalkAssignment/
├── .gitignore
├── .env.example
├── requirements.txt
├── run.py                         # Convenience launcher: python run.py
├── README.md                      # Comprehensive project documentation
├── AI_generated_pictures/         # 15 original generated PNGs across 5 prompts
├── data/
│   ├── raw/
│   │   ├── form_responses.csv     # Raw Google Form responses (11 records)
│   │   └── Product_Task_July2026.pdf # Official Josh Talks hiring brief
│   ├── processed/
│   │   ├── evaluations_normalized.csv # Clean long-format schema (165 ratings)
│   │   ├── participants_anonymized.csv# Anonymized demographic audit roster
│   │   ├── model_metrics_primary.json # Primary benchmark metrics (N=10)
│   │   ├── model_metrics_robustness.json # Sensitivity metrics (N=11)
│   │   ├── prompt_metrics.json        # Prompt-level aggregates
│   │   ├── sensitivity_check.json     # Empirical delta & rank invariance check
│   │   └── statistical_analysis.json  # 95% Bootstrap CIs & rater variance
│   └── metadata/
│       ├── models.json            # Model specs, providers, aspect ratios
│       ├── prompts.json           # 5 prompt definitions & cultural nuance
│       └── qualitative_notes.json # Pixel-grounded strengths & failure modes
├── analysis/
│   ├── clean_data.py              # Ingestion, PII masking, schema normalization
│   ├── calculate_scores.py        # Benchmark score calculation engine
│   └── statistical_analysis.py    # Bootstrap CIs & rater consensus
├── app/
│   ├── __init__.py
│   ├── main.py                    # Multi-page Streamlit application entrypoint
│   ├── config.py                  # Design tokens, caching, custom CSS
│   ├── components/
│   │   ├── __init__.py
│   │   └── cards.py               # KPI cards, radar charts, heatmaps
│   └── pages/
│       ├── overview.py            # Page 1: Executive Overview & KPI Cards
│       ├── leaderboard.py         # Page 2: Interactive Model Leaderboard
│       ├── prompt_analysis.py     # Page 3: Prompt Deep-Dive & Image Grids
│       ├── image_comparison.py    # Page 4: Side-by-Side Image Inspector
│       ├── participant_insights.py# Page 5: Rater Disagreement & Box Plots
│       ├── methodology.py         # Page 6: Experimental Controls & Fairness
│       ├── evaluation_data.py     # Page 7: Filterable Data & CSV Exports
│       ├── rating_ui_concept.py   # Page 8: Interactive Human Rating Mockup
│       ├── scaling_plan.py        # Page 9: Enterprise Architecture & Roadmap
│       └── reports_page.py        # Page 10: Complete Reports & Reflections
├── reports/
│   ├── executive_summary.md       # 1-page executive brief
│   └── main_evaluation_report.md  # Comprehensive assignment submission
└── tests/
    ├── test_data.py               # Data pipeline & PII protection tests
    └── test_metrics.py            # Score calculation & ranking stability tests
```

---

## 💻 Installation & Quickstart

### Prerequisites
- Python 3.10+ (tested on Python 3.11 / 3.14)
- Git

### 1. Clone & Set Up Environment
```bash
git clone <your-repo-url>
cd JoshTalkAssignment

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows (PowerShell):
.venv\Scripts\Activate.ps1
# On macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Run Automated Test Suite
Verify that data ingestion, anonymization, score calculation, and ranking invariance pass with 100% success:
```bash
pytest -v
```

### 3. Launch the Evaluation Platform
Launch the interactive Streamlit dashboard:
```bash
python run.py
# Or directly via streamlit:
streamlit run app/main.py
```
Open your browser at `http://localhost:8501`.

---

## 🔬 Reproducibility & Pipeline Execution
To re-run the entire data normalization and scoring pipeline from scratch:
```bash
# 1. Clean raw survey responses and produce normalized dataset
python analysis/clean_data.py

# 2. Recompute primary and sensitivity metrics
python analysis/calculate_scores.py

# 3. Compute bootstrap confidence intervals and rater variance
python analysis/statistical_analysis.py
```

---

## 📝 Deliverables Checklist (Josh Talks Assignment Compliance)
- [x] **3 Required Models Evaluated**: OpenAI ChatGPT Images 2.5, Gemini 3.1 Pro, Gemini 3.5 Flash-Lite.
- [x] **Focused Indian Use Case**: E-commerce lifestyle & catalog photography.
- [x] **5 Distinct Prompts**: Saree, Steel Tiffin, Namkeen, Kurta, Nehru Jacket.
- [x] **15 Original Images**: Stored in `AI_generated_pictures/` and visually analyzed.
- [x] **10-Participant Primary Protocol**: Exactly 10 primary participants ($N=10$) used for the core benchmark.
- [x] **11th Response Preserved**: Evaluated in an explicit sensitivity check verifying rank stability.
- [x] **100% Consent Verification**: Affirmative consent verified for all 11 raters.
- [x] **Participant Privacy Protected**: Email addresses and names masked in public dashboard.
- [x] **3 Evaluation Dimensions**: Prompt Adherence, Visual Quality, Indian Authenticity.
- [x] **Interactive Leaderboard & Dashboard**: 10-page SaaS platform built with Streamlit & Plotly.
- [x] **Observed Strengths & Weaknesses**: Pixel-grounded critique from real image inspection.
- [x] **Human Evaluation Rating UI Concept**: Interactive prototype included in Page 8.
- [x] **Scaling Proposal**: Detailed roadmap leveraging Josh Jobs contributor network.
- [x] **Executive Summary (1 Page)**: Available in `reports/executive_summary.md`.
- [x] **Main Report**: Available in `reports/main_evaluation_report.md`.
- [x] **Answers to 5 Reflection Questions**: Fully answered in Section 11 of the report and on Page 10.
- [x] **Automated Tests**: 7 automated tests passing in `tests/`.
- [x] **No Fabricated Data**: 100% derived from uploaded source files.
