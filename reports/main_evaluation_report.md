# Text-to-Image Foundation Model Evaluation: Indian E-Commerce Use Case
**Josh Talks AI — Product Operations Hiring Task: Question 1**  
*Author:* Product Operations Candidate  
*Date:* September 2026  
*Focus:* Systematic Human Evaluation of Text-to-Image Foundation Models for Indian E-Commerce Imagery  

---

## 1. Executive Summary
This report presents an empirical, human-in-the-loop evaluation comparing three premier image generation models on five representative Indian e-commerce listing and lifestyle advertisement prompts.

Using a primary cohort of **10 verified adult participants** ($N=10$) providing **150 primary rating points** (plus an 11th participant evaluated under a sensitivity protocol), each generated image was evaluated across three orthogonal dimensions on a 1–5 Likert scale: **Prompt Adherence**, **Visual Quality**, and **Indian Cultural Authenticity**.

### Core Results Summary
- **Model A (OpenAI GPT Image 1 / ChatGPT Image)** decisively ranked **#1** with an overall score of **4.73 / 5.00**, leading across every prompt and every evaluated dimension with the lowest evaluator disagreement ($\sigma = \pm 0.58$).
- **Model B (Google Gemini 3.1 Pro Image)** placed **#2** with an overall score of **3.76 / 5.00**, demonstrating strong festive decorative motifs but hindered by unwanted multi-panel composite compositions.
- **Model C (Google Gemini 3.5 Flash-Lite / 2.5 Flash)** placed **#3** with an overall score of **3.29 / 5.00**, exhibiting high rater disagreement ($\sigma = \pm 1.35$) caused by severe cultural misclassifications (e.g. generating a full-sleeved Bandhgala blazer instead of a sleeveless Nehru jacket).

---

## 2. Evaluation Objective
The objective of this evaluation is to answer a practical business question:  
> **"Which state-of-the-art text-to-image foundation model is most commercially viable and culturally authentic for generating Indian e-commerce product and lifestyle imagery?"**

Unlike broad, academic vision benchmarks that evaluate abstract objects or Western scenarios, this benchmark focuses directly on the economic and cultural realities of Indian digital commerce.

---

## 3. Why Indian E-Commerce Evaluation Matters
1. **Economic Bottleneck for MSMEs**: India is home to over 63 million Micro, Small, and Medium Enterprises (MSMEs). Catalog photography with professional models, makeup artists, and studio lighting costs between ₹50,000 and ₹2,00,000 per collection. If generative AI can produce photorealistic catalog listings, it democratizes high-conversion visual marketing for tier-2/3 sellers.
2. **Failure of Western Assumptions in Indian Contexts**: Global text-to-image models are predominantly pre-trained on Western stock photography. When prompted for Indian garments or lifestyle goods, models frequently collapse into orientalist caricatures, misinterpret traditional draping physics (e.g. saree pleats and pallu orientation), or confuse distinct garments (e.g. Sadri vs. Bandhgala).
3. **High Commercial Sensitivity**: In e-commerce, imagery directly dictates Return on Ad Spend (ROAS) and Return-to-Origin (RTO) rates. An image that misrepresents garment cut or fabric drape leads directly to customer cancellations and returns.

---

## 4. Evaluated Models & Generation Configuration
Per the Josh Talks assignment specifications, the evaluation benchmarks three required foundation models:

| Model ID | Provider | Exact Model Name | Target Resolution | Architectural & Aspect Ratio Behavior |
|---|---|---|---|---|
| **Model A** | OpenAI | GPT Image 1 (`ChatGPT Image 1`) | 1024×1536 / 1254×1254 | Adaptive: Vertical 2:3 for apparel; 1:1 square for packaged items |
| **Model B** | Google | Gemini 3.1 Pro Image (`Gemini 3.1 Pro`) | 2816×1536 / 2048×2048 | Predominantly widescreen 16:9; prone to multi-panel split montages |
| **Model C** | Google | Gemini 3.5 Flash-Lite / 2.5 Flash | 2816×1536 | Strict widescreen 16:9; leaves wide peripheral dead space |

