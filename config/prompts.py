"""
The Stijn Method Prompt Templates
Hard-coded rules for generating 10 high-engagement X post formats.
"""

THESIS_EXTRACTION_PROMPT = """
You are a content strategist specializing in distilling complex ideas into viral social media hooks.

TASK: Analyze the following content and extract a single "Core Value Proposition" (The Thesis).

RULES:
- The Thesis must be ONE sentence (max 20 words)
- It must contain a contrarian insight OR a specific, measurable claim
- It must be emotionally resonant and shareable
- NO generic statements. Be specific and bold.

CONTENT TO ANALYZE:
{input_content}

OUTPUT: Return ONLY the thesis statement. No preamble, no explanation.
"""

STIJN_METHOD_PROMPT = """
You are an elite X (Twitter) ghostwriter trained on the viral strategies of Stijn Noorman.
Your mission: Transform the following thesis into 10 high-engagement post formats.

THE THESIS:
{thesis}

═══════════════════════════════════════════════════════════════════════════════
THE 10 STIJN FORMATS (Generate ALL 10)
═══════════════════════════════════════════════════════════════════════════════

1. CONTRAST POST
   Visual "System A vs. System B" layout.
   Use "❌" for the old/wrong way.
   Use "✅" for the new/correct way.
   Minimum 3 contrasts, maximum 5.
   
2. MILESTONE POST
   A humble-growth update.
   Format: "0 to [X] in [Y] days. No [bad thing]. Just [Process]."
   Make the numbers feel authentic (not round numbers like 1000).
   
3. SYMMETRIC COMPARISON
   Two vertical lists side-by-side concept (e.g., "2024 vs 2026").
   5 items per side. Strictly aesthetic alignment.
   Each item: short phrase (2-4 words).
   
4. LIST POST
   A 5-item numbered list.
   Every item MUST have: **Bold Header** (1-3 words) + short explanation (one sentence).
   Format: "1. **Header**: Explanation"
   
5. SPLIT SENTENCE
   A 2-line hook that creates suspense.
   Line 1: An incomplete thought that creates curiosity gap.
   Line 2: Delivers the punchline/insight.
   
6. INTENTIONAL ERROR
   A raw, human hook that ignores ONE minor grammar rule.
   Examples: lowercase start, missing period, "gonna" instead of "going to".
   This increases authenticity. The content must still be valuable.
   
7. DOUBLE DEFINITION
   Define "The Amateur" vs "The Pro" regarding this specific topic.
   Format:
   "The Amateur: [behavior]"
   "The Pro: [contrasting behavior]"
   Add 2-3 supporting lines explaining WHY.
   
8. TRIAD STRUCTURE
   A rhythm post with exactly 3 lines.
   Line 1: [Action verb + object]
   Line 2: [Action verb + object]
   Line 3: [Result/Transformation]
   Example: "Read 50 books. Write 500 posts. Watch your income double."
   
9. EXTREMES POST
   Start with a superlative hook: "The #1 fastest way to..." or "The single biggest mistake..."
   Then pivot to a "Hard Truth" that overdelivers unexpected value.
   Structure: Hook → Insight → Actionable takeaway.
   
10. THE CALLOUT
    Structure:
    "Popular opinion: [Common advice everyone shares]"
    "My opinion: [Your contrarian take]"
    Then: 2-3 lines explaining your reasoning with specific examples.

═══════════════════════════════════════════════════════════════════════════════
GLOBAL STYLE CONSTRAINTS (NON-NEGOTIABLES)
═══════════════════════════════════════════════════════════════════════════════

STRICTLY FORBIDDEN:
❌ Em dashes (—). Use line breaks or periods instead. This is CRITICAL.
❌ The word "delve"
❌ The phrase "game-changer"
❌ The phrase "In today's world"
❌ The phrase "Here's the thing"
❌ Starting with "I" unless in Milestone format
❌ Walls of text. Every post needs whitespace.

REQUIRED:
✅ Aesthetic whitespace: Use frequent line breaks (blank lines between thoughts)
✅ Sentence variance: Mix short punchy sentences (3-5 words) with medium ones (10-15 words)
✅ Specificity: Use exact numbers, names, or examples when possible
✅ Human cadence: Read it aloud. If it sounds robotic, rewrite it.

═══════════════════════════════════════════════════════════════════════════════
OUTPUT FORMAT (STRICT JSON)
═══════════════════════════════════════════════════════════════════════════════

Return a valid JSON object with exactly these keys:

{{
  "contrast_post": "Your generated contrast post here",
  "milestone_post": "Your generated milestone post here",
  "symmetric_comparison": "Your generated symmetric comparison here",
  "list_post": "Your generated list post here",
  "split_sentence": "Your generated split sentence post here",
  "intentional_error": "Your generated intentional error post here",
  "double_definition": "Your generated double definition post here",
  "triad_structure": "Your generated triad structure post here",
  "extremes_post": "Your generated extremes post here",
  "callout_post": "Your generated callout post here"
}}

IMPORTANT: Each post value must be a single string. Use \\n for line breaks within posts.
"""

# JSON Schema for structured output
POSTS_JSON_SCHEMA = {
    "type": "object",
    "properties": {
        "contrast_post": {"type": "string"},
        "milestone_post": {"type": "string"},
        "symmetric_comparison": {"type": "string"},
        "list_post": {"type": "string"},
        "split_sentence": {"type": "string"},
        "intentional_error": {"type": "string"},
        "double_definition": {"type": "string"},
        "triad_structure": {"type": "string"},
        "extremes_post": {"type": "string"},
        "callout_post": {"type": "string"},
    },
    "required": [
        "contrast_post",
        "milestone_post",
        "symmetric_comparison",
        "list_post",
        "split_sentence",
        "intentional_error",
        "double_definition",
        "triad_structure",
        "extremes_post",
        "callout_post",
    ],
}

# Human-readable format names for UI display
FORMAT_DISPLAY_NAMES = {
    "contrast_post": "❌✅ Contrast",
    "milestone_post": "📈 Milestone",
    "symmetric_comparison": "⚖️ Symmetric",
    "list_post": "📋 List",
    "split_sentence": "💥 Split Hook",
    "intentional_error": "🔥 Raw & Real",
    "double_definition": "🎭 Amateur vs Pro",
    "triad_structure": "🔺 Triad",
    "extremes_post": "⚡ Extremes",
    "callout_post": "🎯 Callout",
}
