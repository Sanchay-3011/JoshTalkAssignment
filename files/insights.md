# Evaluation Insights — Text-to-Image Models for Indian E-commerce

**Sample:** 11 human raters, 5 product prompts, 3 blind-labeled models (A/B/C), 3 criteria per image (Prompt Match, Visual Quality, Indian Authenticity), 1-5 Likert scale. 165 total image ratings collected via Google Form with consent.

## Overall Results

| Model | Avg. Prompt Match | Avg. Visual Quality | Avg. Indian Authenticity | **Overall Score** | Rater Agreement (lower std = more consensus) |
|---|---|---|---|---|---|
| **Model A** | 4.80 | 4.76 | 4.47 | **4.74** 🏆 | 0.55 (high consensus) |
| Model B | 3.85 | 3.76 | 3.80 | 3.81 | 0.88 (moderate) |
| Model C | 3.44 | 3.29 | 3.24 | 3.32 | 1.33 (low consensus — raters disagreed most) |

## Results by Product Category

| Category | Model A | Model B | Model C |
|---|---|---|---|
| Saree | 4.73 | 3.61 | 3.15 |
| Steel Tiffin Box | 4.85 | 3.91 | 3.18 |
| Namkeen Snack Pouch | 4.61 | 4.21 | 3.21 |
| Kurta Set | 4.76 | 3.88 | 3.55 |
| Nehru Jacket | 4.76 | 3.42 | 3.52 |

## Key Findings

**1. Model A wins on every single prompt and every single criterion, with no exceptions.**
This is an unusually clean sweep across 5 categories × 3 criteria (15/15). That consistency is itself worth flagging as a finding: it suggests Model A has a genuinely strong, stable advantage for Indian e-commerce lifestyle photography — the gap isn't noise, since Model A also has the *lowest* rater disagreement (0.55 avg std dev), meaning raters were unusually unanimous. **Caveat:** since Model A was consistently labeled "Model A" and (if) shown first in the form for every prompt, this result should be read alongside a check for order/position bias — a possible improvement flagged below.

**2. Model B is a distant-but-respectable second**, and closes the gap most on culturally-specific/festive prompts (Namkeen Snack Pouch, its best relative showing at 4.21) — suggesting it handles festive Indian visual motifs (diyas, marigolds) better than plain studio product shots.

**3. Model C consistently trails and shows the highest rater disagreement (std dev 1.33 vs. 0.55 for Model A)** — nearly 2.5x more variance. This means raters didn't just rate Model C lower on average, they actively *disagreed* with each other about it — some rated it 1, others rated the same image 5. This is a meaningfully different failure mode from Model B (consistently mediocre): Model C is polarizing, likely producing outputs that are hit-or-miss rather than reliably weak — a distinction a mean score alone hides.

**4. "Indian Authenticity" tracked closely with the other two criteria rather than diverging** — models that matched the prompt and looked visually strong were also generally rated as culturally authentic. This suggests, for this specific e-commerce use case, cultural fit issues show up as general quality/coherence failures rather than a separate, isolated failure mode (unlike what might be expected — e.g., a technically sharp image that still "feels wrong" for India). Worth testing on a broader prompt set before generalizing this.

## Limitations & What I'd Improve With More Time
- **Order bias check**: verify/re-run with the A/B/C position independently randomized per rater per prompt (not just per prompt) to rule out primacy effects fully.
- **Sample size**: 11 raters is enough for directional signal, not statistical significance — I'd target 30+ for a confident production decision.
- **Pairwise (Elo-style) comparison** instead of independent 1-5 Likert scoring would likely sharpen the Model B vs C distinction, which currently overlaps more than the A vs B/C gap.