---

## 5. Evaluation Prompts & Cultural Nuances
Five prompts were designed spanning major Indian retail categories:

1. **Prompt 1 (Red Banarasi Silk Saree)**:  
   *"A lifestyle product photo of a red Banarasi silk saree draped elegantly on a mannequin, soft natural lighting, styled for an Instagram e-commerce ad, clean minimal background"*  
   *Nuance Tested:* Zari embroidery sheen, silk fabric pleating, jewelry styling, luxury ad framing.
2. **Prompt 2 (Stainless Steel Indian Tiffin Box)**:  
   *"A lifestyle product photo of a stainless steel Indian tiffin box (lunch box) with 3 compartments, placed on a wooden kitchen table with soft morning light, styled for an e-commerce listing"*  
   *Nuance Tested:* 3-tier container structure, carrying clamp, home-cooked food items (dal, rice, sabzi).
3. **Prompt 3 (Festive Namkeen Snack Pouch)**:  
   *"A lifestyle product photo of a colorful Indian namkeen snack pouch on a festive background with diyas and marigold flowers, styled for a Diwali sale Instagram ad"*  
   *Nuance Tested:* Packaged FMCG branding, Haldiram-style pouch, crispy bhujia sev, festive marigolds and earthen diyas.
4. **Prompt 4 (Beige Cotton Kurta Set)**:  
   *"A lifestyle product photo of a beige cotton kurta set on a young Indian model standing against a plain studio background, natural lighting, styled for an e-commerce catalog"*  
   *Nuance Tested:* Clean studio catalog portrait (Myntra/Ajio standard), Chikankari embroidery, bindi, mojaris/juttis, natural Indian female facial features.
5. **Prompt 5 (Navy Blue Nehru Jacket with White Kurta)**:  
   *"A lifestyle product photo of a navy blue Nehru jacket paired with a white kurta, worn by a young Indian model standing in a warmly lit indoor setting with traditional decor in the background, styled for a wedding-season e-commerce catalog"*  
   *Nuance Tested:* Sleeveless Nehru sadri vest vs. full-sleeved coat, mandarin collar, festive Indian wedding backdrop.

---

## 6. Evaluation Methodology & Sampling Protocol
- **Blinded Presentation**: Models were labeled anonymously (`Model A`, `Model B`, `Model C`) in the Google Form survey to prevent brand prestige bias.
- **Rating Scale**: Each image was independently scored on a 1–5 Likert scale across:
  1. *Prompt Adherence*: Did the output follow all nouns, adjectives, and constraints?
  2. *Visual Quality*: Is the image sharp, well-lit, and free of physical/anatomical glitches?
  3. *Indian Cultural Authenticity*: Does it feel natural, plausible, and authentic for Indian consumers?
- **Sampling Protocol (10 Primary vs. 11 Robustness)**:
  - The Josh Talks brief requests 8–10 human raters.
  - 11 responses were collected.
  - To respect protocol pre-registration, the **first 10 valid responses** formed the **Primary Benchmark**.
  - All 11 responses were evaluated in an explicit **Sensitivity & Robustness Check**.
  - No data was deleted or concealed.
- **Participant Privacy & Consent**: 100% of participants confirmed age 18+ and executed the formal consent clause. Email addresses and full names have been redacted in all public application tables and replaced with anonymous IDs (`P01` to `P11`).

---

## 7. Comprehensive Results & Leaderboard

### Primary Leaderboard ($N=10$ Participants, 150 Ratings)

