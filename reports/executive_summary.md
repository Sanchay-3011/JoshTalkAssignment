# Executive Summary: Text-to-Image Model Evaluation for Indian E-Commerce
**Josh Talks AI — Product Operations Hiring Task**  
**Evaluation Scope:** 3 Foundation Models · 5 Indian E-Commerce Prompts · 15 Generated Outputs · 10 Primary Evaluators (165 Criteria Ratings) · Blind Evaluation Protocol  

---

### Core Objective & Problem Statement
High-converting lifestyle and product photography is the single largest visual driver of digital retail conversion. However, for India's 63M+ MSMEs and emerging D2C brands, professional studio shoots cost ₹50,000–₹2,00,000 per collection. While generative text-to-image models promise near-zero marginal cost catalog creation, global models are predominantly trained on Western aesthetics. This evaluation rigorously tests whether current foundation models can generate commercially viable, culturally authentic imagery tailored to Indian consumers.

### Evaluated Models & Setup
1. **Model A:** OpenAI — ChatGPT Images 2.5
2. **Model B:** Google — Gemini 3.1 Pro Image (`Gemini 3.1 Pro`)
3. **Model C:** Google — Gemini 3.5 Flash-Lite / 2.5 Flash (`Gemini 3.5-flash`)
- **Evaluation Categories:** Ethnic Apparel (Saree, Kurta, Nehru Jacket), Kitchenware (Steel Tiffin Box), FMCG/Packaged Food (Festive Namkeen Pouch).
- **Judging Criteria (1–5 Likert Scale):** *Prompt Adherence*, *Visual Quality*, and *Indian Cultural Authenticity*.
- **Sample Protocol:** Primary benchmark calculated on the first **10 verified adult participants** ($N=10$) with 100% written consent. An 11th response was collected and evaluated via an explicit sensitivity check.

---

### Official Primary Benchmark Leaderboard (N=10)

| Rank | Model | Overall Score | Prompt Match | Visual Quality | Indian Authenticity | High Rating % (≥4) | Disagreement (StdDev) |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| 🥇 **1** | **Model A (OpenAI ChatGPT Images 2.5)** | **4.73 / 5.00** | **4.78** | **4.74** | **4.68** | **92.7%** | **±0.58 (High Consensus)** |
| 🥈 **2** | **Model B (Google Gemini 3.1 Pro)** | **3.76 / 5.00** | **3.76** | **3.72** | **3.80** | **59.3%** | **±0.88 (Moderate)** |
| 🥉 **3** | **Model C (Google Gemini Flash-Lite)**| **3.29 / 5.00** | **3.28** | **3.30** | **3.28** | **46.7%** | **±1.35 (Polarized)** |

*Sensitivity Robustness Check ($N=11$): Model A (4.74) > Model B (3.81) > Model C (3.32). The ranking hierarchy is 100% invariant to sample size adjustments.*

---

### Top Three Findings
1. **Clean Sweep by Model A (OpenAI):** Model A secured first place across all 5 prompts and all 3 criteria (15/15 sub-metrics). Crucially, Model A understands commercial ad composition—automatically rendering appropriate marketing typography, Indian jewelry (pearl choker, jhumkas, bindi), and interior food items inside the 3-tier tiffin.
2. **Model B Competes Strongly in Festive Visuals:** Model B achieved its highest relative score on the festive snack prompt (**4.21** vs. 4.61 for Model A), accurately depicting diyas and marigold garlands. However, its tendency to generate unsolicited widescreen triptychs and split-screen montages harms catalog ingestion.
3. **Model C Suffers from Semantic & Physical Hallucinations:** Model C exhibited 2.3× higher rater variance than Model A. Evaluators heavily penalized its use of an articulated wooden artist doll for the Saree prompt and its misinterpretation of a sleeveless Nehru jacket as a full-sleeved Bandhgala blazer.

---

### Key Takeaway for Product & AI Teams
**OpenAI ChatGPT Images 2.5 is currently the only enterprise-ready model for turnkey Indian e-commerce lifestyle generation.** For an AI lab building tools for India, fine-tuning must target fine-grained ethnic fashion taxonomy (Nehru sadri vs. Bandhgala) and commercial listing layouts (vertical 2:3 catalog portraits with visible compartments).