| Rank | Model | Overall Score | Prompt Adherence | Visual Quality | Indian Authenticity | High Rating % (≥4) | Consistency Index | Std Dev (σ) |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 🥇 1 | **Model A** | **4.73** | 4.78 | 4.74 | 4.68 | **92.7%** | 0.633 | ±0.58 |
| 🥈 2 | **Model B** | **3.76** | 3.76 | 3.72 | 3.80 | **59.3%** | 0.532 | ±0.88 |
| 🥉 3 | **Model C** | **3.29** | 3.28 | 3.30 | 3.28 | **46.7%** | 0.426 | ±1.35 |

### Sensitivity / Robustness Check ($N=11$ Participants, 165 Ratings)

| Model | Primary Score ($N=10$) | Robustness Score ($N=11$) | Delta (Δ) | Primary Rank | Robustness Rank | Rank Invariant? |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **Model A** | 4.733 | 4.739 | +0.006 | 1 | 1 | **✓ Yes (Stable)** |
| **Model B** | 3.760 | 3.806 | +0.046 | 2 | 2 | **✓ Yes (Stable)** |
| **Model C** | 3.287 | 3.321 | +0.034 | 3 | 3 | **✓ Yes (Stable)** |

*Conclusion: Model rankings are 100% robust against the inclusion of the 11th rater.*

---

## 8. Prompt-Level Findings Grounded in Real Image Evidence

### Prompt 1: Red Banarasi Silk Saree
- **Model A (4.73)**: Superb rendering of metallic gold zari work and authentic silk sheen. Rendered an Instagram ad layout with elegant typography ("Timeless Tradition - BANARASI SILK SAREE"), pearl necklace, and brass urli bowl.
- **Model B (3.61)**: Produced an unexpected 3-panel triptych composite. While textile patterns were acceptable, the widescreen format cannot be used in vertical mobile ads without cropping.
- **Model C (3.15)**: Generated an articulated wooden artist drawing mannequin with visible ball-and-socket joints. Evaluators found this bizarre and unappealing for luxury ethnic wear.

### Prompt 2: Stainless Steel Tiffin Box
- **Model A (4.85)**: Flawless e-commerce listing hero shot. Showcased the 3-tier container both stacked and open, revealing yellow dal tadka, jeera rice, and sabzi, accompanied by clean feature badges ("Food Grade Stainless Steel", "Leak Proof & Durable").
- **Model B (3.91)**: Attractive rustic kitchen setting with Indian masala dabba and mango pickle, but lacked the outer clamping frame that binds tiffin towers together.
- **Model C (3.18)**: Kept the tiffin 100% closed. While photorealistic, it failed the functional requirement of demonstrating interior compartments.

### Prompt 3: Festive Namkeen Snack Pouch
- **Model A (4.61)**: Ultra-realistic Haldiram-style stand-up pouch ("INDIAN NAMKEEN BHUJIA") complete with green veg dot, brass bowl of crispy sev and peanuts, glowing diyas, and Diwali sale marketing copy.
- **Model B (4.21)**: Model B's strongest showing. Produced a colorful "Festive Treats" pouch with "DIWALI SALE! UP TO 40% OFF" promotional overlay, narrowing the gap with Model A.
- **Model C (3.21)**: Wide landscape banner with kaju katli sweets; diluted central product focus.

### Prompt 4: Beige Cotton Kurta Set
- **Model A (4.76)**: Indistinguishable from a professional Myntra or Fabindia catalog photo. Young Indian model with natural facial features, bindi, oxidised jhumkas, and Chikankari embroidery. Vertical 2:3 catalog framing.
- **Model B (3.88)**: Model was barefoot on a wide empty floorboard background, which evaluators noted felt unstyled for a commercial catalog.
- **Model C (3.55)**: Modern palazzo silhouette with juttis, but horizontal 16:9 framing left large empty wall space on the right.

### Prompt 5: Navy Blue Nehru Jacket
- **Model A (4.76)**: 100% prompt adherence: sleeveless navy blue sadri vest with mandarin collar, metallic engraved buttons, and pocket square over a white kurta in an upscale Indian interior.
- **Model B (3.42)**: Split-screen composite (full body + close-up) that breaks standard catalog upload specifications.
- **Model C (3.52)**: **Critical prompt failure**: Generated a full-sleeved Bandhgala blazer instead of a sleeveless Nehru jacket. In apparel e-commerce, this constitutes an unacceptable product defect.

---

## 9. Limitations & Statistical Caveats
1. **Sample Size ($N=10$)**: While sufficient to reveal large effect sizes (e.g. Model A's decisive advantage), $N=10$ cannot capture regional sub-variations across India's diverse states.
2. **Order / Primacy Bias**: Because Model A was displayed first in the Google Form, a slight primacy bias cannot be fully ruled out until randomized presentation is deployed.
3. **Single-Seed Generations**: Only one generation per prompt per model was tested; multi-seed variance remains to be explored.
4. **Lack of Live Conversion Data**: Ratings reflect aesthetic preference, not live checkout conversion or return rates.

---

## 10. Scaling Proposal: Josh Talks AI Vision Evaluation Engine
- **Rater Scaling**: Tap the **Josh Jobs** contributor base (20,000+ freelance transcribers across Tier-2/3 India) to scale to 100+ demographically matched raters.
- **Multilingual Prompts**: Benchmark prompt comprehension across 25+ Indian languages (Hindi, Tamil, Telugu, Marathi).
- **Hybrid Vision-LLM + Human Funnel**: Use Vision LLMs (e.g. GPT-4o / Gemini 1.5 Pro) as high-throughput Tier-1 screeners, routing top outputs to human raters for cultural validation.
- **Elo Pairwise Arena**: Transition to blind head-to-head A/B battles to establish continuous live foundation model rankings.

---

## 11. Final Reflections (The 5 Mandatory Questions)

### 1. Why did you choose this eval?
I chose Indian e-commerce lifestyle and product visual generation because it represents the highest-value, near-term commercial application of generative vision models in India. Direct-to-Consumer (D2C) brands and millions of small MSME sellers on Meesho, Flipkart, and Myntra spend substantial capital on physical catalog shoots. Evaluating whether AI can autonomously generate authentic Indian catalog assets directly tackles an acute economic pain point.

### 2. Why is it useful for India?
Western foundation models frequently fail on Indian cultural and sartorial specifics. They confuse a sleeveless Nehru sadri with a European blazer, render cartoonish representations of Indian people, or miscalculate traditional saree pleats. Running an India-specific evaluation establishes accountability, ensuring AI models serve Indian cultural nuance rather than imposing Western defaults.

### 3. Why would an AI lab building for India care about it?
An AI lab (such as Josh Talks AI, Sarvam AI, or enterprise foundation model builders) cannot guide model training or RLHF alignment using Western benchmarks like MS-COCO. They need domain-specific failure logs: *Which prompts triggered anatomical artifacts? Where did the model confuse ethnic garments?* This evaluation provides labs with actionable fine-tuning signals.

### 4. What did you learn from running the sample?
- **Model A (OpenAI) demonstrates emergent commercial intelligence**: It did not just draw the object; it acted as an art director, adding ad typography, feature badges, and complementary Indian props.
- **Cultural authenticity and general visual quality are correlated**: When models failed on cultural specifics (e.g. Model C's wooden dummy), evaluators marked down visual quality and prompt adherence in tandem.
- **Model C is polarized, not simply mediocre**: Model C had a high standard deviation ($\pm 1.35$), meaning outputs were hit-or-miss rather than uniformly weak.

### 5. What would you improve with more time?
- **Randomized Presentation Order**: Dynamically shuffle image positions per rater per prompt to eliminate primacy bias.
- **Scale Sample Size**: Expand to 50+ raters with demographic and regional stratification.
- **Pairwise Elo Battles**: Use side-by-side A/B comparisons rather than independent Likert scores to eliminate rater scale calibration variance.
- **Multi-Seed Testing**: Generate 5 seeds per prompt to measure within-model consistency.
